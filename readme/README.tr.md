# Equalang becerisi

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · **Türkçe** · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Claude Code, Codex, Cursor ve diğer ajanlara [Equalang](https://equalang.com)'ı kazandıran bir [Agent Skill](https://github.com/anthropics/skills): dosyaları düzenini koruyarak bütün halinde çevirin, kayıtları yazıya dökün, metinleri toplu halde çevirin.

- **Belgeler** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - aynı biçimde geri gelir.
- **Altyazılar** (SRT, VTT) ve **resimler** (JPG, PNG, WebP, BMP).
- **Ses ve video** çevrilmiş altyazı olarak ya da konuşulan dilde bir döküm olarak geri gelir.

## Kurulum

Bunu ajanınıza yapıştırın:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Ya da elle - bir beceri, bir klasörden ibarettir:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # https://equalang.com/api-keys adresinde bir tane oluşturun
```

Claude Code eklentisi olarak: `/plugin marketplace add equalang/equalang-skill`, ardından `/plugin install equalang@equalang`.

Tek gereken `python3` (3.8+); `pip install` edilecek hiçbir şey yok.

## Ajanın çalıştırdıkları

```bash
python3 scripts/equalang.py estimate report.pdf                  # kaça mal olur? (ücretsiz)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # sonuç kaynağın yanına kaydedilir
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Diller.** Kodlar `en`, `zh-CN`, `ja` biçimindedir. Beceriye gömülü bir liste yoktur: `languages` kodları ve adları canlı API'den okur (`text` komutunun kabul ettiği daha geniş küme için `--kind text`), böylece Equalang'ın eklediği bir dil güncelleme gerekmeden kullanılabilir.

**Krediler.** İşler hesabın kredilerini harcar; web sitesindekiyle aynı bakiye. SKILL.md, ajanın önce maliyeti - `estimate` komutundan alarak - söylemesini ve onay almasını sağlar.

Her komut tek bir JSON nesnesi yazdırır - yollar ve krediler, asla dosya içeriği değil - ya da çıkış kodu 1 ile `{"error", "code", "retryable"}`. Ajanın okuduğu dosya [SKILL.md](../SKILL.md)'dir.

## Nasıl tasarlandı

Aynı işlemleri araç olarak sunan [MCP sunucusu](https://github.com/equalang/equalang-mcp) ile aynı üç karar:

1. **Dosya asla modelin içinden geçmez** - komutlar dosyanın nerede olduğunu alır (bir yol ya da Equalang'ın kendisinin çektiği herkese açık bir URL) ve sonuçların nereye yazıldığını yazdırır.
2. **Bir iş tek bir komutun içinde yaşar** - yükle, bekle (API'nin `Retry-After` değerinin istediği kadar durarak), indir. Beklemeyi kesmek işi iptal etmez; `status` onu yeniden ele alır.
3. **API'nin yanıtları tahmin edilmez, aktarılır** - yalnızca API'nin `retryable` olarak işaretlediği yeniden denenir; maliyet API'nin `quote` değeridir; dil listesi onun OpenAPI belgesinden okunur; oluşturulan her iş için tek bir `Idempotency-Key`, böylece kaybolan bir yanıt ikinci, ücretlendirilmiş bir işe dönüşemez.

`python3 scripts/check_api.py`, betiğin kullandığı her yolun ve alanın - ve SKILL.md'nin vaat ettiği her biçimin - hâlâ API'nin sözleşmesinde olduğunu anahtar gerekmeden doğrular. API'nin kendisi: <https://equalang.com/llms.txt>.

Apache-2.0.
