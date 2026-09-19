# Skill di Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · **Italiano** · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Una [Agent Skill](https://github.com/anthropics/skills) che mette [Equalang](https://equalang.com) a disposizione di Claude Code, Codex, Cursor e altri agenti: traduce file interi conservandone l'impaginazione, trascrive registrazioni, traduce stringhe in blocco.

- **Documenti** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - tornano nello stesso formato.
- **Sottotitoli** (SRT, VTT) e **immagini** (JPG, PNG, WebP, BMP).
- **Audio e video** tornano come sottotitoli tradotti, oppure come trascrizione nella lingua parlata.

## Installazione

Incolla questo al tuo agente:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Oppure a mano - una skill è una cartella:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # creane una su https://equalang.com/api-keys
```

Come plugin di Claude Code: `/plugin marketplace add equalang/equalang-skill`, poi `/plugin install equalang@equalang`.

Serve solo `python3` (3.8+); non c'è nulla da installare con `pip install`.

## Cosa esegue l'agente

```bash
python3 scripts/equalang.py estimate report.pdf                  # quanto costerebbe? (gratuito)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # il risultato finisce accanto all'originale
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # un unico testo lungo, diviso in frasi da Equalang
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Lingue.** I codici hanno la forma `en`, `zh-CN`, `ja`. Nella skill non c'è alcun elenco incorporato: `languages` legge codici e nomi dall'API in tempo reale (`--kind text` per l'insieme più ampio accettato da `text`), quindi una lingua aggiunta da Equalang è disponibile senza aggiornamenti.

**Crediti.** Il lavoro consuma i crediti dell'account, lo stesso saldo del sito web. SKILL.md fa sì che l'agente indichi prima il costo - ricavato da `estimate` - e ottenga il consenso.

Ogni comando stampa un solo oggetto JSON - percorsi e crediti, mai il contenuto dei file - oppure `{"error", "code", "retryable"}` con codice di uscita 1. [SKILL.md](../SKILL.md) è ciò che l'agente legge.

## Com'è costruita

Le stesse tre decisioni del [server MCP](https://github.com/equalang/equalang-mcp), che offre le stesse operazioni sotto forma di strumenti:

1. **Un file non passa mai attraverso il modello** - i comandi ricevono dove si trova un file (un percorso, oppure un URL pubblico che Equalang scarica da sé) e stampano dove sono stati scritti i risultati.
2. **Un job vive dentro un solo comando** - caricamento, attesa (sospendendosi per il tempo richiesto dal `Retry-After` dell'API), download. Interrompere l'attesa non annulla il job; `status` lo riprende.
3. **Le risposte dell'API vengono riportate, non indovinate** - si ritenta solo ciò che l'API contrassegna come `retryable`; il costo è il `quote` dell'API; l'elenco delle lingue viene letto dal suo documento OpenAPI; una sola `Idempotency-Key` per ogni job creato, così una risposta persa non può diventare un secondo job addebitato.

`python3 scripts/check_api.py` verifica, senza chiave, che ogni percorso e campo usato dallo script - e ogni formato promesso da SKILL.md - sia ancora nel contratto dell'API. L'API stessa: <https://equalang.com/llms.txt>.

Apache-2.0.
