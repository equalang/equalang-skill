# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · **Bahasa Indonesia** · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Situs web](https://equalang.com) · [Harga](https://equalang.com/pricing) · [Dokumentasi developer](https://equalang.com/developers) · [Kunci API](https://equalang.com/api-keys)

> **Kata kunci:** terjemahan dokumen, translate pdf, terjemahkan pdf tanpa merusak format, translate file word, translate docx, translate ppt, translate file excel, translate epub, translate subtitle, terjemahkan file srt, translate teks di gambar, translate video, transkripsi audio, ubah suara jadi teks, penerjemah ai, api terjemahan, agent skill, claude code skill, codex skill, translation api

**Terjemahkan filenya, pertahankan tata letaknya.** Sebuah [Agent Skill](https://agentskills.io) untuk [Equalang](https://equalang.com) - penerjemah AI yang bekerja pada file utuh: PDF kembali sebagai PDF, presentasi sebagai presentasi, dengan tabel, gambar, dan rumus tetap di tempatnya. Ia juga menerjemahkan subtitle dan gambar, mengubah audio dan video menjadi subtitle terjemahan atau transkrip, serta menerjemahkan teks-teks pendek secara massal. Berjalan di Claude Code, Codex, Cursor, CodeBuddy, dan semua agen lain yang memuat Agent Skills.

## Fitur

- **Dokumen** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, dan TXT kembali dalam format yang sama, tetap bisa diedit, dengan tabel, gambar, rumus, dan tata letak halaman tetap di tempatnya
- **Subtitle dan gambar** - SRT dan VTT mempertahankan timing-nya, dengan opsi baris asli di atas terjemahan; JPG, PNG, WebP, dan BMP kembali dengan teks di dalam gambar sudah diterjemahkan
- **Audio dan video** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM, dan MKV menjadi subtitle terjemahan, atau transkrip dalam bahasa yang diucapkan (SRT, VTT, TXT, JSON)
- **Teks secara massal** - teks-teks pendek diterjemahkan sesuai urutan, atau satu teks panjang (hingga 100,000 karakter) yang dipotong sendiri oleh Equalang per kalimat
- **Bahasa** - 100+ untuk teks dan 12 untuk file, dengan bahasa sumber terdeteksi otomatis saat Anda mengosongkannya

## Dapatkan kunci

Daftar di <https://equalang.com> dan buat kunci di <https://equalang.com/api-keys>. Akun baru langsung mendapat kredit gratis, cukup untuk mencoba satu dokumen.

Simpan di `~/.config/equalang/.env`, cukup sekali per mesin: skill ini dan server MCP Equalang sama-sama membacanya dari sana, dan file itu tetap ada saat salah satunya dipasang ulang atau diperbarui.

```bash
mkdir -p ~/.config/equalang
echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env
chmod 600 ~/.config/equalang/.env
```

`EQUALANG_API_KEY` yang diatur di environment lebih diutamakan - gunakan untuk kunci lain di satu proyek tertentu.

## Instalasi

Membutuhkan `python3` 3.8 atau lebih baru, dan tidak ada lagi selain itu: skrip ini hanya memakai pustaka standar.

Cara tersingkat - tempelkan ini ke agen Anda:

> Instal skill Equalang dengan mengikuti petunjuk di https://equalang.com/install/skill-install.md

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
# Berapa biayanya? Gratis, dan belum ada yang diterjemahkan
python3 scripts/equalang.py estimate report.pdf

# Terjemahkan file; hasil disimpan di samping file sumber
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Dari URL publik (Equalang mengambilnya sendiri), ke sebuah folder
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Apa yang diucapkan dalam rekaman, sebagai teks berpenanda waktu
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Teks-teks pendek, sesuai urutan
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Satu teks panjang, dipotong per kalimat oleh Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Job yang masih berjalan, saldo, dan kode bahasa
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Setiap perintah mencetak JSON: di mana file ditulis dan berapa biayanya, atau apa yang tidak beres. `--help` pada perintah mana pun menampilkan daftar flag-nya. [SKILL.md](../SKILL.md) adalah yang dibaca agen itu sendiri.

Kode bahasa berbentuk seperti `en`, `zh-CN`, `ja`. Jalankan `languages` untuk melihat semuanya, atau `languages chinese` untuk mencari. Job memakan waktu beberapa menit - perintah akan menunggu, dan `status <job_id>` melanjutkannya lagi jika Anda menghentikannya.

## Tautan

- [Equalang](https://equalang.com) · [Harga](https://equalang.com/pricing) · [Dokumentasi developer](https://equalang.com/developers)
- API untuk agen: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - operasi yang sama sebagai server MCP
- Pertanyaan: <support@equalang.com>

## Lisensi

[Apache-2.0](../LICENSE) © Equalang
