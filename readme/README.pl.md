# Skill Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · **Polski** · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Agent Skill](https://github.com/anthropics/skills), który daje Claude Code, Codex, Cursor i innym agentom [Equalang](https://equalang.com): tłumaczenie całych plików z zachowaniem układu, transkrypcję nagrań, hurtowe tłumaczenie tekstów.

- **Dokumenty** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - wracają w tym samym formacie.
- **Napisy** (SRT, VTT) i **obrazy** (JPG, PNG, WebP, BMP).
- **Audio i wideo** wracają jako przetłumaczone napisy albo jako transkrypcja w języku nagrania.

## Instalacja

Wklej to swojemu agentowi:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Albo ręcznie - skill to po prostu folder:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # utwórz klucz na https://equalang.com/api-keys
```

Jako wtyczka Claude Code: `/plugin marketplace add equalang/equalang-skill`, a potem `/plugin install equalang@equalang`.

Wystarczy `python3` (3.8+); nie trzeba niczego instalować przez `pip install`.

## Co uruchamia agent

```bash
python3 scripts/equalang.py estimate report.pdf                  # ile to będzie kosztować? (bezpłatne)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # wynik trafia obok pliku źródłowego
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # jeden długi tekst, dzielony na zdania przez Equalang
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Języki.** Kody wyglądają tak: `en`, `zh-CN`, `ja`. W skillu nie ma wbudowanej listy: `languages` odczytuje kody i nazwy z działającego API (`--kind text` dla szerszego zestawu, który przyjmuje `text`), więc język dodany przez Equalang jest dostępny bez aktualizacji.

**Kredyty.** Praca zużywa kredyty konta, to samo saldo co na stronie. SKILL.md każe agentowi najpierw podać koszt - z `estimate` - i uzyskać zgodę.

Każde polecenie wypisuje jeden obiekt JSON - ścieżki i kredyty, nigdy zawartość plików - albo `{"error", "code", "retryable"}` z kodem wyjścia 1. [SKILL.md](../SKILL.md) to plik, który czyta agent.

## Jak to jest zbudowane

Te same trzy decyzje co w [serwerze MCP](https://github.com/equalang/equalang-mcp), który udostępnia te same operacje jako narzędzia:

1. **Plik nigdy nie przechodzi przez model** - polecenia przyjmują to, gdzie plik się znajduje (ścieżkę albo publiczny URL, który Equalang pobiera sam), i wypisują, gdzie zapisano wyniki.
2. **Zadanie żyje w obrębie jednego polecenia** - przesłanie, oczekiwanie (z przerwami tak długimi, jak każe `Retry-After` z API), pobranie. Przerwanie oczekiwania nie anuluje zadania; `status` do niego wraca.
3. **Odpowiedzi API są powtarzane, a nie zgadywane** - ponawiaj tylko to, co API oznacza jako `retryable`; koszt to `quote` z API; lista języków jest odczytywana z jego dokumentu OpenAPI; jeden `Idempotency-Key` na każde tworzone zadanie, więc utracona odpowiedź nie zamieni się w drugie, płatne zadanie.

`python3 scripts/check_api.py` sprawdza, bez klucza, czy każda ścieżka i każde pole używane przez skrypt - oraz każdy format obiecany w SKILL.md - nadal są w kontrakcie API. Samo API: <https://equalang.com/llms.txt>.

Apache-2.0.
