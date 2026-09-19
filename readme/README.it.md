# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · **Italiano** · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Sito web](https://equalang.com) · [Prezzi](https://equalang.com/pricing) · [Documentazione per sviluppatori](https://equalang.com/developers) · [Chiavi API](https://equalang.com/api-keys)

> **Parole chiave:** traduzione documenti, tradurre pdf, traduttore pdf, tradurre pdf mantenendo il layout, tradurre documento word, tradurre powerpoint, tradurre file excel, tradurre epub, traduzione sottotitoli, tradurre srt, tradurre testo in un'immagine, traduzione video, trascrizione audio, da audio a testo, traduttore ai, agent skill, claude code skill, codex skill, translation api

**Traduci il file, conserva l'impaginazione.** Una [Agent Skill](https://agentskills.io) per [Equalang](https://equalang.com), un traduttore AI che lavora su file interi: un PDF torna come PDF, una presentazione come presentazione, con tabelle, immagini e formule dov'erano. Traduce anche sottotitoli e immagini, trasforma audio e video in sottotitoli tradotti o in una trascrizione, e traduce stringhe in blocco. Funziona in Claude Code, Codex, Cursor, CodeBuddy e in ogni altro agente che carica le Agent Skills.

## Funzionalità

- **Stesso formato in ingresso e in uscita** – PDF, DOCX, PPTX, XLSX, EPUB, HTML e TXT tornano nello stesso formato, ancora modificabili, con tabelle, immagini, formule e impaginazione al loro posto
- **Sottotitoli e immagini** – SRT e VTT conservano i tempi, volendo con la riga originale sopra la traduzione; JPG, PNG, WebP e BMP tornano con il testo nell'immagine tradotto
- **Audio e video** – MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM e MKV diventano sottotitoli tradotti, oppure una trascrizione nella lingua parlata (SRT, VTT, TXT, JSON)
- **Testo in blocco** – stringhe separate tradotte nell'ordine dato, oppure un unico testo lungo (fino a 100.000 caratteri) che Equalang divide da sé in frasi; oltre 100 lingue per il testo, 12 per i file
- **File interi, niente copia e incolla** – fino a 100 MB per file, da un percorso o da un URL pubblico; nulla da spezzettare in caselle di testo
- **Non costa token** – il file va a Equalang e torna un percorso; un PDF di 300 pagine non entra mai nella conversazione
- **Il prezzo prima del job** – `estimate` risponde, gratis, con il costo massimo di un job; i job falliti o annullati non costano nulla; una registrazione viene addebitata per il parlato effettivamente rilevato; i crediti non scadono mai
- **Niente da installare** – un solo script Python, solo libreria standard, Python 3.8+

## Ottieni una chiave

Registrati su <https://equalang.com> e crea una chiave su <https://equalang.com/api-keys>. I nuovi account partono con crediti gratuiti: abbastanza per far passare un documento e vedere che cosa torna indietro.

```bash
export EQUALANG_API_KEY=el_your_key
```

Oppure copia `.env.example` in `.env` in questa directory: è ignorato da git. La chiave viene mostrata una sola volta; Equalang ne conserva soltanto un hash.

## Installazione

La via più breve: incolla questo al tuo agente:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (manuale)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

La vuoi solo per un progetto? Clona in `.claude/skills/equalang` dentro il repository.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex legge anche `.agents/skills/` all'interno di un repository, per limitarla a un solo progetto.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Solo per un progetto: clona in `.codebuddy/skills/equalang` nella radice del progetto.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro e altri</b></summary>

Questa è una semplice [Agent Skill](https://agentskills.io): una cartella con dentro un `SKILL.md`. Ogni client che implementa lo standard carica la stessa cartella – cambia solo la directory in cui la cerca, e ciascuno documenta la propria. Clona il repository in quella directory e la skill è installata.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Preferisci un server MCP? [equalang-mcp](https://github.com/equalang/equalang-mcp) offre le stesse operazioni sotto forma di strumenti, e funziona anche in Claude Desktop, Cursor, Windsurf, Cline e OpenCode.

## Comandi

```bash
# Quanto costerebbe? Gratis, e non viene avviato nulla
python3 scripts/equalang.py estimate report.pdf

# Traduce un file; il risultato finisce accanto all'originale
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Da un URL pubblico (lo scarica Equalang stesso), in una cartella
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Che cosa dice una registrazione, come testo con i tempi
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Stringhe separate, nell'ordine dato
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Un unico testo lungo, diviso in frasi da Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Un job rimasto in esecuzione, il saldo e i codici delle lingue
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Ogni comando stampa un solo oggetto JSON – percorsi e crediti, mai il contenuto dei file – oppure `{"error", "code", "retryable"}` con codice di uscita 1. `--help` su qualsiasi comando ne elenca le opzioni. [SKILL.md](../SKILL.md) è ciò che l'agente legge.

## Tre cose da sapere

**Lingue.** I codici hanno la forma `en`, `zh-CN`, `ja`. Nella skill non c'è alcun elenco incorporato: `languages` legge codici e nomi dall'API in tempo reale (`--kind text` per l'insieme più ampio accettato da `text`), quindi una lingua aggiunta da Equalang è disponibile senza aggiornamenti. Ometti la lingua di origine per farla rilevare automaticamente.

**Crediti.** Il lavoro consuma i crediti dell'account, lo stesso saldo del sito web. SKILL.md fa sì che l'agente indichi il costo – ricavato da `estimate` – e ottenga il consenso prima di avviare un job.

**I job durano minuti.** Il comando aspetta, sospendendosi per il tempo richiesto dal `Retry-After` dell'API. Interromperlo non annulla il job: `status <job_id>` lo riprende e scarica il risultato.

## Domande frequenti

**Il PDF tradotto conserva l'impaginazione?**
Sì, è proprio questo il punto. Il testo viene rimesso dov'era, e tabelle, immagini e formule restano al loro posto; un DOCX, PPTX o XLSX resta modificabile.

**Il mio documento viene inviato al modello?**
No. Lo script carica il file su Equalang e stampa un percorso. Un articolo di 300 pagine non costa alcun token.

**Può tradurre il testo dentro un'immagine?**
Sì. Il testo in un JPG, PNG, WebP o BMP viene riconosciuto, tradotto e ridisegnato nell'immagine.

**Quanto costa un job?**
Lo dice `estimate` prima che parta qualsiasi cosa, ed è gratuito. I prezzi sono su <https://equalang.com/pricing>.

## Com'è costruita

Le stesse tre decisioni del [server MCP](https://github.com/equalang/equalang-mcp):

1. **Un file non passa mai attraverso il modello** – i comandi ricevono dove si trova un file (un percorso, oppure un URL pubblico che Equalang scarica da sé) e stampano dove sono stati scritti i risultati.
2. **Un job vive dentro un solo comando** – caricamento, attesa, download. `status` riprende un job la cui attesa è stata interrotta.
3. **Le risposte dell'API vengono riportate, non indovinate** – si ritenta solo ciò che l'API contrassegna come `retryable`; il costo è il `quote` dell'API; l'elenco delle lingue viene letto dal suo documento OpenAPI; una sola `Idempotency-Key` per ogni job creato, così una risposta persa non può diventare un secondo job addebitato.

`python3 scripts/check_api.py` verifica, senza chiave, che ogni percorso e campo usato dallo script – e ogni formato promesso da SKILL.md – sia ancora nel contratto dell'API.

## Link

- [Equalang](https://equalang.com) · [Prezzi](https://equalang.com/pricing) · [Documentazione per sviluppatori](https://equalang.com/developers)
- API per agenti: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) – le stesse operazioni come server MCP
- Domande: <support@equalang.com>

## Licenza

[Apache-2.0](../LICENSE) © Equalang
