# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · **Bahasa Indonesia** · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Situs web](https://equalang.com) · [Harga](https://equalang.com/pricing) · [Dokumentasi developer](https://equalang.com/developers) · [Kunci API](https://equalang.com/api-keys)

> **Kata kunci:** terjemahan dokumen, translate pdf, terjemahkan pdf tanpa merusak format, translate file word, translate docx, translate ppt, translate file excel, translate epub, translate subtitle, terjemahkan file srt, translate teks di gambar, translate video, transkripsi audio, ubah suara jadi teks, penerjemah ai, api terjemahan, agent skill, claude code skill, codex skill, translation api

**Terjemahkan filenya, pertahankan tata letaknya.** Sebuah [Agent Skill](https://agentskills.io) untuk [Equalang](https://equalang.com) - penerjemah AI yang bekerja pada file utuh: PDF kembali sebagai PDF, presentasi sebagai presentasi, dengan tabel, gambar, dan rumus tetap di tempatnya. Ia juga menerjemahkan subtitle dan gambar, mengubah audio dan video menjadi subtitle terjemahan atau transkrip, serta menerjemahkan string secara massal. Berjalan di Claude Code, Codex, Cursor, CodeBuddy, dan semua agen lain yang memuat Agent Skills.

## Fitur

- **Format masuk, format yang sama keluar** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, dan TXT kembali dalam format yang sama, tetap bisa diedit, dengan tabel, gambar, rumus, dan tata letak halaman tetap di tempatnya
- **Subtitle dan gambar** - SRT dan VTT mempertahankan timing-nya, dengan opsi baris asli di atas terjemahan; JPG, PNG, WebP, dan BMP kembali dengan teks di dalam gambar sudah diterjemahkan
- **Audio dan video** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM, dan MKV menjadi subtitle terjemahan, atau transkrip dalam bahasa yang diucapkan (SRT, VTT, TXT, JSON)
- **Teks secara massal** - string-string terpisah diterjemahkan sesuai urutan, atau satu teks panjang (hingga 100,000 karakter) yang dipotong sendiri oleh Equalang per kalimat; 100+ bahasa untuk teks, 12 untuk file
- **File utuh, tanpa salin-tempel** - hingga 100 MB per file, dari path atau URL publik; tidak ada yang perlu dipecah ke kotak teks
- **Tidak memakan token** - file dikirim ke Equalang dan yang kembali adalah path; PDF 300 halaman tidak pernah masuk ke percakapan
- **Harga sebelum job dimulai** - `estimate` menjawab dengan biaya maksimum sebuah job, gratis; job yang gagal atau dibatalkan tidak dikenai biaya; rekaman ditagih berdasarkan ucapan yang benar-benar terdengar; kredit tidak pernah kedaluwarsa
- **Tidak ada yang perlu diinstal** - satu skrip Python, hanya pustaka standar, Python 3.8+

## Dapatkan kunci

Daftar di <https://equalang.com> dan buat kunci di <https://equalang.com/api-keys>. Akun baru langsung mendapat kredit gratis - cukup untuk mencoba satu dokumen dan melihat hasilnya.

```bash
export EQUALANG_API_KEY=el_your_key
```

Atau salin `.env.example` menjadi `.env` di direktori ini - file itu sudah masuk gitignore. Kunci hanya ditampilkan sekali; Equalang hanya menyimpan hash-nya.

## Instalasi

Cara tersingkat - tempelkan ini ke agen Anda:

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

Hanya untuk satu proyek? Clone ke `.claude/skills/equalang` di dalam repositori.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex juga membaca `.agents/skills/` di dalam repositori, untuk membatasinya ke satu proyek.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Per proyek: clone ke `.codebuddy/skills/equalang` di root proyek.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro, dan lainnya</b></summary>

Ini adalah [Agent Skill](https://agentskills.io) biasa: sebuah folder berisi `SKILL.md`. Setiap klien yang menerapkan standar ini memuat folder yang sama - yang berbeda hanya direktori yang dipindainya, dan masing-masing mendokumentasikannya sendiri. Clone repositori ke direktori itu dan skill pun terpasang.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Lebih suka server MCP? [equalang-mcp](https://github.com/equalang/equalang-mcp) menawarkan operasi yang sama sebagai tool, dan juga berjalan di Claude Desktop, Cursor, Windsurf, Cline, dan OpenCode.

## Perintah

```bash
# Berapa biayanya? Gratis, dan belum ada yang dimulai
python3 scripts/equalang.py estimate report.pdf

# Terjemahkan file; hasil disimpan di samping file sumber
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Dari URL publik (Equalang mengambilnya sendiri), ke sebuah folder
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Apa yang diucapkan dalam rekaman, sebagai teks berpenanda waktu
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# String-string terpisah, sesuai urutan
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Satu teks panjang, dipotong per kalimat oleh Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Job yang masih berjalan, saldo, dan kode bahasa
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Setiap perintah mencetak satu objek JSON - path dan kredit, tidak pernah isi file - atau `{"error", "code", "retryable"}` dengan kode keluar 1. `--help` pada perintah mana pun menampilkan daftar flag-nya. [SKILL.md](../SKILL.md) adalah yang dibaca agen.

## Tiga hal yang perlu diketahui

**Bahasa.** Kode berbentuk seperti `en`, `zh-CN`, `ja`. Tidak ada daftar yang ditanam dalam skill: `languages` membaca kode dan nama dari API secara langsung (`--kind text` untuk kumpulan lebih luas yang diterima `text`), sehingga bahasa yang ditambahkan Equalang langsung tersedia tanpa pembaruan. Kosongkan bahasa sumber agar terdeteksi otomatis.

**Kredit.** Pekerjaan memakai kredit akun, saldo yang sama dengan di situs web. SKILL.md membuat agen menyebutkan biayanya - dari `estimate` - dan mendapat persetujuan sebelum memulai job.

**Job memakan waktu beberapa menit.** Perintah akan menunggu, berhenti sejenak selama yang diminta `Retry-After` dari API. Menghentikannya tidak membatalkan job - `status <job_id>` melanjutkannya dan mengunduh hasilnya.

## Pertanyaan yang sering diajukan

**Apakah PDF hasil terjemahan mempertahankan tata letaknya?**
Ya - justru itu intinya. Teks dikembalikan ke posisi semula, dan tabel, gambar, serta rumus tetap di tempatnya; DOCX, PPTX, atau XLSX tetap bisa diedit.

**Apakah dokumen saya dikirim ke model?**
Tidak. Skrip mengunggah file ke Equalang dan mencetak sebuah path. Makalah 300 halaman tidak memakan token sama sekali.

**Bisakah ia menerjemahkan teks di dalam gambar?**
Bisa. Teks dalam JPG, PNG, WebP, atau BMP dikenali, diterjemahkan, lalu digambar kembali ke dalam gambar.

**Berapa biaya sebuah job?**
`estimate` memberi tahu sebelum apa pun dimulai, dan itu gratis. Daftar harga ada di <https://equalang.com/pricing>.

## Cara pembuatannya

Tiga keputusan yang sama dengan [server MCP](https://github.com/equalang/equalang-mcp):

1. **File tidak pernah melewati model** - perintah menerima lokasi file (path, atau URL publik yang diambil sendiri oleh Equalang) dan mencetak lokasi hasil ditulis.
2. **Sebuah job hidup di dalam satu perintah** - unggah, tunggu, unduh. `status` melanjutkan job yang penantiannya terhenti.
3. **Jawaban API diteruskan, bukan ditebak** - coba ulang hanya yang ditandai `retryable` oleh API; biayanya adalah `quote` dari API; daftar bahasa dibaca dari dokumen OpenAPI-nya; satu `Idempotency-Key` per job yang dibuat, sehingga jawaban yang hilang tidak bisa menjadi job kedua yang ikut ditagih.

`python3 scripts/check_api.py` memverifikasi, tanpa kunci, bahwa setiap path dan field yang dipakai skrip - dan setiap format yang dijanjikan SKILL.md - masih ada dalam kontrak API.

## Tautan

- [Equalang](https://equalang.com) · [Harga](https://equalang.com/pricing) · [Dokumentasi developer](https://equalang.com/developers)
- API untuk agen: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - operasi yang sama sebagai server MCP
- Pertanyaan: <support@equalang.com>

## Lisensi

[Apache-2.0](../LICENSE) © Equalang
