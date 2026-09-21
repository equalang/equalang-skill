---
name: equalang
description: Translate whole files with Equalang, keeping their layout - documents (PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT), subtitles (SRT, VTT), pictures, and audio or video (which come back as translated subtitles) - and transcribe recordings into timed text. Use when the user points at a FILE or a URL of one and wants it translated or transcribed, or wants strings translated in bulk; not for a sentence you can translate yourself.
license: Apache-2.0
---

# Equalang

Point it at a file and it uploads the file, waits for the job, and writes the results beside the source. You get paths back, **never the file's contents** - layout, tables, images and formulas survive, and nothing large enters the conversation.

**Work spends the user's credits. Say what it will cost and get their agreement before `translate` or `transcribe`.** `estimate` gives the number for a file, for free.

## Setup

```bash
export EQUALANG_API_KEY=el_...   # the user creates one at https://equalang.com/api-keys
```

Or put it in this skill's `.env`. Without a key every command answers with how to get one. **Never invent a key - ask the user.**

## Commands

Run from this skill's directory; `python3` and nothing else is needed. Every command prints one JSON object; `--help` lists a command's flags.

```bash
# What would it cost? Uploads without starting anything; free. `kept_until` says how long the upload is held.
python3 scripts/equalang.py estimate report.pdf
#   -> {"file_id": "...", "credits_to_translate": 12.34, "credits_to_transcribe": null, ...}

# Translate a file. A path, a public URL (Equalang fetches it), or --file-id from estimate.
python3 scripts/equalang.py translate report.pdf --to zh-CN
python3 scripts/equalang.py translate --file-id <file_id> --to zh-CN        # no second upload
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# A recording: translated subtitles, or what was said in the language spoken.
python3 scripts/equalang.py translate talk.mp4 --to en --bilingual --format srt --format txt
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Strings in bulk (each translated on its own; at most 50 of 5,000 characters, 20,000 per call).
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
# One long plain text - an article, notes, a .md - up to 100,000 characters. Equalang cuts it at sentences: never split it yourself.
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Look a job up again · stop one · the balance · language codes (no key needed)
python3 scripts/equalang.py status <job_id> -o ./out
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

## Reading the output

A finished job prints `outputs` (each with its `path`) and `credits_charged`. Tell the user both. **Do not read a produced file back to summarise it** unless asked: it is a whole document, and the point of a path is that its contents stay out of the conversation.

A failure prints `{"error", "code", "retryable"}` and exits 1. Retry only when `retryable` is true; `INSUFFICIENT_CREDITS` means the user tops up at https://equalang.com/pricing, not that you try again.

## Worth knowing

- **Formats.** Documents: pdf, docx, pptx, xlsx, epub, html, txt. Subtitles: srt, vtt. Pictures: jpg, png, webp, bmp. Recordings: mp3, m4a, wav, flac, ogg, aac, opus, mp4, mov, webm, mkv. Up to 100 MB. `transcribe` takes recordings only.
- **Results never overwrite.** They land beside a local source (or in `-o DIR`, or the current directory for a URL) under the name Equalang gives them; a taken name gets ` (1)`. Asking `status` again about a finished job names the files it already wrote rather than copying them.
- **Minutes, not seconds, for long files.** The command waits and prints progress to stderr. Interrupting it does **not** cancel the job: `status <job_id>` picks it up, `cancel <job_id>` stops it. A cancelled or failed job is not charged.
- **A recording is charged for the speech actually heard** - silence and music are not - so it usually costs less than `estimate` said; a document costs what `estimate` said.
- **Language codes** look like `en`, `zh-CN`, `zh-TW`, `ja`, `pt`. They are read from the live API, never from memory: `languages` lists the ones files take, `languages --kind text` the wider set `text` takes, and `languages chinese` finds one by name. Omit `--source-language` to have it detected.
- **Several files?** Estimate each, add the numbers up, and ask once - never loop over a folder on your own say-so.
- The API behind this, for anything the script does not do: https://equalang.com/llms.txt
