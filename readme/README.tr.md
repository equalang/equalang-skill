# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · **Türkçe** · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Web sitesi](https://equalang.com) · [Fiyatlandırma](https://equalang.com/pricing) · [Geliştirici belgeleri](https://equalang.com/developers) · [API anahtarları](https://equalang.com/api-keys)

> **Anahtar kelimeler:** belge çevirisi, doküman çeviri, pdf çeviri, pdf çevirici, pdf çeviri format bozulmadan, word belgesi çeviri, powerpoint sunum çeviri, excel çeviri, epub çeviri, altyazı çeviri, srt çeviri, resimdeki yazıyı çevirme, video çeviri, ses dosyasını yazıya çevirme, sesi yazıya dökme, yapay zeka çeviri, agent skill, claude code skill, codex skill, translation api

**Dosyayı çevirin, düzeni koruyun.** [Equalang](https://equalang.com) için bir [Agent Skill](https://agentskills.io). Equalang, dosyaları bütün halinde çeviren bir yapay zekâ çevirmenidir: PDF yine PDF olarak, sunum yine sunum olarak geri gelir; tablolar, görseller ve formüller yerli yerinde kalır. Altyazıları ve resimleri de çevirir, ses ve videoyu çevrilmiş altyazıya ya da döküme dönüştürür, metinleri toplu halde çevirir. Claude Code, Codex, Cursor, CodeBuddy ve Agent Skills yükleyen diğer tüm ajanlarda çalışır.

## Özellikler

- **Hangi biçimde girdiyse o biçimde çıkar** – PDF, DOCX, PPTX, XLSX, EPUB, HTML ve TXT aynı biçimde, düzenlenebilir halde geri gelir; tablolar, görseller, formüller ve sayfa düzeni yerinde kalır
- **Altyazılar ve resimler** – SRT ve VTT zamanlamasını korur, istenirse kaynak satır çevirinin üstünde yer alır; JPG, PNG, WebP ve BMP, resmin içindeki metin çevrilmiş olarak geri gelir
- **Ses ve video** – MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM ve MKV çevrilmiş altyazıya ya da konuşulan dilde bir döküme dönüşür (SRT, VTT, TXT, JSON)
- **Toplu metin** – ayrı dizeler sırasıyla çevrilir ya da Equalang'ın cümle sınırlarından kendisinin böldüğü tek bir uzun metin (100.000 karaktere kadar); metin için 100+, dosyalar için 12 dil
- **Bütün dosyalar, kopyala-yapıştır yok** – dosya başına en fazla 100 MB, bir yoldan ya da herkese açık bir URL'den; metin kutularına bölüp yapıştıracak bir şey yok
- **Token harcamaz** – dosya Equalang'a gider, geriye bir yol gelir; 300 sayfalık bir PDF konuşmaya hiç girmez
- **İşten önce fiyat** – `estimate`, bir işin en fazla kaça mal olabileceğini ücretsiz söyler; başarısız olan ve iptal edilen işler ücretlendirilmez; bir kayıt, gerçekten duyulan konuşma kadar ücretlendirilir; kredilerin süresi dolmaz
- **Kurulacak bir şey yok** – tek bir Python betiği, yalnızca standart kitaplık, Python 3.8+

## Anahtar alın

<https://equalang.com> adresinde kaydolun ve <https://equalang.com/api-keys> adresinde bir anahtar oluşturun. Yeni hesaplar ücretsiz kredilerle başlar – bir belgeyi çevirtip geriye ne geldiğini görmeye yeter.

```bash
export EQUALANG_API_KEY=el_your_key
```

Ya da bu dizinde `.env.example` dosyasını `.env` olarak kopyalayın – git tarafından yok sayılır. Anahtar yalnızca bir kez gösterilir; Equalang onun sadece hash'ini saklar.

## Kurulum

En kısa yol – bunu ajanınıza yapıştırın:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# Kaça mal olur? Ücretsizdir ve hiçbir şey başlatılmaz
python3 scripts/equalang.py estimate report.pdf

# Bir dosyayı çevirir; sonuç kaynağın yanına kaydedilir
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Herkese açık bir URL'den (Equalang kendisi çeker), bir klasöre
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Bir kayıtta söylenenler, zaman damgalı metin olarak
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Ayrı dizeler, sırasıyla
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Equalang'ın cümle sınırlarından böldüğü tek bir uzun metin
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Çalışır halde bırakılmış bir iş, bakiye ve dil kodları
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Her komut tek bir JSON nesnesi yazdırır – yollar ve krediler, asla dosya içeriği değil – ya da çıkış kodu 1 ile `{"error", "code", "retryable"}`. Herhangi bir komutta `--help`, o komutun bayraklarını listeler. Ajanın okuduğu dosya [SKILL.md](../SKILL.md)'dir.

## Bilmeye değer üç şey

**Diller.** Kodlar `en`, `zh-CN`, `ja` biçimindedir. Beceriye gömülü bir liste yoktur: `languages` kodları ve adları canlı API'den okur (`text` komutunun kabul ettiği daha geniş küme için `--kind text`), böylece Equalang'ın eklediği bir dil güncelleme gerekmeden kullanılabilir. Kaynak dilin algılanması için onu boş bırakın.

**Krediler.** İşler hesabın kredilerini harcar; web sitesindekiyle aynı bakiye. SKILL.md, ajanın bir işi başlatmadan önce maliyeti – `estimate` komutundan alarak – söylemesini ve onay almasını sağlar.

**İşler dakikalar sürer.** Komut bekler; API'nin `Retry-After` değerinin istediği kadar duraklar. Komutu kesmek işi iptal etmez – `status <job_id>` işi yeniden ele alır ve sonucu indirir.

## Sık sorulan sorular

**Çevrilen PDF düzenini korur mu?**
Evet – zaten bütün mesele bu. Metin eski yerine konur; tablolar, görseller ve formüller yerinde kalır; DOCX, PPTX ya da XLSX düzenlenebilir kalır.

**Belgem modele gönderiliyor mu?**
Hayır. Betik dosyayı Equalang'a yükler ve bir yol yazdırır. 300 sayfalık bir makale hiç token harcamaz.

**Bir resmin içindeki metni çevirebilir mi?**
Evet. JPG, PNG, WebP ya da BMP içindeki metin tanınır, çevrilir ve resme yeniden işlenir.

**Bir iş kaça mal olur?**
`estimate` bunu hiçbir şey başlamadan önce söyler ve ücretsizdir. Fiyatlar <https://equalang.com/pricing> adresindedir.

## Nasıl tasarlandı

[MCP sunucusu](https://github.com/equalang/equalang-mcp) ile aynı üç karar:

1. **Dosya asla modelin içinden geçmez** – komutlar dosyanın nerede olduğunu alır (bir yol ya da Equalang'ın kendisinin çektiği herkese açık bir URL) ve sonuçların nereye yazıldığını yazdırır.
2. **Bir iş tek bir komutun içinde yaşar** – yükle, bekle, indir. `status`, beklemesi yarıda kesilmiş bir işi yeniden ele alır.
3. **API'nin yanıtları tahmin edilmez, aktarılır** – yalnızca API'nin `retryable` olarak işaretlediği yeniden denenir; maliyet API'nin `quote` değeridir; dil listesi onun OpenAPI belgesinden okunur; oluşturulan her iş için tek bir `Idempotency-Key`, böylece kaybolan bir yanıt ikinci, ücretlendirilmiş bir işe dönüşemez.

`python3 scripts/check_api.py`, betiğin kullandığı her yolun ve alanın – ve SKILL.md'nin vaat ettiği her biçimin – hâlâ API'nin sözleşmesinde olduğunu anahtar gerekmeden doğrular.

## Bağlantılar

- [Equalang](https://equalang.com) · [Fiyatlandırma](https://equalang.com/pricing) · [Geliştirici belgeleri](https://equalang.com/developers)
- Ajanlar için API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) – aynı işlemler, MCP sunucusu olarak
- Sorular: <support@equalang.com>

## Lisans

[Apache-2.0](../LICENSE) © Equalang
