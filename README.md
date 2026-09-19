# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

**English** · [简体中文](readme/README.zh-CN.md) · [日本語](readme/README.ja.md) · [한국어](readme/README.ko.md) · [Español](readme/README.es.md) · [Français](readme/README.fr.md) · [Deutsch](readme/README.de.md) · [Português](readme/README.pt.md) · [Italiano](readme/README.it.md) · [Русский](readme/README.ru.md) · [Polski](readme/README.pl.md) · [Türkçe](readme/README.tr.md) · [Tiếng Việt](readme/README.vi.md) · [Bahasa Indonesia](readme/README.id.md) · [ไทย](readme/README.th.md) · [हिन्दी](readme/README.hi.md) · [العربية](readme/README.ar.md)

[Website](https://equalang.com) · [Pricing](https://equalang.com/pricing) · [Developer docs](https://equalang.com/developers) · [API keys](https://equalang.com/api-keys)

> **Keywords:** document translation, pdf translator, translate pdf keep layout, docx translation, pptx translation, excel translation, epub translation, subtitle translation, srt translator, image translation, video translation, audio transcription, speech to text, ai translator, agent skill, claude code skill, codex skill, translation api

**Translate the file, keep the layout.** An [Agent Skill](https://agentskills.io) for [Equalang](https://equalang.com) - an AI translator that works on whole files: a PDF comes back as a PDF, a deck as a deck, with tables, images and formulas where they were. It also translates subtitles and pictures, turns audio and video into translated subtitles or a transcript, and translates strings in bulk. Works in Claude Code, Codex, Cursor, CodeBuddy and every other agent that loads Agent Skills.

## Features

- **Format in, format out** - PDF, DOCX, PPTX, XLSX, EPUB, HTML and TXT come back in the same format, still editable, with tables, images, formulas and page layout in place
- **Subtitles and pictures** - SRT and VTT keep their timing, optionally with the source line above the translation; JPG, PNG, WebP and BMP come back with the text in the picture translated
- **Audio and video** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM and MKV become translated subtitles, or a transcript in the language spoken (SRT, VTT, TXT, JSON)
- **Text in bulk** - separate strings translated in order, or one long text (up to 100,000 characters) that Equalang cuts at sentences itself; 100+ languages for text, 12 for files
- **Whole files, no pasting** - up to 100 MB a file, from a path or a public URL; nothing to split into text boxes
- **Costs no tokens** - the file goes to Equalang and a path comes back; a 300-page PDF never enters the conversation
- **The price before the job** - `estimate` answers with the most a job can cost, for free; failed and cancelled jobs cost nothing; a recording is charged for the speech actually heard; credits never expire
- **Nothing to install** - one Python script, standard library only, Python 3.8+

## Get a key

Sign up at <https://equalang.com> and create a key at <https://equalang.com/api-keys>. New accounts start with free credits - enough to put a document through and see what comes back.

```bash
export EQUALANG_API_KEY=el_your_key
```

Or copy `.env.example` to `.env` in this directory - it is gitignored. The key is shown once; Equalang keeps only a hash of it.

## Install

The shortest way - paste this to your agent:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (manual)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Project-scoped instead? Clone into `.claude/skills/equalang` in the repository.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex also reads `.agents/skills/` inside a repository, to scope it to one project.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Project-scoped: clone into `.codebuddy/skills/equalang` at the project root.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro and others</b></summary>

This is a plain [Agent Skill](https://agentskills.io): a folder with a `SKILL.md` in it. Every client that implements the standard loads the same folder - only the directory it scans differs, and each documents its own. Clone the repository into that directory and the skill is installed.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Prefer an MCP server? [equalang-mcp](https://github.com/equalang/equalang-mcp) offers the same operations as tools, and works in Claude Desktop, Cursor, Windsurf, Cline and OpenCode as well.

## Commands

```bash
# What would it cost? Free, and nothing is started
python3 scripts/equalang.py estimate report.pdf

# Translate a file; the result lands beside the source
python3 scripts/equalang.py translate report.pdf --to zh-CN

# From a public URL (Equalang fetches it itself), into a folder
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# What a recording says, as timed text
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Separate strings, in order
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# One long text, cut at sentences by Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# A job left running, the balance, and the language codes
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Every command prints one JSON object - paths and credits, never file contents - or `{"error", "code", "retryable"}` with exit code 1. `--help` on any command lists its flags. [SKILL.md](SKILL.md) is what the agent reads.

## Three things worth knowing

**Languages.** Codes look like `en`, `zh-CN`, `ja`. No list is built into the skill: `languages` reads the codes and names from the live API (`--kind text` for the wider set `text` takes), so a language Equalang adds is available without an update. Leave the source language out to have it detected.

**Credits.** Work spends the account's credits, the same balance as the website. SKILL.md has the agent name the cost - from `estimate` - and get agreement before it starts a job.

**Jobs take minutes.** The command waits, pausing as long as the API's `Retry-After` asks. Interrupting it does not cancel the job - `status <job_id>` picks it back up and downloads the result.

## Questions people ask

**Does the translated PDF keep its layout?**
Yes - that is the point. Text is put back where it was, and tables, images and formulas stay in place; a DOCX, PPTX or XLSX stays editable.

**Is my document sent to the model?**
No. The script uploads the file to Equalang and prints a path. A 300-page paper costs no tokens.

**Can it translate the text inside a picture?**
Yes. Text in a JPG, PNG, WebP or BMP is recognised, translated and drawn back into the picture.

**What does a job cost?**
`estimate` says before anything starts, and it is free. Prices are at <https://equalang.com/pricing>.

## How it is built

The same three decisions as the [MCP server](https://github.com/equalang/equalang-mcp):

1. **A file never passes through the model** - commands take where a file is (a path, or a public URL that Equalang fetches itself) and print where the results were written.
2. **A job lives inside one command** - upload, wait, download. `status` picks up a job whose wait was interrupted.
3. **The API's answers are repeated, not guessed** - retry only what the API marks `retryable`; the cost is the API's `quote`; the language list is read from its OpenAPI document; one `Idempotency-Key` per created job, so a lost answer cannot become a second, charged job.

`python3 scripts/check_api.py` verifies, without a key, that every path and field the script uses - and every format SKILL.md promises - is still in the API's contract.

## Links

- [Equalang](https://equalang.com) · [Pricing](https://equalang.com/pricing) · [Developer docs](https://equalang.com/developers)
- API for agents: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - the same operations as an MCP server
- Questions: <support@equalang.com>

## License

[Apache-2.0](LICENSE) © Equalang
