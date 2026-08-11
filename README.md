# techtoc に記事を出す

このリポジトリは、techtoc に記事を出すときの**置き方の見本**です。

`main` に push すると、techtoc が `content/` の中を取り込んで
サイトを作り直します。**`content/` の外は取り込まれません**
（この README も取り込まれません）。

---

## ファイルの置き方

```
content/
  docs/v1/<lang>/....mdx     ドキュメント（版あり・階層あり）
  handson/<lang>/....mdx     ハンズオン（申し込みができる）
  blog/<lang>/....mdx        ブログ（日付順）
  pages/<lang>/....mdx       単独のページ（会社概要など）
```

**`<lang>` は `ja` か `en`。** 置いた言語のぶんだけ出ます。
片方だけでも構いません（訳が無いページは、その言語では出ません）。

### URL の決まり方

ファイルの場所が、そのまま URL になります。

```
content/docs/v1/ja/intro.mdx          →  /<会社>/ja/docs/intro
content/docs/v1/ja/guide/setup.mdx    →  /<会社>/ja/docs/guide/setup
content/handson/ja/raspi.mdx          →  /<会社>/ja/handson/raspi
content/blog/ja/2026-08-hello.mdx     →  /<会社>/ja/blog/2026-08-hello
```

**`docs` だけ `v1/` が要ります**（版を持てるようにしてあるため）。
他の 3 つは `<lang>/` から直に始めます。

### 階層の名前と並び順

`docs` はフォルダで階層を作れます。フォルダの表示名と並び順は
`_structure.json` で決めます。**言語に依らないので 1 回だけ書きます。**

```json
{
  "guide": { "position": 1, "label": { "ja": "使いかた", "en": "Guide" } },
  "reference": { "position": 2, "label": "Reference" }
}
```

`content/docs/v1/_structure.json` に置きます。**任意です**——
無ければフォルダ名がそのまま表示名になります。

---

## 記事の書き方

先頭に `---` で挟んだ **frontmatter** を置きます。ここが規約です。

### docs

```yaml
---
title: はじめに              # 必須
description: 概要と導入手順   # 任意（一覧と検索に出ます）
sidebar_position: 1          # 任意（小さいほど上）
draft: false                 # 任意（true にすると出ません）
---
```

### blog

```yaml
---
title: RADIUS の話
date: 2026-08-12             # 必須（新しい順に並びます）
author: 山田                  # 任意
tags: [radius, eap]          # 任意
draft: false                 # 任意
---
```

### handson（申し込みができる回）

```yaml
---
title: ラズパイを RADIUS で認証させる
description: 3 時間で動かします
event_date: 2026-11-14T13:00:00+09:00   # 必須
duration_minutes: 180                    # 必須
capacity: 12                             # 必須
venue: オンライン（Zoom）                 # 任意
instructor: 山田                          # 任意
requirements:                            # 任意（持ち物）
  - Raspberry Pi
  - microSD カード
price_yen: 8800                          # 任意（0 なら無料）
payment_url: https://example.com/pay     # 有料なら必須
---
```

**有料（`price_yen` が 1 以上）なのに `payment_url` が無い回は
取り込まれません。** 申し込めても払えない状態を作らないためです。

### pages

```yaml
---
title: 会社概要
description: 私たちについて   # 任意
---
```

---

## 本文の書き方

ふつうの Markdown が使えます。それに加えて 2 つ。

### 見出し

**`# 見出し` を本文の先頭に書かないでください。**
frontmatter の `title` が h1 になります。本文は `##` から始めます。

```markdown
---
title: はじめに
---

導入の文章。

## 概要        ← ここから
```

### 注記（callout）

```markdown
:::note
補足です。
:::

:::warning[気をつけること]
見出しを付けられます。
:::
```

使えるのは **6 種類だけ**です。

| | 使いどころ |
|---|---|
| `note` | 補足 |
| `tip` | こうするとよい |
| `info` | 参考 |
| `warning` | 気をつけること |
| `danger` | 壊れること |
| `caution` | `warning` と同じ扱い |

**これ以外の名前（`:::message` など）は、そのままの文字で出ます。**
色も枠も付きません。

### コード

```markdown
​```go
func main() {}
​```
```

言語を書くと色が付きます。

---

## 取り込まれないもの

- `content/` の外にあるもの（README・ソース・画像置き場など）
- `draft: true` の記事
- `.mdx` `.md` 以外のファイル

**`title` が無い記事があると、取り込み全体が止まります。**
その 1 本だけ飛ばす形にはなっていません——気づかないまま
出ていないより、止まって理由が出るほうがよい、という作りです。

**`_` か `.` で始まる名前のファイル・フォルダは読まれません。**
書きかけを置いておく場所として使えます（`_drafts/` など）。

---

## 反映されないときは

techtoc の「リポジトリ」の画面に、**最後の取り込みと失敗の理由**が
出ています。よくあるのは次の 2 つです。

**記事が 0 本と言われる** — `content/` の下に `.mdx` がありません。
`docs` なら `content/docs/v1/ja/` まで作れているか確かめてください。

**特定の記事だけ出ない** — `draft: true` になっているか、
ファイル名が `_` `.` で始まっているか、frontmatter の書式が
壊れています（`---` が 2 本あるか、インデントが揃っているか）。

**全部出ない** — どこか 1 本の frontmatter が壊れている可能性が
高いです。理由に**ファイル名が出る**ので、そこを直してください。

---

## この見本の中身

```
content/
  docs/v1/ja/intro.mdx      日本語のドキュメント
  docs/v1/ja/setup.mdx      2 本目（複数ファイルの確認用）
  docs/v1/en/intro.mdx      英語版
```
