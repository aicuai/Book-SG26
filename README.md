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
| `Notebooks/ComfyUI.ipynb` | Google Colab 用 ComfyUI 起動ノートブック（Cloudflare トンネル） |
| `Notebooks/ComfyUI_pinggy.ipynb` | Google Colab 用 ComfyUI 起動ノートブック（Pinggy トンネル） |
| `Notebooks/Stable_Diffusion_WebUI_Forge_classic.ipynb` | Stable Diffusion WebUI Forge classic 起動ノートブック |
| `Notebooks/ComfyUI_Launch_Notebook_Wan2_2_I2V_v12.ipynb` | Wan2.2 I2V 用 ComfyUI 起動ノートブック |
| `Notebooks/ComfyUI_Launch_Notebook_SD2_R2V_v15.ipynb` | SD2 R2V 用 ComfyUI 起動ノートブック |
| `Workflows/` | ComfyUI UI で読み込むワークフロー JSON |
| `Workflows/api/sdxl_txt2img.json` | SDXL 画像生成ワークフロー（API 形式） |
| `Workflows/api/wan22_t2v.json` | Wan2.2 テキストから動画生成ワークフロー（API 形式） |
| `bench/bench_tunnel.py` | トンネル方式ベンチマークスクリプト |

## Google Colab での使い方

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://j.aicu.ai/CSGP)

1. `Notebooks/ComfyUI_pinggy.ipynb` を [Google Colab で開く](https://j.aicu.ai/CSGP)
2. Civitai API キーを Colab のシークレットに `CIVITAI_KEY` として登録
3. 必要なモデルの URL を各フォルダ欄に入力
4. セルを実行して ComfyUI を起動

詳しい手順は書籍本編およびノートブック内の説明をご参照ください。

### トンネル方式と推奨環境

本書では、Google Colab 上の ComfyUI をお手元のブラウザから WebUI として操作するために、外部公開トンネルを利用します。本リポジトリでは Cloudflare 方式と Pinggy 方式の 2 通りを用意しています。

| 方式 | ノートブック | セッション制限 |
|------|------------|--------------|
| Cloudflare | `Notebooks/ComfyUI.ipynb` | 制限なし（無料） |
| Pinggy | `Notebooks/ComfyUI_pinggy.ipynb` | 1 セッション 60 分（無料枠の場合） |

ご利用環境やワークフローの内容によって、応答速度や大きなファイルのやり取りの安定性が異なる場合があります。書籍本編で扱う Wan2.2 など、比較的負荷の高いワークフローを継続的に試す場合は、**Google Colab Pro と Pinggy の有料プランの併用**もご検討ください。より上位の GPU や長いセッション時間が選択できるようになります。

- Pinggy: https://pinggy.io/
- Cloudflare Tunnel: https://www.cloudflare.com/products/tunnel/

## ワークフロー

`Workflows/api/` ディレクトリに ComfyUI API 形式のワークフロー JSON を収録しています。`Workflows/` 直下は ComfyUI の UI で読み込むワークフロー JSON です。

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

- Google Colab（無料／Pro いずれも、エンドユーザーは Pinggy または Cloudflare トンネル経由で WebUI に接続）
- ローカル ComfyUI Desktop（NVIDIA GPU 推奨）
- SSH 接続環境（AICU サーバー等）

## 関連リンク

- [書籍情報（SBクリエイティブ）](https://www.sbcr.jp/product/4815637675/)
- [Google Colab ノートブック](https://j.aicu.ai/CSGP)
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
