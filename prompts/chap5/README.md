# 第5章　動画を生成してみよう　https://j.aicu.ai/SG26c5

[![サンプル動画を再生](../../images/chap5_r2v_poster.jpg)](Seedance2.0_R2V%E2%80%97Movie_720p_SAMPLE.mp4)

**▶️ [Seedance 2.0 (R2V)「リズメイの待ち合わせ」を再生する](Seedance2.0_R2V%E2%80%97Movie_720p_SAMPLE.mp4)**（15秒 / 音声あり）

渋谷のハチ公前で待ち合わせる響姫メイと渋谷リズを描いた15秒のCM風動画です。
このページ全体で、**この動画をゼロから作るまでのプロンプト15点**を公開しています。

書籍『【キャラクターを創り動かす】画像・動画生成AI スタートガイド』第5章で使用するプロンプトをまとめています。各セクションのコードブロックはそのままコピーして使えます。

> 💡 上の画像をクリックすると GitHub の動画プレイヤーで再生されます（音声つき）。
> 生成に使用したプロンプトは [5-4-5](#5-4-5) にあります。

## テキストファイル版もあります

このページのプロンプトは、[`5-2/`](5-2/) [`5-3/`](5-3/) [`5-4/`](5-4/) の各ディレクトリに
**テキストファイル（.txt）としても置いてあります。内容はこのページと同一です。**

用途に応じて使い分けてください。

| | 向いている使い方 |
|---|---|
| **このページ** | ブラウザで読む／必要な部分だけコピーする |
| **`.txt` ファイル** | 個別にダウンロードする／原文のまま扱う／`git clone` して手元で編集する |

> このページでは、原文の BOM・行頭の余分な空白を除去し、単語の途中で改行されていた箇所を
> つなげています（コピーしてそのまま使えるようにするため）。
> **完全な原文が必要な場合は `.txt` を参照してください。**

## 目次

| 節 | 内容 |
|---|---|
| **[5-2](#5-2)** | **Wan2.2 で画像から動画を作る（I2V）** |
| [5-2-1](#5-2-1) | I2V用プロンプトを ChatGPT に作らせる |
| [5-2-2](#5-2-2) | 渋谷リズ ― スマホを見ながら歩く |
| [5-2-3](#5-2-3) | 響姫メイ ― 歌う |
| [5-2-4](#5-2-4) | 品質向上のためのネガティブプロンプト |
| **[5-3](#5-3)** | **Wan2.2 で開始画像と終了画像から動画を作る（FLF2V）** |
| [5-3-1](#5-3-1) | カット動画用プロンプトを ChatGPT に作らせる |
| [5-3-2](#5-3-2) | ループ動画用プロンプトを ChatGPT に作らせる |
| [5-3-3](#5-3-3) | ロゴアニメーション用プロンプトを ChatGPT に作らせる |
| [5-3-4](#5-3-4) | 響姫メイが振り向く |
| [5-3-5](#5-3-5) | 響姫メイ（ちびキャラ）のダンスループ |
| [5-3-6](#5-3-6) | 響姫メイのロゴアニメーション |
| **[5-4](#5-4)** | **Seedance 2.0 でシナリオから動画を作る（R2V）** |
| [5-4-1](#5-4-1) | テーマとシナリオ案を考える |
| [5-4-2](#5-4-2) | シナリオを定型テンプレートにまとめる |
| [5-4-3](#5-4-3) | イメージボードを作る（i2i） |
| [5-4-4](#5-4-4) | Seedance 2.0 用プロンプトに変換する |
| [5-4-5](#5-4-5) | 「リズメイの待ち合わせ」完成プロンプト |

---

# 5-2

**Wan2.2 で画像から動画を作る（Image to Video）**

## 5-2-1

**I2V用プロンプトを ChatGPT に作らせる**

画像の内容と動かしたい要素を渡すと、Wan2.2 向けの英語プロンプトとネガティブプロンプトを組み立ててくれるメタプロンプトです。`#入力情報` の各項目を自分の画像に合わせて書き換えて使います。

```
#Prompt
あなたは Wan2.2 の Image-to-Video（I2V）用プロンプト作成アシスタントです。
私が渡す画像内容と要望をもとに、Wan2.2向けの英語プロンプトを作成してください。
#ルール
- 単語羅列ではなく、自然な短文で3～5文程度にまとめる
- 画像に写っているものを前提にし、「どう動くか」を中心に書く
- 主体の動き、カメラの動き、環境や光の変化、動きの強さを必ず入れる
- 画像にない要素は勝手に増やさない
- 顔崩れやチラつきを防ぐネガティブプロンプトも付ける
- 出力は以下の形式にする
#出力形式
【Prompt】
...
【Negative Prompt】
...
【解説】
...
#入力情報
画像の内容：スマホを眺めながら歩き続けている
動かしたい内容：オレンジのパーカーの女の子、髪の毛、服
カメラ：後ろに下がりながら女の子を追従する
環境変化：わずかな日差し、朝
雰囲気：穏やかな日常、にぎやかな街
NG事項：動かない、歩かない、背景が動かない
```

## 5-2-2

**渋谷リズ ― スマホを見ながら歩く**

[5-2-1](#5-2-1) のメタプロンプトから生成した、実際の I2V 用プロンプトです。

```
#Prompt
The girl in the orange hoodie keeps walking forward while looking at her smartphone, with a calm and natural expression. Her long pink ponytail and loose hair strands sway gently with each step, and the orange hoodie and drawstrings move softly in the morning breeze. The camera slowly moves backward while tracking her from the front, keeping her centered as the busy city street flows behind her. Subtle morning sunlight flickers across her face, clothes, and legs, creating a peaceful everyday atmosphere in a lively urban street.

#Negativeprompt
static image, no walking, frozen pose, motionless background, stiff body, face distortion, deformed eyes, flickering face, unstable facial features, extra limbs, extra fingers, bad hands, warped phone, changing outfit, changing hairstyle, inconsistent character, jitter, shaking camera, heavy blur, ghosting, duplicated body, unnatural leg movement, sliding feet, broken anatomy, background melting, sudden scene change, text, watermark, logo
```

## 5-2-3

**響姫メイ ― 歌う**

日本語の短いプロンプトでも I2V は動作します。

```
#Prompt
女の子が歌っている、自然な動きで滑らかな動作。
```

## 5-2-4

**品質向上のためのネガティブプロンプト**

どの I2V にも共通で追加できる、汎用の品質向上ネガティブプロンプトです。

```
#Negativeprompt
flickering, jittering, facedeformation, distorted anatomy, changing identity, blurry, low quality
```

---

# 5-3

**Wan2.2 で開始画像と終了画像から動画を作る（First / Last Frame to Video）**

## 5-3-1

**カット動画用プロンプトを ChatGPT に作らせる**

開始画像から終了画像へ自然につながるカット動画を作るためのメタプロンプトです。

```
#Prompt
あなたは Wan2.2のFirst/Last Frame to Video（FLF2V）用プロンプト作成アシスタントです。
私が渡す「開始画像」「終了画像」と要望をもとに、Wan2.2向けの英語プロンプトを作成してください。
#目的
- 開始画像から終了画像へ、同じキャラクター・同じ衣装・同じ世界観を保ったまま自然につながる動画を作ること
- 単なる切り替えではなく、中間の動きが想像できる、なめらかな遷移にすること
- 顔崩れ、別人化、衣装変化、背景破綻、急なジャンプカット感をできるだけ防ぐこと
#ルール
- 単語の羅列ではなく、自然な短文で3～5文程度にまとめる
- 「何が写っているか」より、「開始画像から終了画像へどう変化するか」を優先して書く
- 主体の動き、顔や視線の変化、髪や服の揺れ、カメラの動き、空気感や光の変化を入れる
- 開始画像と終了画像の間を埋めるような、無理のない自然な動きにする
- 画像にない要素は勝手に増やさない
- キャラクターの髪型、髪色、衣装、装飾、顔立ちを維持する
- 急激な変形、別人化、顔崩れ、チラつき、形状変化、背景破綻を防ぐネガティブプロンプトも付ける
#出力形式
【Prompt】
...
【Negative Prompt】
...
#入力情報
開始画像の内容：水色ツインテールの少女の後ろ姿。白いフリル衣装、黒リボン。
終了画像の内容：同じ少女の正面姿。やさしくにっこり笑っている。
やりたい変化：後ろ姿から勢いよく振り返り、ダブルピースサインをして微笑む。
主体の動き：体を勢いよく回転する。
顔・視線の変化：大きな笑顔、笑う時には目を閉じて元気に。
髪や服の動き：髪とリボンが大きく揺れる。
カメラ：ほぼ固定。少しだけ寄る。
雰囲気：清楚、可愛い、やさしい、幸せ。
NG事項：別人化、顔崩れ、髪型変化、衣装変化、背景追加、激しいカメラ移動。
```

## 5-3-2

**ループ動画用プロンプトを ChatGPT に作らせる**

同じ画像を開始フレームと終了フレームの両方に使い、繰り返し再生しても違和感のないループ動画を作るためのメタプロンプトです。

```
#Prompt
あなたはWan2.2の First/Last Frame to Video（FLF2V）用プロンプト作成アシスタントです。
同じ画像を開始フレームと終了フレームに使う、自然にループする動画用の英語プロンプトを作成してください。
#目的
- 同じ画像を開始と終了に使い、繰り返しても違和感の少ないループ動画を作ること
- キャラクターの見た目や衣装を保ったまま、動きはしっかり出すこと
- ダンスや回転などの見栄えする動きを入れつつ、顔崩れ、別人化、衣装破綻、不自然な変形を防ぐこと
- 最後は自然に開始フレームへ戻れる流れにすること
#ルール
- 単語の羅列ではなく、自然な短文で3～4文程度にまとめる
- 動きは弱くしすぎず、リズム感のある連続動作として書く
- ステップ、回転、腕の動き、体の上下動、髪やリボンや服の揺れを適切に入れる
- 動きはしっかり出すが、骨格、顔、髪型、衣装デザインが破綻しないようにする
- カメラは基本固定。必要ならごく弱い寄りや揺れだけにする
- 画像にない要素は増やさない
- 同じキャラクター、同じ衣装、同じ背景を維持する
- ネガティブプロンプトも付ける
#出力形式
【Prompt】
...
【Negative Prompt】
...
#入力情報
画像の内容：水色の長いツインテールに黒リボン、白いフリル衣装のちびキャラ少女。ピンクの大きな瞳。可愛く清楚な印象。背景は単色グリーン。
ループで入れたい動き：笑顔で元気よく、プロダンサーのようにリズムよく踊る。左右に軽くステップしながら腕を可愛く動かし、その場で軽やかにくるっと回転する。ツインテール、黒リボン、スカートのフリルが動きに合わせてふわっと大きめに揺れる。最後は自然に最初の正面ポーズへ戻る。
カメラ：基本固定。全身が見える安定した画角。
雰囲気：可愛い、元気、明るい、アイドル風、キレがある、楽しい、見栄えがよい、自然なループ。
NG事項：別人化、顔崩れ、目の破綻、髪型変化、ツインテールの本数や長さの破綻、衣装変化、背景色の変化、不自然な手足、激しすぎる変形、過剰なカメラ移動、ループ切れの違和感
```

## 5-3-3

**ロゴアニメーション用プロンプトを ChatGPT に作らせる**

シンプルなロゴから装飾された完成版ロゴへ変形する動画を作るためのメタプロンプトです。

```
#Prompt
あなたは Wan2.2 の First / Last Frame to Video（FLF2V）用プロンプト作成アシスタントです。
私が渡す「開始画像」「終了画像」と要望をもとに、ロゴ変形動画向けの英語プロンプトを作成してください。
#目的
- 開始画像のロゴから終了画像のロゴへ、自然で見栄えよく変形する動画を作ること
- ロゴ文字の可読性、デザインの一貫性、ブランド感を保ちながら変化させること
- 単なる切り替えではなく、完成形へ段階的に進化する流れにすること
#ルール
- 単語の羅列ではなく、自然な短文で3～5文程度にまとめる
- 「何があるか」より、「開始画像から終了画像へどう変化するか」を優先して書く
- ロゴ文字の可読性、構図、配色、デザインの統一感を維持する
- 追加される要素や装飾は、段階的に自然に現れる流れにする
- 変形は見栄えよく、動きはしっかり出しつつ、不自然な崩れや急な飛びを避ける
- カメラは基本固定とし、必要な場合のみごく弱い寄りや発光演出に留める
- 画像にない要素は勝手に増やしすぎない
- ネガティブプロンプトも付ける
#出力形式
【Prompt】
...
【Negative Prompt】
...
#入力情報
開始画像の内容：シンプルな「響姫メイ」ロゴ
終了画像の内容：王冠・宝石・バナー・英字・レース付きの豪華版ロゴ
やりたい変化：文字を保ったまま豪華な完成形へ進化
変形の流れ：きらめき → 上部装飾 → 左右装飾 → 下部バナー → 完成
カメラ：固定
雰囲気：可愛い、華やか、アイドル風、きらきら
NG事項：文字崩れ、色変化、構図崩れ、不自然な変形
```

## 5-3-4

**響姫メイが振り向く**

後ろ姿の開始画像から、振り向いてダブルピースする終了画像へつなぐカット動画のプロンプトです。

```
#Prompt
A young girl with long light-blue twin-tails is seen from behind, then she quickly spins around to face the camera with a lively, energetic turn. As she rotates, her twin-tails, black ribbons, and frilled white dress sway widely and naturally with the motion. She lands in a front-facing pose, closes her eyes, shows a big cheerful smile, and raises both hands in a bright double peace sign, keeping the same hairstyle, outfit, and gentle character identity. The camera stays almost fixed with only a slight push-in, and the soft clean lighting creates a pure, cute, warm, and happy feeling.

#Negativeprompt
identity change, different person, face distortion, inconsistent face, unstable eyes, hairstyle change, twin-tail shape change, outfit change, extra accessories, added background elements, background distortion, flicker, frame inconsistency, jitter, ghosting, warped body, bad anatomy, aggressive camera movement, strong zoom, camera shake, blur
```

## 5-3-5

**響姫メイ（ちびキャラ）のダンスループ**

同じ画像を開始・終了フレームに使う、シームレスに繰り返せるダンスループのプロンプトです。

```
#Prompt
A cute chibi girl with pink hair and yellow highlights in a side upswept ponytail performs a joyful and energetic seamless dance loop, bouncing much more playfully with bigger hops, cheerful springy jumps, and lively side-to-side steps while keeping her full-body front view, original outfit, and solid green background unchanged. She dances with a fun rhythm, swinging her arms wide, lifting her knees a little higher, and repeating upbeat turns, quick twirls, and buoyant hops that feel lively and adorable without becoming extreme. Her ponytail, loose hair strands, hoodie, and shorts bounce and sway clearly with each movement, making the motion feel full of life while preserving her face, hairstyle, proportions, and clothing design. The camera stays fixed, and the dance ends by smoothly settling back into her original centered pose so the loop repeats naturally.

#Negativeprompt
background color change, camera movement, zoom, cut, scene transition, new objects, extra limbs, extra fingers, missing limbs, face distortion, different person, anatomy error, twisted neck, unnatural head direction, unnatural body orientation, broken pose, extreme split, exaggerated leg spread, clothing change, hairstyle change, unstable expression, flicker, jitter, warped body, deformed hands, inconsistent proportions, off-center framing
```

## 5-3-6

**響姫メイのロゴアニメーション**

シンプルなロゴが段階的に豪華版へ変形するプロンプトです。

```
#Prompt
A clean and simple "響姫メイ" logo gradually evolves into its ornate final version while keeping the text fully readable, centered, and consistent in color, outline, and overall composition. Soft sparkling highlights appear first around the letters, then the upper decoration forms naturally above the logo, with the crown and gemstone assembling in place as if growing from the existing design. Next, the side ornaments emerge smoothly on the left and right, followed by the lower black ribbon banner, the "Hibiki Mei" text, and the lace details unfolding beneath in a graceful, step-by-step progression. The camera stays fixed, with only a very subtle glow and shimmer effect, creating a cute, glamorous, idol-like transformation that feels polished, magical, and visually coherent.

#Negativeprompt
text distortion, unreadable letters, broken typography, wrong characters, color shift, composition drift, off-center logo, warped shapes, inconsistent outline thickness, sudden popping, hard cuts, jitter, flicker, deformed crown, deformed ribbon, malformed ornaments, excessive added elements, messy decoration, low detail, blur, duplicated parts, unstable layout, unnatural morphing
```

---

# 5-4

**Seedance 2.0 でシナリオから動画を作る（Reference to Video）**

5-4 は「テーマとシナリオを考える → 定型にまとめる → イメージボードを作る → R2V プロンプトに変換する → 生成する」という流れで進めます。以下のセクションはその順番に並んでいます。

## 5-4-1

**テーマとシナリオ案を考える**

キャラクター設定と動画コンセプトから、15秒動画のテーマ案とシナリオ案を出させるプロンプトです。

```
#Prompt
以下のオリジナルキャラクター設定と動画コンセプトをもとに、15秒の短い動画向けのテーマ案とシナリオ案を考えてください。
【動画の目的】
・オリジナルキャラ2人の世界観の紹介用
・2人のオリジナルキャラ「響姫 メイ」と「渋谷 リズ」のハッピーな日常を垣間見せる
・キャラクターに対する感情の入り口を作る、興味を持たせる
【動画の尺】
・15秒
・CM風のサクッと気軽に見られる長さ
【主人公の見せ方】
・表情や衣装の印象を見せたい
・メイはちょっと繊細で内向的
・リズは元気で底抜けに明るい性格
・2人は仲の良い友人関係
【最後に残したい印象】
・ワクワクする日常
・2人の日常をもっと見たいと思わせたい
上記の条件をもとに、次の内容を考えてください。
【テーマとシナリオ案】
・この動画に合うテーマ案を3つ
・それぞれのテーマの短い説明
・15秒動画として成立する台詞付きのシナリオ案
・冒頭、中盤、締めの流れが分かる形で整理
・最後に、いちばんキャラの魅力が伝わりやすい案を1つおすすめしてください
以上、難しい言葉は使わず、分かりやすく整理して提案してください。
```

## 5-4-2

**シナリオを定型テンプレートにまとめる**

[5-4-1](#5-4-1) で選んだ案を、以降の工程で使い回せる定型フォーマットに整えさせるプロンプトです。

```
#Prompt
ではこの「渋谷待ち合わせ編」のシナリオ案を、以下のテンプレートにあてはめて、シナリオ案としてまとめて下さい。
シナリオ案まとめのテンプレート
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
タイトル：「＿＿＿＿＿」
テーマ：「▲▲は■■■」
あらすじ：
（100～120文字程度で記述）
15秒シナリオ案：
【冒頭】●～●秒
（20～50文字程度で状況を説明）
＊＊＊「～～…、～～～～。」
【中盤】●～●秒
（20～50文字程度で状況を説明）
＊＊＊「～～～～！」
【転換】●～●秒
（20～50文字程度で状況を説明）
＊＊＊「～～～、～～～～～！」
＊＊「～～～～。」
【締め】●～●秒
（20～50文字程度で状況を説明）
＊＊＊「～～～、～～」
＊＊「～～～！！」
```

## 5-4-3

**イメージボードを作る（i2i）**

シナリオから、3×3の9コマ構成のイメージボードを生成させるプロンプトです。各コマに「全景」「寄り」「見せ場」などの役割を割り当てて、動画全体の流れにメリハリを付けます。

```
#Prompt
添付のオリジナルキャラクター設定と背景、シナリオ案を基に、15秒のショート動画向けのイメージボードを作成して下さい。
イメージボード画像は16:9の横長画面で、16:9の縦横比のコマを3×3の9コマで並べる形とし、解像度は2Kで出力して下さい。
なお、イメージボードのそれぞれのコマには、適切な場面で、以下のような役割を持たせて動画全体の流れにメリハリが出るように描いてください。
・全景（世界観を説明）
・中景（状況と被写体の関係を説明）
・寄り（感情を描く）
・横顔（間や空気感を演出）
・アクションとリアクション
・見せ場の直前
・見せ場
・余韻（見せ場の受け）
・締め
#描画スタイル
背景のみフォトリアルな描写にして、登場キャラのみセルシェーディングで描き、光と陰の描写が現実世界と完全に調和しているように描いてください。
#シナリオ案
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
タイトル：「リズメイの待ち合わせ」
テーマ：「人混みの中でも、リズはメイを見つけてくれる」
＜あらすじ＞
渋谷駅前のにぎやかな空気の中で、待ち合わせのハチ公前にリズの姿はなく、少し不安そうに待つメイ。
そこへリズが元気よく遅れて現れて、メイの日常が一気に明るくなり、2人は仲良く街へお買い物へ。という短いCM風シナリオ
【冒頭】0～４秒
渋谷駅前。人混みとスクランブル交差点の雰囲気。メイがスマホを持って、少し困った顔で周囲を見回している。
メイ：「あれ……リズ、来ないな……」
【中盤】４～６秒
オレンジのパーカー姿のリズが、メイを探して渋谷の人混みの中を走っている。
リズ：「ハァ、ハァ…」
【転換】６～1０秒
メイが気づいて、ぱっと表情が明るくなる。少し照れながら小さく手を振り返す。
リズ：「お～～い！メイ～～！」
メイ：「…っ！」（気が付く）
【締め】1０～15秒
リズがメイの手を取って、2人は合流。メイはホッとしつつもとても嬉しそうに笑う。渋谷の街へ歩き出す。
メイ：「ハチ公前って言ったじゃ～ん」
リズ：「ゴメン ゴメ～ン！」
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
```

## 5-4-4

**Seedance 2.0 用プロンプトに変換する**

キャラクター設定・イメージボード・シナリオを、Seedance 2.0 の R2V 用フォーマットへ変換させるプロンプトです。`#Seedance2.0 R2V用のテンプレート` の部分が、参照画像とカット割りの書き方の型になります。

```
#Prompt
添付の、オリジナルキャラクター設定、イメージボード、シナリオ案を基に、以下のテンプレートに後述のシナリオ案をあてはめる形で、Seedance2.0 のR2V用の動画生成用プロンプトを書いてください。
なお、日本語以外のプロンプトは全て英文で記載して下さい。文字数は2,500～3,000文字程度を上限とします。
動画の長さは15秒を想定します。
#Seedance2.0 R2V用のテンプレート
～～～～～～～～～～～～～～～～～～～～～
※参照ファイルに応じて記載
Use
@Image1 for the [人物名] ,
@Image2 for the [人物名] ,
@Image3 for the [環境や状況] ,
@Image4 for the [敵や脅威],
@Video1 for the [参照させたい要素],
@Audio1 for the [参照させたい要素],
[描写スタイル］
※A short anime、 photorealistic film などを記載
＜動画のシナリオ＞
[Cut 1, ＊-＊ seconds:]
（カット内容の説明を英文でここに記載）
※以下、登場人物の台詞があれば記載
Japanese dialogue:
[人物名]：「（ここにセリフを記載）」
[Cut 2, ＊-＊ seconds:]
（カット内容の説明を英文でここに記載）
※以下、登場人物の台詞があれば記載
Japanese dialogue:
[人物名]：「（ここにセリフを記載）」
[Cut 3, ＊-＊ seconds:]
（カット内容の説明を英文でここに記載）
※以下、登場人物の台詞があれば記載
Japanese dialogue:
[人物名]：「（ここにセリフを記載）」
・
・
・
Additional notes and restrictions
※必要があれば記載する
[表現の補足]
[避けたい表現]
#描画スタイル
背景のみフォトリアルな描写にして、登場キャラのみセルシェーディングで描き、光と陰の描写が現実世界と完全に調和しているように描いてください。
#シナリオ案
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
タイトル：「リズメイの待ち合わせ」
テーマ：「人混みの中でも、リズはメイを見つけてくれる」
＜あらすじ＞
渋谷駅前のにぎやかな空気の中で、待ち合わせのハチ公前にリズの姿はなく、少し不安そうに待つメイ。
そこへリズが元気よく遅れて現れて、メイの日常が一気に明るくなり、2人は仲良く街へお買い物へ。という短いCM風シナリオ
【冒頭】0～４秒
渋谷駅前。人混みとスクランブル交差点の雰囲気。メイがスマホを持って、少し困った顔で周囲を見回している。
メイ：「あれ……リズ、来ないな……」
【中盤】４～６秒
オレンジのパーカー姿のリズが、メイを探して渋谷の人混みの中を走っている。
リズ：「ハァ、ハァ…」
【転換】６～1０秒
メイが気づいて、ぱっと表情が明るくなる。少し照れながら小さく手を振り返す。
リズ：「お～～い！メイ～～！」
メイ：「…っ！」（気が付く）
【締め】1０～15秒
リズがメイの手を取って、2人は合流。メイはホッとしつつもとても嬉しそうに笑う。渋谷の街へ歩き出す。
メイ：「ハチ公前って言ったじゃ～ん」
リズ：「ゴメン ゴメ～ン！」
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
```

## 5-4-5

**「リズメイの待ち合わせ」完成プロンプト（R2V）**

上記の工程を経て完成した、冒頭のサンプル動画の生成に実際に使用した Seedance 2.0 R2V プロンプトです。`@Image1` に響姫メイ、`@Image2` に渋谷リズ、`@Image3` にイメージボードを指定します。

```
#Prompt
Use
@Image1 for Hibiki Mei,
@Image2 for Shibuya Rhyth,
@Image3 for the storyboard, shot flow, framing, and mood.
A short anime with photorealistic Shibuya background integration.
Only the background, crowd, and city should be photorealistic.
Only Mei and Rhyth should be clean cel-shaded anime characters.
Match their lighting and shadows to sunny midday Shibuya, around 6500K.
The tone is a cheerful 15-second character introduction CM, showing Mei's shy sensitivity and Rhyth's bright energy.

<Video Scenario>
[Cut 1, 0-4 seconds:]
Bright daytime Shibuya near the Hachiko meeting area.
Show the busy plaza and scramble crossing atmosphere, then focus on Hibiki Mei waiting alone with her smartphone.
Keep her white frilled dress, black ribbons, long pale aqua twin-tails with soft pink accents, and pink eyes consistent with @Image1.
She looks slightly worried and searches the crowd.
Japanese dialogue:
Hibiki Mei: 「あれ……リズ、来ないな……」

[Cut 2, 4-6 seconds:]
Shibuya Rhyth hurries through the crowd, searching for Mei.
Keep her orange hoodie, sporty shorts, sneakers, tan skin, blue eyes, and pink-blonde side ponytail consistent with @Image2.
She is a little out of breath but still cheerful. Use a dynamic tracking shot to show speed.
Japanese dialogue:
Shibuya Rhyth: 「ハァ、ハァ…」

[Cut 3, 6-10 seconds:]
Rhyth spots Mei and waves high from the crowd. Cut to Mei noticing her.
Mei's face changes from worry to relief and joy, and she gives a small shy wave back.
This is the emotional turning point. Use a close-up for Mei's reaction and a matching shot connecting both girls.
Japanese dialogue:
Shibuya Rhyth: 「お～～い！メイ～～！」
Hibiki Mei: 「…っ！」

[Cut 4, 10-15 seconds:]
Rhyth reaches Mei and naturally takes her hand. Mei smiles with relief, still shy but clearly happy.
They walk together into Shibuya as if going shopping. End with a rear or three-quarter shot of both girls walking side by side, making the day feel like it is just beginning.
Japanese dialogue:
Hibiki Mei: 「ハチコウ前って言ったじゃ～ん」
Shibuya Rhyth: 「ゴメン ゴメ～ン！」

Additional notes and restrictions
- Total duration: about 15 seconds.
- Keep the location recognizable as Shibuya and the Hachiko meeting area.
- Preserve both character designs strictly.
- Mei must stay elegant, shy, soft, and reserved.
- Rhyth must stay lively, bright, friendly, and expressive.
- Use varied framing: establishing shot, medium shot, close-up, reaction shot, reunion shot, final walking-away shot.
- Keep Japanese lip sync natural.
- Avoid fantasy effects, magical particles, sci-fi elements, subtitles, text overlays, watermark, UI, manga symbols, chibi style, heavy camera shake, dark mood, or romance-heavy presentation.
- End with a bright everyday-adventure feeling.
```
