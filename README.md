# 【キャラクターを創り動かす】画像・動画生成AI スタートガイド

## サポートリポジトリ

生成AIであなたの想像するキャラクターをカタチにしよう！
「技術知識」と「リテラシー」が身につく入門書

生成AI技術で「あなたのオリジナルキャラクター」を生み出すことを目指す入門書です。
自分の中にあるイメージを生成AI技術を使って表現し、動きを与えてみましょう。
さらに、クラウドコンピューティング（Google Colab）を使った画像生成環境を利用することで、
インターネット環境さえあれば画像や動画を生成できる方法も解説します。

<!-- 書影: images/cover.png を配置してください（未配置のため現在は非表示） -->
<img src="images/cover.png" alt="【キャラクターを創り動かす】画像・動画生成AI スタートガイド 書影" width="280" align="right">

本リポジトリは、SBクリエイティブより発売の書籍『**【キャラクターを創り動かす】画像・動画生成AI スタートガイド**』の公式サポートコンテンツです。

ComfyUI を使った画像・動画生成のワークフロー、テンプレート、Google Colab ノートブックを提供しています。

## 書籍情報

- **発売日**: 2026年9月19日（土）
- **ISBN**: 978-4-8156-3767-5
- **サイズ**: B5判 / 272ページ
- **定価**: 2,860円（本体2,600円＋10%税）
- **著者**: [AICU media 編集部](https://x.com/aicuai) / [白井 暁彦](https://x.com/o_ob) / [道草 雑草子（ざすこ）](https://x.com/zasuko_michiksa)
- **出版社**: SBクリエイティブ
- **書籍ページ**: https://www.sbcr.jp/product/4815637675/
- **対応環境**: Google Colab & Stability Matrix

## 目次

- 第1章　生成AIの基礎知識を身に付けよう
- 第2章　画像と動画を生成する準備を整えよう
- 第3章　画像を生成してみよう
- 第4章　オリジナルキャラクターを創り出そう
- 第5章　動画を生成してみよう
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

## バージョンと再現性について

書籍は刊行後に修正できませんが、**ソフトウェアは毎週変わります**。
そのため本リポジトリでは「いつの時点の組み合わせで動作確認したか」を明示します。

### リリースタグ

書籍の各刷・各章の検証時点に対応する **リリースタグ**を打ちます。

| タグ | 時点 | 内容 |
|---|---|---|
| `beta` | 初稿 | 執筆・検証中のスナップショット |
| `rc1` | 校了 | 校了時点。誌面と一致 |
| **`v1.0`** | **発売日（2026-09-19）** | **第1刷に対応する正式版** |

```bash
# 書籍（第1刷）に対応する内容を取得する
git clone https://github.com/aicuai/Book-SG26.git
cd Book-SG26
git checkout v1.0
```

タグを使えば、**あなたの手元と書籍の記述が確実に一致**します。
最新版（main）は改善が入っている代わりに、書籍の画面と異なる場合があります。

### 動作確認済みの組み合わせ

ノートブックは **AICU ComfyUI LTS**（AICU が動作検証した ComfyUI とカスタムノードの組み合わせ）を
使用します。ComfyUI 本体は2〜4週ごとに新版が出るため、最新版をそのまま使うと
**実行した日によって結果が変わる**ことがあります。LTS はこれを防ぐ仕組みです。

各ノートブックの冒頭に、検証時点の版数を記載しています。

### うまく動かないとき

1. **タグを確認** — `git checkout` で書籍に対応するタグに切り替える
2. **Issue で報告** — [Issues](https://github.com/aicuai/Book-SG26/issues) に、
   実行日・エラーメッセージ・使用したノートブック名を添えてご報告ください
3. モデルの配布元が変更・削除された場合は、本リポジトリ側で追従します

> 生成AI分野は変化が速く、書籍執筆時点と現在で状況が変わることがあります。
> 本リポジトリは**継続的に検証・更新**し、読者の皆さまが最後まで手を動かせる状態を維持します。
