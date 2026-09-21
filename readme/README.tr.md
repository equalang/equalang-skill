# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · **Türkçe** · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Web sitesi](https://equalang.com) · [Fiyatlandırma](https://equalang.com/pricing) · [Geliştirici belgeleri](https://equalang.com/developers) · [API anahtarları](https://equalang.com/api-keys)

> **Anahtar kelimeler:** belge çevirisi, doküman çeviri, pdf çeviri, pdf çevirici, pdf çeviri format bozulmadan, word belgesi çeviri, powerpoint sunum çeviri, excel çeviri, epub çeviri, altyazı çeviri, srt çeviri, resimdeki yazıyı çevirme, video çeviri, ses dosyasını yazıya çevirme, sesi yazıya dökme, yapay zeka çeviri, agent skill, claude code skill, codex skill, translation api

**Dosyayı çevirin, düzeni koruyun.** [Equalang](https://equalang.com) için bir [Agent Skill](https://agentskills.io). Equalang, dosyaları bütün halinde çeviren bir yapay zekâ çevirmenidir: PDF yine PDF olarak, sunum yine sunum olarak geri gelir; tablolar, görseller ve formüller yerli yerinde kalır. Altyazıları ve resimleri de çevirir, ses ve videoyu çevrilmiş altyazıya ya da döküme dönüştürür, kısa metinleri toplu halde çevirir. Claude Code, Codex, Cursor, CodeBuddy ve Agent Skills yükleyen diğer tüm ajanlarda çalışır.

## Şöyle isteyebilirsiniz

- “~/Documents/contract.pdf dosyasını Türkçeye çevir, sayfa düzeni aynı kalsın.”
- “pitch-deck.pptx dosyasını İngilizceye ve Almancaya çevir.”
- “https://example.com/whitepaper.pdf dosyasını Türkçeye çevirip ~/Downloads içine kaydet.”
- “thesis.docx dosyasını İngilizceye çevirmek ne kadar tutar?”
- “interview.mp4 için Türkçe altyazı hazırla; her satırın üstünde orijinali kalsın.”
- “standup.m4a kaydını zaman damgalarıyla yazıya dök.”
- “menu.jpg içindeki yazıyı Türkçeye çevir.”
- “locales/en.json içindeki metinleri Almancaya, Fransızcaya ve Arapçaya çevir.”

## Özellikler

- **Belgeler** – PDF, DOCX, PPTX, XLSX, EPUB, HTML ve TXT aynı biçimde, düzenlenebilir halde geri gelir; tablolar, görseller, formüller ve sayfa düzeni yerinde kalır
- **Altyazılar ve resimler** – SRT ve VTT zamanlamasını korur, istenirse kaynak satır çevirinin üstünde yer alır; JPG, PNG, WebP ve BMP, resmin içindeki metin çevrilmiş olarak geri gelir
- **Ses ve video** – MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM ve MKV çevrilmiş altyazıya ya da konuşulan dilde bir döküme dönüşür (SRT, VTT, TXT, JSON)
- **Toplu metin** – kısa metinler sırasıyla çevrilir ya da Equalang'ın cümle sınırlarından kendisinin böldüğü tek bir uzun metin (100.000 karaktere kadar)
- **Diller** – metin için 100+, dosyalar için 12; kaynak dili boş bıraktığınızda otomatik olarak algılanır

## Anahtar alın

<https://equalang.com> adresinde kaydolun ve <https://equalang.com/api-keys> adresinde bir anahtar oluşturun. Yeni hesaplar ücretsiz kredilerle başlar – bir belgeyi çevirip denemeye yeter.

Anahtarı bir kez `~/.config/equalang/.env` dosyasına kaydedin, kalıcı olarak geçerli olur: hangi ajanı kullanırsanız kullanın - Claude Code, Codex, WorkBuddy, Cursor ya da başka biri - her yeni oturumda, yeniden kurulum ve güncellemelerden sonra da, export gerekmeden. Equalang MCP sunucusu da aynı dosyayı okur.

```bash
mkdir -p ~/.config/equalang
echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env
chmod 600 ~/.config/equalang/.env
```

Ortamda tanımlı `EQUALANG_API_KEY` önceliklidir; tek bir projede farklı bir anahtar kullanmak için bunu kullanın.

## Kurulum

`python3` 3.8 veya üzeri gerekir, başka bir şey gerekmez: betik yalnızca standart kitaplığı kullanır.

En kısa yol – bunu ajanınıza yapıştırın:

> Equalang becerisini https://equalang.com/install/skill-install.md adresindeki yönergeleri izleyerek kurun.

<details open>
<summary><b>Claude Code</b> (eklenti)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (elle)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Yalnızca tek bir proje için mi? Depodaki `.claude/skills/equalang` dizinine klonlayın.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex, beceriyi tek bir projeyle sınırlamak için bir deponun içindeki `.agents/skills/` dizinini de okur.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Tek proje için: proje kökündeki `.codebuddy/skills/equalang` dizinine klonlayın.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro ve diğerleri</b></summary>

Bu sade bir [Agent Skill](https://agentskills.io): içinde `SKILL.md` bulunan bir klasör. Standardı uygulayan her istemci aynı klasörü yükler – yalnızca taradığı dizin farklıdır ve her istemci kendi dizinini belgelerinde belirtir. Depoyu o dizine klonlayın, beceri kurulmuş olur.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

MCP sunucusu mu tercih edersiniz? [equalang-mcp](https://github.com/equalang/equalang-mcp) aynı işlemleri araç olarak sunar; Claude Desktop, Cursor, Windsurf, Cline ve OpenCode'da da çalışır.

## Komutlar

```bash
# Kaça mal olur? Ücretsizdir, çeviri başlamaz
python3 scripts/equalang.py estimate report.pdf

# Bir dosyayı çevirir; sonuç kaynağın yanına kaydedilir
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Herkese açık bir URL'den (Equalang kendisi çeker), bir klasöre
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Bir kayıtta söylenenler, zaman damgalı metin olarak
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Kısa metinler, sırasıyla
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Equalang'ın cümle sınırlarından böldüğü tek bir uzun metin
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Çalışır halde bırakılmış bir iş, bakiye ve dil kodları
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Her komut JSON yazdırır: dosyaların nereye yazıldığını ve kaça mal olduğunu ya da neyin ters gittiğini. Bayraklarını görmek için herhangi bir komuta `--help` ekleyin. Ajanın okuduğu dosya [SKILL.md](../SKILL.md)'dir.

Dil kodları `en`, `zh-CN`, `ja` biçimindedir. Hepsini listelemek için `languages`, aramak için `languages chinese` çalıştırın. İşler dakikalar sürer – komut bekler ve komutu kesersen `status <job_id>` işi yeniden ele alır.

## Bağlantılar

- [Equalang](https://equalang.com) · [Fiyatlandırma](https://equalang.com/pricing) · [Geliştirici belgeleri](https://equalang.com/developers)
- Ajanlar için API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) – aynı işlemler, MCP sunucusu olarak
- Sorular: <support@equalang.com>

## Lisans

[Apache-2.0](../LICENSE) © Equalang
