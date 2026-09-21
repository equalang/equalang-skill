# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[ウェブサイト](https://equalang.com) · [料金](https://equalang.com/pricing) · [開発者向けドキュメント](https://equalang.com/developers) · [API キー](https://equalang.com/api-keys)

> **キーワード:** ドキュメント翻訳, PDF 翻訳, PDF 翻訳 レイアウト保持, PDF 翻訳 レイアウトそのまま, Word 翻訳, パワーポイント 翻訳, エクセル 翻訳, EPUB 翻訳, 論文 翻訳, 字幕翻訳, SRT 翻訳, 画像翻訳, 動画翻訳, 音声 文字起こし, 動画 文字起こし, AI 翻訳, agent skill, claude code skill, codex skill, translation api

**ファイルを翻訳しても、レイアウトはそのまま。** [Equalang](https://equalang.com) の [Agent Skill](https://agentskills.io) です。Equalang はファイルを丸ごと扱う AI 翻訳ツールで、PDF は PDF のまま、スライドはスライドのまま、表・画像・数式も元の位置で返ってきます。字幕や画像の翻訳、音声・動画からの翻訳済み字幕や書き起こしの作成、短いテキストの一括翻訳にも対応。Claude Code、Codex、Cursor、CodeBuddy をはじめ、Agent Skills を読み込めるあらゆるエージェントで動きます。

## こんなふうに頼めます

- 「~/Documents/contract.pdf を日本語に翻訳して。レイアウトはそのままで」
- 「pitch-deck.pptx を英語と中国語に翻訳して」
- 「https://example.com/whitepaper.pdf を日本語に翻訳して ~/Downloads に保存して」
- 「thesis.docx を英語に翻訳すると、いくらかかる？」
- 「interview.mp4 に日本語字幕を付けて。各行の上に原文も残して」
- 「standup.m4a をタイムスタンプ付きで文字起こしして」
- 「menu.jpg の文字を日本語に翻訳して」
- 「locales/en.json の文言を韓国語・中国語・フランス語に翻訳して」

## 特長

- **ドキュメント** - PDF、DOCX、PPTX、XLSX、EPUB、HTML、TXT は同じ形式のまま、編集可能な状態で返ってきます。表、画像、数式、ページレイアウトも元の位置のままです
- **字幕と画像** - SRT と VTT はタイミングを保持し、訳文の上に原文を併記することもできます。JPG、PNG、WebP、BMP は画像内の文字が翻訳された状態で返ってきます
- **音声と動画** - MP3、M4A、WAV、FLAC、OGG、AAC、Opus、MP4、MOV、WebM、MKV を、翻訳済みの字幕、または話されている言語のままの書き起こし (SRT、VTT、TXT、JSON) にします
- **テキストの一括翻訳** - 短いテキストを順番どおりに翻訳。長いテキスト 1 件 (100,000 文字まで) も渡せ、その場合は Equalang が文の区切りで分割します
- **言語** - テキストは 100 以上、ファイルは 12 の言語に対応。ソース言語を省略すると自動検出されます

## キーを取得する

<https://equalang.com> で登録し、<https://equalang.com/api-keys> でキーを作成します。新規アカウントには無料クレジットが付いてきます。ドキュメントを 1 本試すには十分です。

キーは `~/.config/equalang/.env` に一度保存すれば、ずっと有効です。Claude Code、Codex、WorkBuddy、Cursor などどのエージェントでも、新しいセッションでも、再インストールや更新の後でも使え、export は不要です。Equalang MCP サーバーも同じファイルを読みます。

```bash
mkdir -p ~/.config/equalang
echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env
chmod 600 ~/.config/equalang/.env
```

環境変数 `EQUALANG_API_KEY` が設定されていれば、そちらが優先されます。特定のプロジェクトだけ別のキーを使うときに使います。

## インストール

`python3` 3.8 以降が必要で、ほかには何もいりません。スクリプトは標準ライブラリしか使いません。

いちばん手軽な方法は、これをエージェントに貼り付けることです:

> https://equalang.com/install/skill-install.md の手順に従って、Equalang のスキルをインストールしてください。

<details open>
<summary><b>Claude Code</b> (プラグイン)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (手動)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

プロジェクト単位で使いたい場合は、リポジトリ内の `.claude/skills/equalang` にクローンします。
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex はリポジトリ内の `.agents/skills/` も読み込むので、1 つのプロジェクトに限定することもできます。
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

プロジェクト単位の場合は、プロジェクトルートの `.codebuddy/skills/equalang` にクローンします。
</details>

<details>
<summary><b>Cursor、Gemini CLI、OpenCode、Copilot、Goose、Amp、Kiro など</b></summary>

これはごく普通の [Agent Skill](https://agentskills.io)、つまり `SKILL.md` が入ったフォルダーです。この標準を実装しているクライアントなら、どれも同じフォルダーを読み込みます。違うのはスキャンするディレクトリだけで、その場所は各クライアントのドキュメントに書かれています。そのディレクトリにリポジトリをクローンすれば、スキルのインストールは完了です。

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

MCP サーバーのほうがよければ、[equalang-mcp](https://github.com/equalang/equalang-mcp) が同じ操作をツールとして提供しています。Claude Desktop、Cursor、Windsurf、Cline、OpenCode でも使えます。

## コマンド

```bash
# いくらかかる? 無料で、翻訳は始まりません
python3 scripts/equalang.py estimate report.pdf

# ファイルを翻訳する。結果は元ファイルの隣に保存されます
python3 scripts/equalang.py translate report.pdf --to zh-CN

# 公開 URL から (Equalang が自分で取得)、フォルダーに保存
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# 録音で話されている内容を、タイムスタンプ付きテキストに
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# 短いテキストを、順番どおりに
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# 長いテキスト 1 件を、Equalang が文の区切りで分割
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# 実行中のままのジョブ、残高、言語コード
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

どのコマンドも JSON を出力します。ファイルをどこに書いたか、いくらかかったか、うまくいかなかったときは何が起きたかが分かります。どのコマンドでも `--help` を付けるとフラグの一覧が出ます。エージェントが読むのは [SKILL.md](../SKILL.md) です。

言語コードは `en`、`zh-CN`、`ja` のような形式です。`languages` を実行すると一覧が出て、`languages chinese` で検索できます。ジョブには数分かかります。コマンドは完了を待ち、途中で中断しても `status <job_id>` で再開できます。

## リンク

- [Equalang](https://equalang.com) · [料金](https://equalang.com/pricing) · [開発者向けドキュメント](https://equalang.com/developers)
- エージェント向け API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - 同じ操作を MCP サーバーとして提供
- お問い合わせ: <support@equalang.com>

## ライセンス

[Apache-2.0](../LICENSE) © Equalang
