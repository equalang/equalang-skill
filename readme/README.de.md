# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Website](https://equalang.com) · [Preise](https://equalang.com/pricing) · [Entwicklerdokumentation](https://equalang.com/developers) · [API-Schlüssel](https://equalang.com/api-keys)

> **Stichwörter:** pdf übersetzen, pdf übersetzer, pdf übersetzen layout beibehalten, dokumente übersetzen, word dokument übersetzen, docx übersetzen, powerpoint übersetzen, excel übersetzen, epub übersetzen, untertitel übersetzen, srt übersetzen, bild übersetzen, text im bild übersetzen, video übersetzen, audio transkribieren, sprache in text, ki übersetzer, agent skill, claude code skill, codex skill, translation api

**Datei übersetzen, Layout behalten.** Ein [Agent Skill](https://agentskills.io) für [Equalang](https://equalang.com) – einen KI-Übersetzer, der mit ganzen Dateien arbeitet: Ein PDF kommt als PDF zurück, eine Präsentation als Präsentation, Tabellen, Bilder und Formeln bleiben, wo sie waren. Er übersetzt außerdem Untertitel und Bilder, macht aus Audio und Video übersetzte Untertitel oder ein Transkript und übersetzt kurze Texte in großen Mengen. Läuft in Claude Code, Codex, Cursor, CodeBuddy und jedem anderen Agenten, der Agent Skills lädt.

## Beispielanfragen

- „Übersetze ~/Documents/contract.pdf ins Deutsche und behalte das Layout bei.“
- „Übersetze pitch-deck.pptx ins Englische und Französische.“
- „Übersetze https://example.com/whitepaper.pdf ins Deutsche und speichere es in ~/Downloads.“
- „Was würde es kosten, thesis.docx ins Englische zu übersetzen?“
- „Erstelle deutsche Untertitel für interview.mp4, mit der Originalzeile über jeder Übersetzung.“
- „Transkribiere standup.m4a mit Zeitstempeln.“
- „Erstelle eine deutsche Version von menu.jpg.“
- „Übersetze novel.epub ins Deutsche.“

## Funktionen

- **Dokumente** – PDF, DOCX, PPTX, XLSX, EPUB, HTML und TXT kommen im selben Format zurück, weiterhin bearbeitbar, Tabellen, Bilder, Formeln und Seitenlayout an ihrem Platz
- **Untertitel und Bilder** – SRT und VTT behalten ihr Timing, auf Wunsch mit der Originalzeile über der Übersetzung; JPG, PNG, WebP und BMP kommen mit übersetztem Text im Bild zurück
- **Audio und Video** – aus MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM und MKV werden übersetzte Untertitel oder ein Transkript in der gesprochenen Sprache (SRT, VTT, TXT, JSON)
- **Text in großen Mengen** – kurze Texte, in ihrer Reihenfolge übersetzt, oder ein langer Text (bis zu 100.000 Zeichen), den Equalang selbst an Satzgrenzen teilt
- **Sprachen** – über 100 für Text und 12 für Dateien, wobei die Quellsprache erkannt wird, wenn du sie weglässt

## Schlüssel holen

Registriere dich unter <https://equalang.com> und erstelle einen Schlüssel unter <https://equalang.com/api-keys>. Neue Konten bekommen kostenlose Credits – genug, um ein Dokument zu übersetzen und es auszuprobieren.

Speichere ihn einmal in `~/.config/equalang/.env`, dann gilt er dauerhaft: in jedem Agenten – Claude Code, Codex, WorkBuddy, Cursor oder einem anderen –, in jeder neuen Sitzung und auch nach Neuinstallation oder Update, ganz ohne export. Der Equalang-MCP-Server liest dieselbe Datei.

```bash
# Ersetze el_your_key durch deinen Schlüssel
mkdir -p ~/.config/equalang && echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env && chmod 600 ~/.config/equalang/.env
```

Zuerst wird die Umgebungsvariable `EQUALANG_API_KEY` geprüft, die Datei nur gelesen, wenn sie fehlt – so kann ein einzelnes Projekt einen anderen Schlüssel verwenden.

## Installation

Benötigt `python3` 3.8 oder neuer, sonst nichts: Das Skript verwendet nur die Standardbibliothek.

Der kürzeste Weg – füge das bei deinem Agenten ein:

> Installiere den Equalang-Skill, indem du der Anleitung unter https://equalang.com/install/skill-install.md folgst.

<details open>
<summary><b>Claude Code</b> (Plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (von Hand)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Lieber nur für ein Projekt? Klone nach `.claude/skills/equalang` im Repository.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex liest auch `.agents/skills/` innerhalb eines Repositorys, um den Skill auf ein Projekt zu beschränken.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Nur für ein Projekt: Klone nach `.codebuddy/skills/equalang` im Projektstamm.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro und andere</b></summary>

Das ist ein ganz normaler [Agent Skill](https://agentskills.io): ein Ordner mit einer `SKILL.md` darin. Jeder Client, der den Standard umsetzt, lädt denselben Ordner – nur das Verzeichnis, das er durchsucht, ist ein anderes, und jeder dokumentiert sein eigenes. Klone das Repository in dieses Verzeichnis, und der Skill ist installiert.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Lieber ein MCP-Server? [equalang-mcp](https://github.com/equalang/equalang-mcp) bietet dieselben Operationen als Tools an und läuft auch in Claude Desktop, Cursor, Windsurf, Cline und OpenCode.

## Befehle

```bash
# Was würde es kosten? Kostenlos, und es wird nichts übersetzt
python3 scripts/equalang.py estimate report.pdf

# Eine Datei übersetzen; das Ergebnis landet neben der Quelldatei
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Von einer öffentlichen URL (Equalang ruft sie selbst ab), in einen Ordner
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Was in einer Aufnahme gesagt wird, als Text mit Zeitmarken
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Kurze Texte, in ihrer Reihenfolge
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Ein langer Text, von Equalang an Satzgrenzen geteilt
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Ein Auftrag, der noch läuft, das Guthaben und die Sprachcodes
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Jeder Befehl gibt JSON aus: wohin die Dateien geschrieben wurden und was sie gekostet haben, oder was schiefgegangen ist. Hänge `--help` an einen beliebigen Befehl, um dessen Optionen zu sehen. Der Agent selbst liest [SKILL.md](../SKILL.md).

Sprachcodes sehen aus wie `en`, `zh-CN`, `ja`. Mit `languages` bekommst du die Liste, mit `languages chinese` suchst du darin. Ein Auftrag dauert Minuten – der Befehl wartet, und `status <job_id>` nimmt ihn wieder auf, wenn du ihn unterbrichst.

## Links

- [Equalang](https://equalang.com) · [Preise](https://equalang.com/pricing) · [Entwicklerdokumentation](https://equalang.com/developers)
- API für Agenten: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) – dieselben Operationen als MCP-Server
- Fragen: <support@equalang.com>

## Lizenz

[Apache-2.0](../LICENSE) © Equalang
