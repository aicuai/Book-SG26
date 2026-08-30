# 【キャラクターを創り動かす】画像・動画生成AI スタートガイド

## サポートリポジトリ

生成AIであなたの想像するキャラクターをカタチにしよう！
「技術知識」と「リテラシー」が身につく入門書

生成AI技術で「あなたのオリジナルキャラクター」を生み出すことを目指す入門書です。
自分の中にあるイメージを生成AI技術を使って表現し、動きを与えてみましょう。
さらに、クラウドコンピューティング（Google Colab）を使った画像生成環境を利用することで、
インターネット環境さえあれば画像や動画を生成できる方法も解説します。

<a href="https://www.sbcr.jp/product/4815637675/">
<img src="images/SG26.png" alt="【キャラクターを創り動かす】画像・動画生成AI スタートガイド 書影" width="280" align="right">
</a>

本リポジトリは、SBクリエイティブより発売の書籍『**【キャラクターを創り動かす】画像・動画生成AI スタートガイド**』の公式サポートコンテンツです。

ComfyUI を使った画像・動画生成のワークフロー、テンプレート、Google Colab ノートブックを提供しています。

## この本で作れるもの

[![サンプル動画を再生](images/chap5_r2v_poster.jpg)](prompts/chap5/Seedance2.0_R2V%E2%80%97Movie_720p_SAMPLE.mp4)

**▶️ [「リズメイの待ち合わせ」を再生する](prompts/chap5/Seedance2.0_R2V%E2%80%97Movie_720p_SAMPLE.mp4)**（15秒 / 音声あり）

オリジナルキャラクター「響姫メイ」と「渋谷リズ」が渋谷で待ち合わせる15秒のCM風動画です。
キャラクター設定 → シナリオ → イメージボード → 動画生成までを、**本書の手順どおりに作れます**。

この動画を作るのに使ったプロンプトは [第5章のプロンプト集](prompts/chap5/)（https://j.aicu.ai/SG26c5 ）で全文公開しています。

## 書籍情報

- **発売日**: 2026年9月19日（土）
- **ISBN**: 978-4-8156-3767-5
- **サイズ**: B5判 / 320ページ
- **定価**: 3,300円（本体3,000円＋10%税）
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

## ディレクトリ構成

書籍内で参照する固定ディレクトリです。

| ディレクトリ | 内容 |
|---|---|
| [`ipynb/`](ipynb/) | Google Colab 用ノートブック（ComfyUI / Forge / LoRA 学習） |
| [`prompts/`](prompts/) | 章ごとのプロンプト素材 |
| [`workflow/`](workflow/) | ComfyUI ワークフロー JSON（UI 形式） |
| [`api-workflows/`](api-workflows/) | ComfyUI ワークフロー JSON（API 形式） |
| [`WebUI_Launch_Setup_Files/`](WebUI_Launch_Setup_Files/) | WebUI (Forge) 用の設定ファイル（Config-Presets / prompt-all-in-one） |
| [`images/`](images/) | ノートブックが `input/` に自動取得するサンプル画像（`sg26_*.png`）、書影、解説図 |
| [`bench/`](bench/) | トンネル速度ベンチマーク |

### 主なコンテンツ

| ファイル | 内容 |
|---------|------|
| [`ipynb/ComfyUI-pinggy.ipynb`](ipynb/ComfyUI-pinggy.ipynb) | **ComfyUI 起動ノートブック（Pinggy版）— 書籍で使用するのはこちら** |
| [`ipynb/ComfyUI.ipynb`](ipynb/ComfyUI.ipynb) | ComfyUI 起動ノートブック（Cloudflare版・時間制限なしの代替） |
| [`ipynb/Stable_Diffusion_WebUI_Forge_classic.ipynb`](ipynb/Stable_Diffusion_WebUI_Forge_classic.ipynb) | Forge (WebUI) 起動ノートブック |
| [`ipynb/SG26-LoRA-KohyaTrainer.ipynb`](ipynb/SG26-LoRA-KohyaTrainer.ipynb) | LoRA 学習ノートブック |
| [`prompts/chap5/README.md`](prompts/chap5/README.md) | 第5章のプロンプト全文（動画サンプル付き） |
| [`bench/bench_tunnel.py`](bench/bench_tunnel.py) | トンネル方式ベンチマークスクリプト |

## 短縮URL

書籍紙面の QR コードはこの短縮URLを指しています。リポジトリ構成が変わっても、
短縮URLの転送先を付け替えることで**リンクは維持されます**。

| 短縮URL | 開いたとき | 内容 | 紙面 |
|---|---|---|---|
| https://j.aicu.ai/SG26P | 🚀 **Colab で起動** | ComfyUI 起動ノートブック Pinggy 版（**書籍で使用**） | 2章 |
| https://j.aicu.ai/CSGF | 🚀 **Colab で起動** | Forge Classic 起動ノートブック | 2-5 p.68-69 |
| https://j.aicu.ai/SG26CW | 🚀 **Colab で起動** | ComfyUI 起動ノートブック Wan2.2 版 | 5-2 / 5-3 p.228-229 |
| https://j.aicu.ai/SG26CR | 🚀 **Colab で起動** | ComfyUI 起動ノートブック Seedance 2.0 R2V | 5-4 p.254-255 |
| https://j.aicu.ai/LoRA26 | 🚀 **Colab で起動** | LoRA Trainer LTS 版（HollowStrawberry 式） | — |
| https://j.aicu.ai/SG26LoRA | 🚀 **Colab で起動** | LoRA 学習ノートブック（付録） | 4-5 参照 |
| https://j.aicu.ai/SG26C | 🚀 **Colab で起動** | ComfyUI 起動ノートブック Cloudflare 版（代替） | — |
| https://j.aicu.ai/SG26Wan | 💾 **ダウンロード** | Wan2.2 I2V ワークフロー | 5-2 p.228-229 |
| https://j.aicu.ai/SG26WanF | 💾 **ダウンロード** | Wan2.2 FLF2V ワークフロー | 5-3 p.240-241 |
| https://j.aicu.ai/SG26R2V | 💾 **ダウンロード** | Seedance 2.0 R2V ワークフロー | 5-4 p.254-255 |
| https://j.aicu.ai/SG26US | 💾 **ダウンロード** | SeedVR2 アップスケールワークフロー | 5-4 |
| https://j.aicu.ai/CSGC | 💾 **ダウンロード** | ComfyUI 起動ノートブック（GitHub 表示） | — |
| https://j.aicu.ai/SG26c5 | 📂 一覧を表示 | 第5章のプロンプト集（サンプル動画つき） | 5章 |
| https://j.aicu.ai/SG26A | 🛒 外部サイト | 書籍を購入する（Amazon） | — |
| https://j.aicu.ai/CSG | 🔗 外部サイト | note.com 連載 | — |

### 🚀 と 💾 で紙面の手順が変わります

**🚀 Colab で起動** — QR を読むと **Google Colab でノートブックが開きます**。
ダウンロードは不要です。ただし **Colab で GitHub から開いたノートブックは
編集が保存されません**。読者はモデルURL等のフォーム欄を書き換えるので、
紙面には次の一行が必要です。

> 実行する前に、上部の「**ドライブにコピー**」をクリックしてください。
> コピーしないと、設定を変えてもページを閉じたときに消えてしまいます。

**💾 ダウンロード** — GitHub のファイルページが開きます。
右上の**ダウンロードアイコン**をクリックして保存し、ComfyUI に読み込みます。

> ⚠️ **ワークフロー（.json）は Colab では開けません。**
> Colab の GitHub ローダは `.ipynb` しか受け付けず、JSON を渡すと
> `invalid notebook` になります。**ノートブックとワークフローで手順が違う**のは
> このためです。5章 p.228-229 は同じ見開きに両方の QR があるので、書き分けが要ります。

この表は [`qa/shortlinks.yml`](qa/shortlinks.yml) が正本で、毎週の QA で転送先まで自動検査しています。
**短縮URLの発行・付け替えは人が行います**（自動化していません）。

## Google Colab での使い方

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://j.aicu.ai/SG26P)

**書籍で使用するのは Pinggy 版です。**

1. [`ipynb/ComfyUI-pinggy.ipynb` を Google Colab で開く](https://j.aicu.ai/SG26P)
2. **ファイル → ドライブにコピーを保存**（そのままでは編集内容を保存できません）
3. Civitai API キーを Colab のシークレットに `CIVITAI_KEY` として登録
4. 必要なモデルの URL を各フォルダ欄に入力
5. セルを実行して ComfyUI を起動
6. 実行ログに表示された Pinggy の URL を開き、**赤い「Enter site」ボタン**をクリック

詳しい手順は書籍本編およびノートブック内の説明をご参照ください。

### トンネルについて

ComfyUI の画面を Colab の外から開くために、トンネルを経由します。
**方式ごとにノートブックが分かれています。**

| ノートブック | 方式 | 特徴 |
|---|---|---|
| **[`ComfyUI-pinggy.ipynb`](ipynb/ComfyUI-pinggy.ipynb)**<br>https://j.aicu.ai/SG26P | Pinggy | **書籍で使用。** 起動・再起動が高速（20秒〜1分）。画像・動画のアップロードが安定し、Wan2.2 等の重いワークフローが完走しやすい。無料枠は **60分**（切れたらセルを再実行） |
| [`ComfyUI.ipynb`](ipynb/ComfyUI.ipynb)<br>https://j.aicu.ai/SG26C | Cloudflare | 時間制限なし。ただし大きなペイロードを扱うワークフローでは不安定な場合があります |

Pinggy を使うと、URL を開いたときに次の確認画面が表示されます。
**赤い「Enter site」ボタン**をクリックすると ComfyUI が開きます（初回のみ）。

<img src="images/pinggy_enter_site.png" alt="Pinggy の確認画面。赤い Enter site ボタンをクリックする" width="420">

Pinggy の詳細: https://pinggy.io/

## ワークフロー

| ディレクトリ | 形式 | 読み込み方 |
|---|---|---|
| [`workflow/`](workflow/) | UI 形式 | ComfyUI 画面にドラッグ＆ドロップ |
| [`api-workflows/`](api-workflows/) | API 形式 | 「Load API workflow」から読み込み |

### `workflow/` — 書籍で使用するワークフロー

| ワークフロー | 対応する節 | 必要モデル |
|---|---|---|
| `SG26Wan22-14B-I2V-GGUF.json` | 5-2 画像から動画 | Wan2.2 I2V A14B (GGUF) + UMT5-XXL + Wan2.1 VAE |
| `SG26Wan22-14B-FLF2V-GGUF.json` | 5-3 開始・終了画像から動画 | 同上（I2V と共通） |
| `WorkFlow_api_seedance2_R2V.json` | 5-4 シナリオから動画 | comfy.org API ノード + SeedVR2 |
| `VideoUpScaleSeedVR2.json` | 動画のアップスケール | SeedVR2 |

### `api-workflows/` — 軽量な検証用

| ワークフロー | 用途 | 必要モデル |
|-------------|------|-----------|
| `sdxl_txt2img.json` | SDXL 画像生成（軽量テスト用） | Sierunami.v1 checkpoint |
| `wan22_t2v.json` | Wan2.2 テキスト→動画（重量テスト用） | Wan2.2 T2V 14B + UMT5-XXL + Wan2.2 VAE |

モデルのダウンロード URL はノートブック内のメモセルを参照してください。

## プロンプト素材

書籍で使用した生成AIプロンプトを全文公開しています。

| | 内容 |
|---|---|
| [第5章](prompts/chap5/) | Wan2.2 I2V / FLF2V、Seedance 2.0 R2V のプロンプト15点とサンプル動画 |

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
- [ComfyUI 起動ノートブック（Pinggy版）を Colab で開く](https://j.aicu.ai/SG26P)
- [note.com 連載](https://j.aicu.ai/CSG)
- [AICU media](https://ja.aicu.ai/)
- [ComfyUI 公式](https://www.comfy.org/)
- [ComfyUI ワークフローテンプレート](https://www.comfy.org/ja/workflows/comfyui/)
- ハッシュタグ: [#AIcsg](https://x.com/search?q=%23AIcsg)

## シリーズ既刊

- [画像生成AI Stable Diffusion スタートガイド](https://github.com/aicuai/Book-StartGuideSDXL)（SDXL対応・第3刷）
- [ComfyUI マスターガイド](https://j.aicu.ai/comfysb)

## 関連リポジトリ

書籍のサポートは複数のリポジトリに分かれています。

| リポジトリ | 役割 |
|---|---|
| **[aicuai/Book-SG26](https://github.com/aicuai/Book-SG26)**（本リポジトリ） | ノートブック・ワークフロー・プロンプト素材 |
| [aicuai/ComfyLTS](https://github.com/aicuai/ComfyLTS) | 動作確認済みバージョンの固定台帳（LTS ライン） |
| [AICU/SDXL-LoRA](https://huggingface.co/AICU/SDXL-LoRA) | 学習用データセットと LoRA |
| [AICU/ComfyLTS](https://huggingface.co/AICU/ComfyLTS) | ControlNet モデル |
| [aicuai/Book-StartGuideSDXL](https://github.com/aicuai/Book-StartGuideSDXL) | 前作（SDXL・黄色本） |

## 本書・本リポジトリを引用するとき

研究・記事・教材で本書やこのリポジトリの内容を参照する場合、出典を示していただければ
許諾の申請は不要です。**引用の範囲を超える転載（章まるごと・図版の再配布）は
[SBクリエイティブ](https://www.sbcr.jp/)にお問い合わせください。**

### 書誌情報

| 項目 | 値 |
|---|---|
| 書名 | 【キャラクターを創り動かす】画像・動画生成AI スタートガイド |
| 著者 | AICU media 編集部、白井 暁彦、道草 雑草子 |
| 出版社 | SBクリエイティブ |
| 発行 | 2026年9月19日 |
| ISBN | 978-4-8156-3767-5 |
| 判型・頁 | B5判 / 320ページ |
| 書籍ページ | https://www.sbcr.jp/product/4815637675/ |
| 購入（Amazon） | https://j.aicu.ai/SG26A |
| サポートリポジトリ | https://github.com/aicuai/Book-SG26 |

### 文中での書き方

> AICU media 編集部・白井暁彦・道草雑草子『【キャラクターを創り動かす】画像・動画生成AI スタートガイド』SBクリエイティブ, 2026, ISBN 978-4-8156-3767-5.

このリポジトリのワークフローやプロンプトを使った場合は、あわせて
`https://github.com/aicuai/Book-SG26` を併記してください。

### BibTeX

日本語フィールドをそのまま使う場合（`upLaTeX` / `LuaLaTeX` + `pBibTeX` 等）:

```bibtex
@book{aicu2026startguide,
  author    = {AICU media 編集部 and 白井 暁彦 and 道草 雑草子},
  title     = {【キャラクターを創り動かす】画像・動画生成AI スタートガイド},
  publisher = {SBクリエイティブ},
  year      = {2026},
  month     = {9},
  isbn      = {978-4-8156-3767-5},
  pages     = {320},
  url       = {https://www.sbcr.jp/product/4815637675/},
  note      = {サポートリポジトリ: \url{https://github.com/aicuai/Book-SG26}}
}
```

ASCII のみの処理系向け（英語論文で引用する場合）:

```bibtex
@book{aicu2026startguide_en,
  author    = {{AICU media Editorial Department} and Shirai, Akihiko and Michikusa, Zasuko},
  title     = {Start Guide to Image and Video Generative {AI}: Create and Animate Your Own Characters},
  publisher = {SB Creative},
  address   = {Tokyo, Japan},
  year      = {2026},
  month     = {9},
  isbn      = {978-4-8156-3767-5},
  pages     = {320},
  language  = {japanese},
  url       = {https://www.sbcr.jp/product/4815637675/},
  note      = {In Japanese. Support repository: \url{https://github.com/aicuai/Book-SG26}}
}
```

> 英題は本書の内容を説明するための便宜的な訳で、公式の英語版書名ではありません。

### 生成した作品を発表するとき

本書の手順で作った画像・動画は**あなたのもの**です。出典表記の義務はありません。
「この本で作りました」と添えていただけると励みになります（[#SG26](https://x.com/hashtag/SG26)）。

ただし**モデルごとに再配布条件が異なります**。下の[ライセンス](#ライセンス)をご確認ください。

## ライセンス

**© AICU Japan 株式会社 / All Rights Reserved.**（[NOTICE.md](./NOTICE.md)）

本リポジトリのワークフロー JSON・プロンプト素材・ノートブックは、
**本書の読者が自分の環境へ複製し、実行し、改変して使う**ことができます。
生成した画像・動画は自分の作品として公開・商用利用できます。

**再配布と、書籍・商用教材への転載には事前の許諾が必要です。**
詳しくは [NOTICE.md](./NOTICE.md) をご覧ください。

**ただし、これらが呼び出すソフトウェアとモデルには、それぞれ別のライセンスがあります。**
とくに**生成した画像の商用利用**と**モデル自体の再配布**は条件が異なるので、
下表をご確認ください（2026-08-20 時点の実査）。

### ソフトウェア

| 対象 | ライセンス |
|---|---|
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | GPL-3.0 |
| [ComfyUI_GGUF](https://github.com/Isi-dev/ComfyUI_GGUF) | Apache-2.0 |
| [ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) | Apache-2.0 |
| [rgthree-comfy](https://github.com/rgthree/rgthree-comfy) | MIT |
| [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) | MIT |
| [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation) | MIT |
| [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) | GPL-3.0 |
| [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | GPL-3.0 |
| [ComfyUI-VFI](https://github.com/GACLove/ComfyUI-VFI) | 記載なし |
| [ComfyUI-PainterI2V](https://github.com/princepainter/ComfyUI-PainterI2V) | 記載なし |
| [ComfyUI-LogicUtils](https://github.com/aria1th/ComfyUI-LogicUtils) | 記載なし |

### モデル

| 対象 | ライセンス |
|---|---|
| [Wan2.2 / Wan2.1 ComfyUI Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) | Apache-2.0 |
| [Wan2.2-I2V / T2V-A14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF) | Apache-2.0 |
| [stabilityai/sdxl-vae](https://huggingface.co/stabilityai/sdxl-vae) | MIT |
| [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | 記載なし（上流 Wan-AI は Apache-2.0） |
| [mellow_pencil-XL](https://huggingface.co/bluepen5805/mellow_pencil-XL) | [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/) |
| [Sierunami](https://civitai.com/models/1048343) | [Illustrious License](https://freedevproject.org/faipl-1.0-sd/)（FAIPL 1.0-SD） |
| [Flying Effect (Wan2.1 I2V LoRA)](https://civitai.com/models/1348626) | Civitai（`Image` `RentCivit` `Rent` `Sell`） |
| [Flow Camera](https://civitai.com/models/1903906) | Civitai（`Image` `RentCivit` `Rent` `Sell`） |
| Seedance 2.0（5-4 / ByteDance）| オープンライセンスではなく **API 提供者の利用規約**。下記参照 |

### 生成した画像について

**Fair AI Public License 1.0-SD は、生成物をライセンスの対象外としています。**

> The output of this software is not covered by this license,
> and no contributor claims any rights to it.

Sierunami・mellow_pencil-XL で作った画像は、**あなたのものです。**
販売・作品公開に制限はかかりません。

**Seedance 2.0（5-4）だけは性格が違います。** これは ComfyUI の API ノード経由で
ByteDance のサービスを呼び出すもので、オープンライセンスではありません。
[Comfy の利用規約](https://www.comfy.org/terms-of-service)は出力の権利を利用者が保持すると定め、
Partner Node は各提供者の規約に従うとしています。ByteDance 側も出力の知的財産権を主張しませんが、
**「生成できること」は「公開してよいこと」を意味しません。**
既存のキャラクター・実在人物に似た出力になっていないか、公開前にご自身で確認してください。
オリジナルキャラクターを使い、権利者の了解が取れているものであれば問題ありません。

### モデルを再配布するとき

**モデルファイル自体を配り直す場合は、条件が変わります。**

- **Sierunami** — 作者が「Do not reprint this model」と明記しています。
  マージや共有は可能ですが、**派生物の商用利用（生成サービス・受注モデル等）はできません**
- **FAIPL 1.0-SD はコピーレフト**です。派生物は同じ自由度を保つライセンスで公開する必要があります
- Civitai のモデルは `Sell` フラグがあるものだけ再配布できます

読者が自分の環境で使う分には、これらの制限は関係ありません。

## 謝辞

本書とこのリポジトリは、多くの方の仕事の上に成り立っています。

**ノートブック原作・動作検証**
ざすこ（[道草 雑草子](https://x.com/zasuko_michiksa)）— Colab 起動ノートブックの設計と、
全経路の実機確認をご担当いただきました。

**モデル・カスタムノードの作者のみなさま**
[Ocean3](https://civitai.com/user/Ocean3)（Sierunami）/
[Y_AI_N](https://civitai.com/models/1348626)（Flying Effect）/
[Nul_samx](https://civitai.com/models/1903906)（Flow Camera）/
[bluepen5805](https://huggingface.co/bluepen5805)（mellow_pencil-XL）/
[Kijai](https://github.com/kijai) / [Kosinkadink](https://github.com/Kosinkadink) /
[cubiq](https://github.com/cubiq) / [rgthree](https://github.com/rgthree) /
[Fannovel16](https://github.com/Fannovel16) / [Isi-dev](https://github.com/Isi-dev) /
[numz](https://github.com/numz) / [aria1th](https://github.com/aria1th) /
[GACLove](https://github.com/GACLove) / [princepainter](https://github.com/princepainter)

**上流プロジェクト**
[ComfyUI](https://github.com/comfyanonymous/ComfyUI)（comfyanonymous 氏と貢献者のみなさま）/
[Comfy-Org](https://huggingface.co/Comfy-Org) / [QuantStack](https://huggingface.co/QuantStack) /
[Wan-AI](https://huggingface.co/Wan-AI) / [Stability AI](https://huggingface.co/stabilityai) /
[Pinggy](https://pinggy.io/) / [Cloudflare](https://www.cloudflare.com/)

**QA レビュアーのみなさま**
発売前の原稿を読み、誤りと分かりにくさを指摘してくださった読者レビュアーのみなさまに感謝します。

**編集**
SBクリエイティブ 編集部

## Issues

不具合報告・ご質問は [Issues](../../issues) へお願いします。

## このリポジトリを更新する方へ

書籍の紙面は刊行後に修正できません。**紙面のQRコードが指す先を壊さない**ことを
最優先に、次の方針で運用しています。

### ファイルを移動・リネームするとき

書籍のQRコードは[短縮URL](#短縮url)を指しており、転送先の付け替えでリンクを維持できます。
**ただし付け替えを忘れると、読者は404に着地します。**

1. 移動前に、そのパスを指す短縮URLが無いか確認する
2. 移動後に短縮URLの転送先を付け替える
3. `curl -o /dev/null -w '%{http_code}' -L <短縮URL>` で疎通を確認する

ノートブックや README が参照しているファイル名も、あわせて更新してください。

### ノートブックを変更するとき

`ipynb/` 配下のノートブックは[短縮URL](#短縮url)の参照先で、読者がいつ開くか分かりません。
**検証していない変更を `main` に入れないでください。**
とくに書籍で使用する `ipynb/ComfyUI-pinggy.ipynb`（https://j.aicu.ai/SG26P ）は要注意です。

1. ブランチを切って push する
2. `https://colab.research.google.com/github/aicuai/Book-SG26/blob/<branch>/ipynb/<ノートブック名>`
   で実機テストする（ローカルでは Colab 環境を再現できません）
3. 動作確認後に `main` へマージする

### ノートブックから画像を取得するとき

**必ず `raw.githubusercontent.com` を使ってください。**
`github.com/.../blob/...` を指定すると、画像ではなく**HTMLページ**がその
ファイル名で保存されます（ダウンローダはURL末尾からファイル名を作るだけのため）。

```
blob版: HTTP 200 / text/html  ← HTMLページ
raw版 : HTTP 200 / image/png  ← 本物のPNG
```

Colab では相対パスも解決されないため、ノートブック内の画像は絶対URLにします。

### 動画を README に載せるとき

GitHub の README では **mp4 をインライン再生できません**（`<video>` タグは
サニタイザで除去されます）。再生ボタン付きのポスター画像を置き、クリックで
GitHub の動画プレイヤーへ遷移させてください。

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
