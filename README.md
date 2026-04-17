# 【キャラクターを創り動かす】画像・動画生成AI スタートガイド

## サポートリポジトリ

生成AIであなたの想像するキャラクターをカタチにしよう！
「技術知識」と「リテラシー」が身につく入門書

本リポジトリは、SBクリエイティブより発売の書籍『**【キャラクターを創り動かす】画像・動画生成AI スタートガイド**』の公式サポートコンテンツです。

ComfyUI を使った画像・動画生成のワークフロー、テンプレート、Google Colab ノートブックを提供しています。

## 書籍情報

- **発売日**: 2026年7月10日（金）
- **ISBN**: 978-4-8156-3767-5
- **サイズ**: B5判 / 160ページ
- **定価**: 2,860円（本体2,600円+10%税）
- **著者**: AICU media 編集部 / 白井暁彦 / 道草 雑草子
- **出版社**: SBクリエイティブ

## 目次

- 第1章　生成AIの基礎知識を身に付けよう
- 第2章　画像と動画を生成する準備を整えよう
- 第3章　画像を生成してみよう
- 第4章　動画を生成してみよう
- 第5章　生成AIをクリエイティブに活用しよう
- 第6章　生成AIとの向き合い方を考えよう
- 第7章　生成AIと共に歩んでいこう

## コンテンツ

| ファイル | 内容 |
|---------|------|
| `ComfyUI.ipynb` | Google Colab 用 ComfyUI 起動ノートブック（Cloudflare トンネル） |
| `ComfyUI-pinggy.ipynb` | Google Colab 用 ComfyUI 起動ノートブック（Pinggy トンネル） |
| `api-workflows/sdxl_txt2img.json` | SDXL 画像生成ワークフロー |
| `api-workflows/wan22_t2v.json` | Wan2.2 テキストから動画生成ワークフロー |
| `bench/bench_tunnel.py` | トンネル方式ベンチマークスクリプト |

## Google Colab での使い方

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://j.aicu.ai/CSGC)

1. `ComfyUI-pinggy.ipynb` を [Google Colab で開く](https://j.aicu.ai/CSGC)
2. Civitai API キーを Colab のシークレットに `CIVITAI_KEY` として登録
3. 必要なモデルの URL を各フォルダ欄に入力
4. セルを実行して ComfyUI を起動

詳しい手順は書籍本編およびノートブック内の説明をご参照ください。

### Pinggy 版について

Pinggy 版（`ComfyUI-pinggy.ipynb`）は SSH トンネルを利用しており、Cloudflare 版と比較して以下の利点があります：

- ComfyUI の起動・再起動が高速（20秒〜1分）
- 画像・動画のアップロードが安定
- Wan2.2 等の重いワークフローが正常に完了

Pinggy は無料枠で **60分のセッション** が利用できます。セッション切れの場合はセルを再実行してください。
Pinggy の詳細: https://pinggy.io/

> Cloudflare 版（`ComfyUI.ipynb`）も引き続き利用可能ですが、大きなペイロードを扱うワークフローでは不安定な場合があります。

## ワークフロー

`api-workflows/` ディレクトリに ComfyUI API 形式のワークフロー JSON を収録しています。

| ワークフロー | 用途 | 必要モデル |
|-------------|------|-----------|
| `sdxl_txt2img.json` | SDXL 画像生成（軽量テスト用） | Sierunami.v1 checkpoint |
| `wan22_t2v.json` | Wan2.2 テキスト→動画（重量テスト用） | Wan2.2 T2V 14B + UMT5-XXL + Wan2.2 VAE |

ワークフローは ComfyUI の「Load API workflow」で読み込めます。モデルのダウンロード URL はノートブック内のメモセルを参照してください。

## ベンチマーク（トンネル速度比較）

Cloudflare と Pinggy のトンネル方式を定量比較するスクリプトです。

### 実行方法

ComfyUI が起動した状態で、Colab のセル or ターミナルから実行します：

```bash
# ベースライン（ローカル直接接続）
python bench/bench_tunnel.py --host http://127.0.0.1:8188 --label local

# Cloudflare トンネル経由
python bench/bench_tunnel.py --host https://xxxx.trycloudflare.com --label cloudflare

# Pinggy トンネル経由
python bench/bench_tunnel.py --host https://xxxx.a.pinggy.link --label pinggy

# SDXL のみ（軽量テスト、30秒程度）
python bench/bench_tunnel.py --host https://xxxx.a.pinggy.link --label pinggy --test sdxl

# Wan2.2 のみ（重量テスト、数分）
python bench/bench_tunnel.py --host https://xxxx.a.pinggy.link --label pinggy --test wan22

# 結果を比較
python bench/bench_tunnel.py --compare results/
```

### 計測項目

| テスト | 内容 | 切り分け対象 |
|--------|------|-------------|
| latency | API レスポンス時間 | トンネルのオーバーヘッド |
| sdxl | SDXL txt2img (1024x1024) | 小ペイロード画像生成 |
| wan22 | Wan2.2 T2V (832x480, 33f) | 大ペイロード動画生成 |
| upload | 画像アップロード | multipart POST の安定性 |

結果は `results/tunnel_bench_{label}.json` に保存されます。

## 対応環境

- Google Colab (T4 / L4 GPU)
- ローカル ComfyUI Desktop
- SSH 接続環境（AICU サーバー等）

## 関連リンク

- [書籍情報（SBクリエイティブ）](https://www.sbcr.jp/product/4815637675/)
- [Google Colab ノートブック](https://j.aicu.ai/CSGC)
- [note.com 連載](https://j.aicu.ai/CSG)
- [AICU media](https://ja.aicu.ai/)
- [ComfyUI 公式](https://www.comfy.org/)
- [ComfyUI ワークフローテンプレート](https://www.comfy.org/ja/workflows/comfyui/)
- ハッシュタグ: [#AIcsg](https://x.com/search?q=%23AIcsg)

## シリーズ既刊

- [画像生成AI Stable Diffusion スタートガイド](https://github.com/aicuai/Book-StartGuideSDXL)（SDXL対応・第3刷）
- [ComfyUI マスターガイド](https://j.aicu.ai/comfysb)

## ライセンス

書籍連動コンテンツです。ワークフロー JSON は自由にご利用いただけます。
ノートブック原作：ざすこ（道草 雑草子）

## Issues

不具合報告・ご質問は [Issues](../../issues) へお願いします。
