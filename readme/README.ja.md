# Equalang スキル

[English](../README.md) · [简体中文](README.zh-CN.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Claude Code、Codex、Cursor などのエージェントで [Equalang](https://equalang.com) を使えるようにする [Agent Skill](https://github.com/anthropics/skills) です。レイアウトを保ったままファイルを丸ごと翻訳し、録音を文字に起こし、文字列を一括翻訳します。

- **ドキュメント** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - 同じ形式のまま返ってきます。
- **字幕** (SRT, VTT) と **画像** (JPG, PNG, WebP, BMP)。
- **音声と動画** は、翻訳済みの字幕、または話されている言語のままの書き起こしとして返ってきます。

## インストール

これをエージェントに貼り付けます:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

または手動で - スキルはただのフォルダーです:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # https://equalang.com/api-keys で作成
```

Claude Code プラグインとして: `/plugin marketplace add equalang/equalang-skill` の後に `/plugin install equalang@equalang`。

必要なのは `python3` (3.8+) だけで、`pip install` するものはありません。

## エージェントが実行するコマンド

```bash
python3 scripts/equalang.py estimate report.pdf                  # 費用はいくら? (無料)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # 結果は元ファイルの隣に保存
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**言語。** コードは `en`、`zh-CN`、`ja` のような形式です。スキルに言語リストは組み込まれていません。`languages` が稼働中の API からコードと名称を読み取る (`text` が受け付ける、より広い一覧は `--kind text`) ため、Equalang が追加した言語はアップデートなしで使えます。

**クレジット。** 処理はアカウントのクレジット、つまりウェブサイトと同じ残高を消費します。SKILL.md は、エージェントが先に費用 - `estimate` で得たもの - を伝え、同意を得るよう定めています。

どのコマンドも JSON オブジェクトを 1 つ出力します - パスとクレジットだけで、ファイルの中身は含みません - 失敗時は `{"error", "code", "retryable"}` を終了コード 1 で出力します。エージェントが読むのは [SKILL.md](../SKILL.md) です。

## 設計

同じ操作をツールとして提供する [MCP サーバー](https://github.com/equalang/equalang-mcp) と同じ 3 つの判断です:

1. **ファイルはモデルを通らない** - コマンドはファイルの場所 (パス、または Equalang が自分で取得する公開 URL) を受け取り、結果を書き出した場所を出力します。
2. **ジョブは 1 つのコマンドの中で完結する** - アップロード、待機 (API の `Retry-After` が求める時間だけ休む)、ダウンロード。待機を中断してもジョブはキャンセルされず、`status` で再開できます。
3. **API の答えは推測せず、そのまま伝える** - 再試行するのは API が `retryable` とした場合のみ。費用は API の `quote`。言語リストは API の OpenAPI ドキュメントから読み取る。作成するジョブごとに `Idempotency-Key` を 1 つ使うため、応答が失われても、課金される 2 つ目のジョブにはなりません。

`python3 scripts/check_api.py` は、スクリプトが使うすべてのパスとフィールド - そして SKILL.md が約束するすべての形式 - が API のコントラクトに今も存在することを、キーなしで検証します。API 本体: <https://equalang.com/llms.txt>。

Apache-2.0.
