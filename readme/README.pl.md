# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · **Polski** · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Strona](https://equalang.com) · [Cennik](https://equalang.com/pricing) · [Dokumentacja dla programistów](https://equalang.com/developers) · [Klucze API](https://equalang.com/api-keys)

> **Słowa kluczowe:** tłumaczenie dokumentów, tłumacz dokumentów, tłumaczenie pdf, tłumacz pdf, tłumaczenie pdf z zachowaniem formatowania, tłumaczenie plików word, tłumaczenie prezentacji powerpoint, tłumaczenie excel, tłumaczenie epub, tłumaczenie napisów, tłumaczenie napisów srt, tłumaczenie tekstu ze zdjęcia, tłumaczenie filmów, transkrypcja nagrań, zamiana mowy na tekst, tłumacz ai, agent skill, claude code skill, codex skill, translation api

**Przetłumacz plik, zachowaj układ.** [Agent Skill](https://agentskills.io) dla [Equalang](https://equalang.com) – tłumacza AI, który pracuje na całych plikach: PDF wraca jako PDF, prezentacja jako prezentacja, a tabele, obrazy i wzory zostają tam, gdzie były. Tłumaczy też napisy i obrazy, zamienia audio i wideo w przetłumaczone napisy albo transkrypcję i hurtowo tłumaczy teksty. Działa w Claude Code, Codex, Cursor, CodeBuddy i każdym innym agencie, który ładuje Agent Skills.

## Funkcje

- **Ten sam format na wejściu i na wyjściu** – PDF, DOCX, PPTX, XLSX, EPUB, HTML i TXT wracają w tym samym formacie, nadal edytowalne, z tabelami, obrazami, wzorami i układem strony na swoich miejscach
- **Napisy i obrazy** – SRT i VTT zachowują znaczniki czasu, opcjonalnie z oryginalną linią nad tłumaczeniem; JPG, PNG, WebP i BMP wracają z przetłumaczonym tekstem na obrazie
- **Audio i wideo** – MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM i MKV stają się przetłumaczonymi napisami albo transkrypcją w języku nagrania (SRT, VTT, TXT, JSON)
- **Teksty hurtowo** – osobne ciągi znaków tłumaczone po kolei albo jeden długi tekst (do 100 000 znaków), który Equalang sam dzieli na zdania; ponad 100 języków dla tekstu, 12 dla plików
- **Całe pliki, bez wklejania** – do 100 MB na plik, ze ścieżki lub publicznego URL; niczego nie trzeba dzielić na kawałki i wklejać w pola tekstowe
- **Nie kosztuje tokenów** – plik trafia do Equalang, a wraca ścieżka; 300-stronicowy PDF nigdy nie trafia do rozmowy
- **Cena przed zadaniem** – `estimate` podaje, za darmo, maksymalny koszt zadania; zadania nieudane i anulowane nic nie kosztują; za nagranie płaci się tylko za faktycznie usłyszaną mowę; kredyty nigdy nie wygasają
- **Nic do instalowania** – jeden skrypt w Pythonie, tylko biblioteka standardowa, Python 3.8+

## Zdobądź klucz

Zarejestruj się na <https://equalang.com> i utwórz klucz na <https://equalang.com/api-keys>. Nowe konta zaczynają z darmowymi kredytami – wystarczy, żeby przepuścić dokument i zobaczyć, co wróci.

```bash
export EQUALANG_API_KEY=el_your_key
```

Albo skopiuj `.env.example` do `.env` w tym katalogu – plik jest ignorowany przez git. Klucz jest pokazywany tylko raz; Equalang przechowuje wyłącznie jego hash.

## Instalacja

Najkrótsza droga – wklej to swojemu agentowi:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (wtyczka)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (ręcznie)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Tylko dla jednego projektu? Sklonuj do `.claude/skills/equalang` w repozytorium.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex czyta też `.agents/skills/` wewnątrz repozytorium, co pozwala ograniczyć skill do jednego projektu.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Dla jednego projektu: sklonuj do `.codebuddy/skills/equalang` w katalogu głównym projektu.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro i inne</b></summary>

To zwykły [Agent Skill](https://agentskills.io): folder z plikiem `SKILL.md` w środku. Każdy klient, który implementuje ten standard, ładuje ten sam folder – różni się tylko katalog, który przeszukuje, a każdy klient opisuje go w swojej dokumentacji. Sklonuj repozytorium do tego katalogu i skill jest zainstalowany.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Wolisz serwer MCP? [equalang-mcp](https://github.com/equalang/equalang-mcp) udostępnia te same operacje jako narzędzia i działa także w Claude Desktop, Cursor, Windsurf, Cline i OpenCode.

## Polecenia

```bash
# Ile by to kosztowało? Za darmo, nic nie jest uruchamiane
python3 scripts/equalang.py estimate report.pdf

# Przetłumacz plik; wynik ląduje obok oryginału
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Z publicznego URL (Equalang pobiera go sam), do folderu
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Co pada w nagraniu, jako tekst ze znacznikami czasu
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Osobne ciągi znaków, po kolei
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Jeden długi tekst, dzielony na zdania przez Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Zadanie pozostawione w toku, saldo i kody języków
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Każde polecenie wypisuje jeden obiekt JSON – ścieżki i kredyty, nigdy zawartość plików – albo `{"error", "code", "retryable"}` z kodem wyjścia 1. `--help` przy dowolnym poleceniu wyświetla jego flagi. [SKILL.md](../SKILL.md) to plik, który czyta agent.

## Trzy rzeczy, które warto wiedzieć

**Języki.** Kody wyglądają tak: `en`, `zh-CN`, `ja`. W skillu nie ma wbudowanej listy: `languages` odczytuje kody i nazwy z działającego API (`--kind text` dla szerszego zestawu, który przyjmuje `text`), więc język dodany przez Equalang jest dostępny bez aktualizacji. Pomiń język źródłowy, aby został wykryty automatycznie.

**Kredyty.** Praca zużywa kredyty konta, to samo saldo co na stronie. SKILL.md każe agentowi podać koszt – z `estimate` – i uzyskać zgodę, zanim uruchomi zadanie.

**Zadania trwają minuty.** Polecenie czeka, robiąc przerwy tak długie, jak każe `Retry-After` z API. Przerwanie go nie anuluje zadania – `status <job_id>` wraca do niego i pobiera wynik.

## Częste pytania

**Czy przetłumaczony PDF zachowuje układ?**
Tak – właśnie o to chodzi. Tekst wraca tam, gdzie był, a tabele, obrazy i wzory zostają na miejscu; DOCX, PPTX i XLSX pozostają edytowalne.

**Czy mój dokument jest wysyłany do modelu?**
Nie. Skrypt przesyła plik do Equalang i wypisuje ścieżkę. 300-stronicowa praca nie kosztuje żadnych tokenów.

**Czy potrafi przetłumaczyć tekst na obrazie?**
Tak. Tekst w pliku JPG, PNG, WebP lub BMP jest rozpoznawany, tłumaczony i nanoszony z powrotem na obraz.

**Ile kosztuje zadanie?**
`estimate` podaje koszt, zanim cokolwiek ruszy, i jest bezpłatne. Cennik: <https://equalang.com/pricing>.

## Jak to jest zbudowane

Te same trzy decyzje co w [serwerze MCP](https://github.com/equalang/equalang-mcp):

1. **Plik nigdy nie przechodzi przez model** – polecenia przyjmują to, gdzie plik się znajduje (ścieżkę albo publiczny URL, który Equalang pobiera sam), i wypisują, gdzie zapisano wyniki.
2. **Zadanie żyje w obrębie jednego polecenia** – przesłanie, oczekiwanie, pobranie. `status` wraca do zadania, na które oczekiwanie zostało przerwane.
3. **Odpowiedzi API są powtarzane, a nie zgadywane** – ponawiane jest tylko to, co API oznacza jako `retryable`; koszt to `quote` z API; lista języków jest odczytywana z jego dokumentu OpenAPI; jeden `Idempotency-Key` na każde tworzone zadanie, więc utracona odpowiedź nie zamieni się w drugie, płatne zadanie.

`python3 scripts/check_api.py` sprawdza, bez klucza, czy każda ścieżka i każde pole używane przez skrypt – oraz każdy format obiecany w SKILL.md – nadal są w kontrakcie API.

## Linki

- [Equalang](https://equalang.com) · [Cennik](https://equalang.com/pricing) · [Dokumentacja dla programistów](https://equalang.com/developers)
- API dla agentów: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) – te same operacje jako serwer MCP
- Pytania: <support@equalang.com>

## Licencja

[Apache-2.0](../LICENSE) © Equalang
