# Equalang-Skill

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Ein [Agent Skill](https://github.com/anthropics/skills), der Claude Code, Codex, Cursor und anderen Agenten [Equalang](https://equalang.com) gibt: ganze Dateien mit erhaltenem Layout übersetzen, Aufnahmen transkribieren, Strings in großen Mengen übersetzen.

- **Dokumente** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - kommen im selben Format zurück.
- **Untertitel** (SRT, VTT) und **Bilder** (JPG, PNG, WebP, BMP).
- **Audio und Video** kommen als übersetzte Untertitel zurück oder als Transkript in der gesprochenen Sprache.

## Installation

Füge das bei deinem Agenten ein:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Oder von Hand - ein Skill ist ein Ordner:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # Schlüssel erstellen unter https://equalang.com/api-keys
```

Als Claude Code-Plugin: `/plugin marketplace add equalang/equalang-skill`, dann `/plugin install equalang@equalang`.

`python3` (3.8+) ist alles, was nötig ist; es gibt nichts per `pip install` zu installieren.

## Was der Agent ausführt

```bash
python3 scripts/equalang.py estimate report.pdf                  # was würde es kosten? (kostenlos)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # Ergebnis landet neben der Quelldatei
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Sprachen.** Codes sehen aus wie `en`, `zh-CN`, `ja`. In den Skill ist keine Liste eingebaut: `languages` liest Codes und Namen aus der Live-API (`--kind text` für die größere Auswahl, die `text` annimmt), sodass eine Sprache, die Equalang hinzufügt, ohne Update verfügbar ist.

**Credits.** Arbeit verbraucht die Credits des Kontos, dasselbe Guthaben wie auf der Website. SKILL.md lässt den Agenten zuerst die Kosten nennen - aus `estimate` - und die Zustimmung einholen.

Jeder Befehl gibt ein einziges JSON-Objekt aus - Pfade und Credits, nie Dateiinhalte - oder `{"error", "code", "retryable"}` mit Exit-Code 1. [SKILL.md](../SKILL.md) ist das, was der Agent liest.

## Wie er gebaut ist

Dieselben drei Entscheidungen wie beim [MCP-Server](https://github.com/equalang/equalang-mcp), der dieselben Operationen als Tools anbietet:

1. **Eine Datei läuft nie durch das Modell** - Befehle nehmen entgegen, wo eine Datei liegt (ein Pfad oder eine öffentliche URL, die Equalang selbst abruft), und geben aus, wohin die Ergebnisse geschrieben wurden.
2. **Ein Auftrag lebt innerhalb eines Befehls** - hochladen, warten (mit Pausen, so lang das `Retry-After` der API verlangt), herunterladen. Das Warten zu unterbrechen bricht den Auftrag nicht ab; `status` nimmt ihn wieder auf.
3. **Die Antworten der API werden wiedergegeben, nicht erraten** - wiederholt wird nur, was die API als `retryable` markiert; die Kosten sind das `quote` der API; die Sprachliste wird aus ihrem OpenAPI-Dokument gelesen; ein `Idempotency-Key` pro angelegtem Auftrag, sodass aus einer verlorenen Antwort kein zweiter, berechneter Auftrag werden kann.

`python3 scripts/check_api.py` prüft ohne Schlüssel, dass jeder Pfad und jedes Feld, das das Skript verwendet - und jedes Format, das SKILL.md verspricht - noch im Vertrag der API steht. Die API selbst: <https://equalang.com/llms.txt>.

Apache-2.0.
