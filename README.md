# Equalang skill

**English** · [简体中文](readme/README.zh-CN.md) · [日本語](readme/README.ja.md) · [한국어](readme/README.ko.md) · [Español](readme/README.es.md) · [Français](readme/README.fr.md) · [Deutsch](readme/README.de.md) · [Português](readme/README.pt.md) · [Italiano](readme/README.it.md) · [Русский](readme/README.ru.md) · [Polski](readme/README.pl.md) · [Türkçe](readme/README.tr.md) · [Tiếng Việt](readme/README.vi.md) · [Bahasa Indonesia](readme/README.id.md) · [ไทย](readme/README.th.md) · [हिन्दी](readme/README.hi.md) · [العربية](readme/README.ar.md)

An [Agent Skill](https://github.com/anthropics/skills) that gives Claude Code, Codex, Cursor and other agents [Equalang](https://equalang.com): translate whole files with their layout kept, transcribe recordings, translate strings in bulk.

- **Documents** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - come back in the same format.
- **Subtitles** (SRT, VTT) and **pictures** (JPG, PNG, WebP, BMP).
- **Audio and video** come back as translated subtitles, or as a transcript in the language spoken.

## Install

Paste this to your agent:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Or by hand - a skill is a folder:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # create one at https://equalang.com/api-keys
```

As a Claude Code plugin: `/plugin marketplace add equalang/equalang-skill`, then `/plugin install equalang@equalang`.

`python3` (3.8+) is all it needs; there is nothing to `pip install`.

## What the agent runs

```bash
python3 scripts/equalang.py estimate report.pdf                  # what would it cost? (free)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # result lands beside the source
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Languages.** Codes look like `en`, `zh-CN`, `ja`. No list is built into the skill: `languages` reads the codes and names from the live API (`--kind text` for the wider set `text` takes), so a language Equalang adds is available without an update.

**Credits.** Work spends the account's credits, the same balance as the website. SKILL.md has the agent name the cost - from `estimate` - and get agreement first.

Every command prints one JSON object - paths and credits, never file contents - or `{"error", "code", "retryable"}` with exit code 1. [SKILL.md](SKILL.md) is what the agent reads.

## How it is built

The same three decisions as the [MCP server](https://github.com/equalang/equalang-mcp), which offers the same operations as tools:

1. **A file never passes through the model** - commands take where a file is (a path, or a public URL that Equalang fetches itself) and print where the results were written.
2. **A job lives inside one command** - upload, wait (pausing as long as the API's `Retry-After` asks), download. Interrupting the wait does not cancel the job; `status` picks it up.
3. **The API's answers are repeated, not guessed** - retry only what the API marks `retryable`; the cost is the API's `quote`; the language list is read from its OpenAPI document; one `Idempotency-Key` per created job, so a lost answer cannot become a second, charged job.

`python3 scripts/check_api.py` verifies, without a key, that every path and field the script uses - and every format SKILL.md promises - is still in the API's contract. The API itself: <https://equalang.com/llms.txt>.

Apache-2.0.
