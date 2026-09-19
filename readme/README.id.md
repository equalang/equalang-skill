# Skill Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · **Bahasa Indonesia** · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Sebuah [Agent Skill](https://github.com/anthropics/skills) yang memberikan [Equalang](https://equalang.com) kepada Claude Code, Codex, Cursor, dan agen lainnya: menerjemahkan file utuh dengan tata letak tetap terjaga, mentranskripsikan rekaman, menerjemahkan string secara massal.

- **Dokumen** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - kembali dalam format yang sama.
- **Subtitle** (SRT, VTT) dan **gambar** (JPG, PNG, WebP, BMP).
- **Audio dan video** kembali sebagai subtitle terjemahan, atau sebagai transkrip dalam bahasa yang diucapkan.

## Instalasi

Tempelkan ini ke agen Anda:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Atau secara manual - skill hanyalah sebuah folder:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # buat di https://equalang.com/api-keys
```

Sebagai plugin Claude Code: `/plugin marketplace add equalang/equalang-skill`, lalu `/plugin install equalang@equalang`.

Yang dibutuhkan hanya `python3` (3.8+); tidak ada yang perlu di-`pip install`.

## Yang dijalankan agen

```bash
python3 scripts/equalang.py estimate report.pdf                  # berapa biayanya? (gratis)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # hasil disimpan di samping file sumber
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Bahasa.** Kode berbentuk seperti `en`, `zh-CN`, `ja`. Tidak ada daftar yang ditanam dalam skill: `languages` membaca kode dan nama dari API secara langsung (`--kind text` untuk kumpulan lebih luas yang diterima `text`), sehingga bahasa yang ditambahkan Equalang langsung tersedia tanpa pembaruan.

**Kredit.** Pekerjaan memakai kredit akun, saldo yang sama dengan di situs web. SKILL.md membuat agen menyebutkan biayanya - dari `estimate` - dan mendapat persetujuan terlebih dahulu.

Setiap perintah mencetak satu objek JSON - path dan kredit, tidak pernah isi file - atau `{"error", "code", "retryable"}` dengan kode keluar 1. [SKILL.md](../SKILL.md) adalah yang dibaca agen.

## Cara pembuatannya

Tiga keputusan yang sama dengan [server MCP](https://github.com/equalang/equalang-mcp), yang menawarkan operasi yang sama sebagai tool:

1. **File tidak pernah melewati model** - perintah menerima lokasi file (path, atau URL publik yang diambil sendiri oleh Equalang) dan mencetak lokasi hasil ditulis.
2. **Sebuah job hidup di dalam satu perintah** - unggah, tunggu (berhenti sejenak selama yang diminta `Retry-After` dari API), unduh. Menghentikan penantian tidak membatalkan job; `status` melanjutkannya.
3. **Jawaban API diteruskan, bukan ditebak** - coba ulang hanya yang ditandai `retryable` oleh API; biayanya adalah `quote` dari API; daftar bahasa dibaca dari dokumen OpenAPI-nya; satu `Idempotency-Key` per job yang dibuat, sehingga jawaban yang hilang tidak bisa menjadi job kedua yang ikut ditagih.

`python3 scripts/check_api.py` memverifikasi, tanpa kunci, bahwa setiap path dan field yang dipakai skrip - dan setiap format yang dijanjikan SKILL.md - masih ada dalam kontrak API. API-nya sendiri: <https://equalang.com/llms.txt>.

Apache-2.0.
