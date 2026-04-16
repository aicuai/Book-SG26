#!/usr/bin/env python3
"""
ComfyUI トンネル方式ベンチマーク (Cloudflare vs Pinggy)

ComfyUI HTTP API 経由で各トンネル方式の応答速度・安定性を比較計測。
aicu-bench パターン準拠: cold/warm 分離、median 報告、GPU テレメトリ。

計測項目:
  1. API 応答時間 (/system_stats へのレイテンシ)
  2. 画像生成 (SDXL txt2img: 小ペイロード、~30s)
  3. 動画生成 (Wan2.2 t2v: 大ペイロード、数分)
  4. 画像アップロード (multipart POST: ペイロードサイズ依存)

Usage:
    # ローカル (トンネルなし、ベースライン)
    python bench_tunnel.py --host http://127.0.0.1:8188 --label local --runs 3

    # Cloudflare トンネル経由
    python bench_tunnel.py --host https://xxx.trycloudflare.com --label cloudflare --runs 3

    # Pinggy トンネル経由
    python bench_tunnel.py --host https://xxx.a.pinggy.link --label pinggy --runs 3

    # SDXL のみ (軽量テスト)
    python bench_tunnel.py --host https://xxx.a.pinggy.link --label pinggy --test sdxl

    # Wan2.2 のみ (重量テスト)
    python bench_tunnel.py --host https://xxx.a.pinggy.link --label pinggy --test wan22

    # 結果比較
    python bench_tunnel.py --compare results/
"""

import argparse
import json
import os
import subprocess
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

DEFAULT_RUNS = 3
WORKFLOW_DIR = Path(__file__).parent.parent / "workflows"


# ============================================================
# GPU テレメトリ
# ============================================================

def get_nvidia_smi() -> dict:
    """nvidia-smi から GPU 情報を取得 (Colab / ローカル両対応)"""
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=gpu_name,memory.used,memory.total,temperature.gpu,power.draw",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            parts = [p.strip() for p in result.stdout.strip().split(",")]
            return {
                "gpu_name": parts[0],
                "vram_used_mb": int(parts[1]),
                "vram_total_mb": int(parts[2]),
                "temp_c": int(parts[3]),
                "power_w": float(parts[4]),
            }
    except Exception:
        pass
    return {}


# ============================================================
# ComfyUI API ヘルパー
# ============================================================

def api_get(host: str, path: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(f"{host}{path}")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def api_post(host: str, path: str, data: dict, timeout: int = 30) -> dict:
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{host}{path}",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def get_system_stats(host: str) -> dict:
    try:
        return api_get(host, "/system_stats", timeout=10)
    except Exception:
        return {}


def free_memory(host: str):
    try:
        api_post(host, "/free", {"unload_models": True, "free_memory": True}, timeout=10)
    except Exception:
        pass
    time.sleep(2)


def queue_prompt(host: str, workflow: dict) -> str:
    result = api_post(host, "/prompt", {"prompt": workflow})
    return result.get("prompt_id", "")


def wait_for_completion(host: str, prompt_id: str, timeout: int = 600) -> dict:
    start = time.time()
    while time.time() - start < timeout:
        try:
            history = api_get(host, f"/history/{prompt_id}", timeout=10)
            if prompt_id in history:
                entry = history[prompt_id]
                status = entry.get("status", {})
                if status.get("status_str") == "error":
                    return {"success": False, "error": "ComfyUI execution error"}
                if status.get("completed", False):
                    return {"success": True, "outputs": entry.get("outputs", {})}
                outputs = entry.get("outputs", {})
                for node_output in outputs.values():
                    if "images" in node_output or "gifs" in node_output:
                        return {"success": True, "outputs": outputs}
        except Exception:
            pass
        time.sleep(1)
    return {"success": False, "error": "timeout"}


def upload_image(host: str, image_path: str) -> dict:
    """画像アップロード (multipart/form-data) — トンネルのペイロード耐性を測る"""
    import mimetypes
    boundary = "----BenchBoundary"
    filename = os.path.basename(image_path)
    mime = mimetypes.guess_type(image_path)[0] or "image/png"

    with open(image_path, "rb") as f:
        file_data = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="image"; filename="{filename}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        f"{host}/upload/image",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


# ============================================================
# ベンチマーク関数
# ============================================================

def bench_latency(host: str, runs: int) -> list:
    """API レイテンシ計測 (/system_stats への GET)"""
    results = []
    for i in range(1, runs + 1):
        start = time.time()
        try:
            api_get(host, "/system_stats", timeout=10)
            elapsed = round(time.time() - start, 3)
            success = True
        except Exception as e:
            elapsed = round(time.time() - start, 3)
            success = False
        results.append({
            "run": i,
            "elapsed_s": elapsed,
            "success": success,
            "timestamp": datetime.now().isoformat(),
        })
        print(f"  [latency] run {i}/{runs}: {elapsed}s ({'OK' if success else 'FAIL'})")
    return results


def bench_workflow(host: str, workflow_path: Path, label: str, runs: int,
                   timeout: int = 600) -> list:
    """ワークフロー実行ベンチマーク (cold + warm)"""
    with open(workflow_path, encoding="utf-8") as f:
        workflow = json.load(f)

    results = []
    for i in range(1, runs + 1):
        print(f"\n  [{label}] Run {i}/{runs}")

        # Cold start
        free_memory(host)
        gpu_before = get_nvidia_smi()
        start = time.time()
        try:
            pid = queue_prompt(host, workflow)
            if not pid:
                raise RuntimeError("Failed to queue prompt")
            result = wait_for_completion(host, pid, timeout=timeout)
            cold_elapsed = round(time.time() - start, 3)
            cold_ok = result.get("success", False)
        except Exception as e:
            cold_elapsed = round(time.time() - start, 3)
            cold_ok = False
            print(f"    COLD ERROR: {e}")
        gpu_after_cold = get_nvidia_smi()
        print(f"    cold: {cold_elapsed}s ({'OK' if cold_ok else 'FAIL'})")

        # Warm start
        start = time.time()
        try:
            pid = queue_prompt(host, workflow)
            if not pid:
                raise RuntimeError("Failed to queue prompt")
            result = wait_for_completion(host, pid, timeout=timeout)
            warm_elapsed = round(time.time() - start, 3)
            warm_ok = result.get("success", False)
        except Exception as e:
            warm_elapsed = round(time.time() - start, 3)
            warm_ok = False
            print(f"    WARM ERROR: {e}")
        gpu_after_warm = get_nvidia_smi()
        print(f"    warm: {warm_elapsed}s ({'OK' if warm_ok else 'FAIL'})")

        results.append({
            "run": i,
            "cold_start_s": cold_elapsed if cold_ok else None,
            "warm_start_s": warm_elapsed if warm_ok else None,
            "cold_success": cold_ok,
            "warm_success": warm_ok,
            "gpu_before": gpu_before,
            "gpu_after_cold": gpu_after_cold,
            "gpu_after_warm": gpu_after_warm,
            "timestamp": datetime.now().isoformat(),
        })

    return results


def bench_upload(host: str, image_path: str, runs: int) -> list:
    """画像アップロード計測"""
    if not os.path.exists(image_path):
        print(f"  [upload] SKIP: {image_path} not found")
        return []

    file_size_mb = round(os.path.getsize(image_path) / 1024 / 1024, 2)
    results = []
    for i in range(1, runs + 1):
        start = time.time()
        try:
            upload_image(host, image_path)
            elapsed = round(time.time() - start, 3)
            success = True
        except Exception as e:
            elapsed = round(time.time() - start, 3)
            success = False
            print(f"    ERROR: {e}")
        results.append({
            "run": i,
            "elapsed_s": elapsed,
            "success": success,
            "file_size_mb": file_size_mb,
            "timestamp": datetime.now().isoformat(),
        })
        print(f"  [upload] run {i}/{runs}: {elapsed}s ({file_size_mb}MB) ({'OK' if success else 'FAIL'})")
    return results


# ============================================================
# 統計ヘルパー
# ============================================================

def median(values):
    s = sorted(v for v in values if v is not None)
    n = len(s)
    if n == 0:
        return None
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]


# ============================================================
# 結果比較
# ============================================================

def compare_results(results_dir: str):
    """複数の結果 JSON を読み込んで比較表を出力"""
    results_path = Path(results_dir)
    files = sorted(results_path.glob("tunnel_bench_*.json"))

    if not files:
        print(f"No result files found in {results_dir}")
        return

    print(f"\n{'='*70}")
    print(f"  Tunnel Benchmark Comparison")
    print(f"{'='*70}")
    print(f"\n{'Label':<15} {'Latency':<12} {'SDXL cold':<12} {'SDXL warm':<12} {'Wan2.2 cold':<14} {'Wan2.2 warm':<12}")
    print(f"{'-'*15} {'-'*12} {'-'*12} {'-'*12} {'-'*14} {'-'*12}")

    for f in files:
        with open(f) as fp:
            data = json.load(fp)
        label = data.get("tunnel_method", "?")
        lat = data.get("latency", {}).get("median_s", "-")
        sdxl_c = data.get("sdxl_txt2img", {}).get("cold_start_median_s", "-")
        sdxl_w = data.get("sdxl_txt2img", {}).get("warm_start_median_s", "-")
        wan_c = data.get("wan22_t2v", {}).get("cold_start_median_s", "-")
        wan_w = data.get("wan22_t2v", {}).get("warm_start_median_s", "-")

        fmt = lambda v: f"{v:.3f}s" if isinstance(v, (int, float)) else str(v)
        print(f"{label:<15} {fmt(lat):<12} {fmt(sdxl_c):<12} {fmt(sdxl_w):<12} {fmt(wan_c):<14} {fmt(wan_w):<12}")

    print()


# ============================================================
# メイン
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="ComfyUI Tunnel Benchmark (Cloudflare vs Pinggy)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--host", type=str, required=False,
                        default="http://127.0.0.1:8188",
                        help="ComfyUI URL (トンネル URL or localhost)")
    parser.add_argument("--label", type=str, required=False, default="local",
                        help="計測ラベル (local / cloudflare / pinggy)")
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS,
                        help="計測回数 (default: 3)")
    parser.add_argument("--test", type=str, default="all",
                        choices=["all", "latency", "sdxl", "wan22", "upload"],
                        help="実行するテスト")
    parser.add_argument("--upload-image", type=str, default=None,
                        help="アップロードテスト用画像パス")
    parser.add_argument("--timeout", type=int, default=600,
                        help="ワークフロー実行タイムアウト秒数")
    parser.add_argument("--output-dir", type=str,
                        default=os.path.join(os.path.dirname(__file__), "..", "results"))
    parser.add_argument("--compare", type=str, default=None,
                        help="結果ディレクトリを指定して比較表を出力")
    args = parser.parse_args()

    # 比較モード
    if args.compare:
        compare_results(args.compare)
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  ComfyUI Tunnel Benchmark")
    print(f"  Host:  {args.host}")
    print(f"  Label: {args.label}")
    print(f"  Runs:  {args.runs}")
    print(f"  Test:  {args.test}")
    print(f"{'='*60}")

    # 接続テスト
    print("\nChecking ComfyUI connection...", end=" ")
    sys_stats = get_system_stats(args.host)
    if sys_stats:
        print("OK")
    else:
        print("FAILED — ComfyUI が応答しません。URL を確認してください。")
        return

    summary = {
        "experiment": "tunnel-bench",
        "tunnel_method": args.label,
        "host": args.host,
        "runs": args.runs,
        "comfyui_info": sys_stats,
        "generated": datetime.now().isoformat(),
    }

    run_all = args.test == "all"

    # 1. API レイテンシ
    if run_all or args.test == "latency":
        print(f"\n--- API Latency ---")
        lat_results = bench_latency(args.host, args.runs * 3)  # レイテンシは多めに
        lat_times = [r["elapsed_s"] for r in lat_results if r["success"]]
        summary["latency"] = {
            "median_s": median(lat_times),
            "min_s": min(lat_times) if lat_times else None,
            "max_s": max(lat_times) if lat_times else None,
            "results": lat_results,
        }
        print(f"  Median: {summary['latency']['median_s']}s")

    # 2. SDXL txt2img
    sdxl_wf = WORKFLOW_DIR / "sdxl_txt2img.json"
    if (run_all or args.test == "sdxl") and sdxl_wf.exists():
        print(f"\n--- SDXL txt2img ---")
        sdxl_results = bench_workflow(args.host, sdxl_wf, "sdxl", args.runs,
                                      timeout=args.timeout)
        cold_med = median([r["cold_start_s"] for r in sdxl_results])
        warm_med = median([r["warm_start_s"] for r in sdxl_results])
        summary["sdxl_txt2img"] = {
            "cold_start_median_s": cold_med,
            "warm_start_median_s": warm_med,
            "workflow": "workflows/sdxl_txt2img.json",
            "results": sdxl_results,
        }
        print(f"\n  SDXL cold median: {cold_med}s / warm median: {warm_med}s")

    # 3. Wan2.2 t2v
    wan_wf = WORKFLOW_DIR / "wan22_t2v.json"
    if (run_all or args.test == "wan22") and wan_wf.exists():
        print(f"\n--- Wan2.2 T2V ---")
        wan_results = bench_workflow(args.host, wan_wf, "wan22", args.runs,
                                     timeout=args.timeout)
        cold_med = median([r["cold_start_s"] for r in wan_results])
        warm_med = median([r["warm_start_s"] for r in wan_results])
        summary["wan22_t2v"] = {
            "cold_start_median_s": cold_med,
            "warm_start_median_s": warm_med,
            "workflow": "workflows/wan22_t2v.json",
            "results": wan_results,
        }
        print(f"\n  Wan2.2 cold median: {cold_med}s / warm median: {warm_med}s")

    # 4. 画像アップロード
    if (run_all or args.test == "upload") and args.upload_image:
        print(f"\n--- Image Upload ---")
        up_results = bench_upload(args.host, args.upload_image, args.runs)
        up_times = [r["elapsed_s"] for r in up_results if r["success"]]
        summary["upload"] = {
            "median_s": median(up_times),
            "file_size_mb": up_results[0]["file_size_mb"] if up_results else None,
            "results": up_results,
        }
        print(f"  Upload median: {summary['upload']['median_s']}s")

    # 結果保存
    out_file = output_dir / f"tunnel_bench_{args.label}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"  Results saved: {out_file}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
