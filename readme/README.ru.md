# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · **Русский** · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Сайт](https://equalang.com) · [Цены](https://equalang.com/pricing) · [Документация для разработчиков](https://equalang.com/developers) · [API-ключи](https://equalang.com/api-keys)

> **Ключевые слова:** перевод документов, переводчик документов, перевод pdf, переводчик pdf, перевод pdf с сохранением форматирования, перевод word, перевод презентации pptx, перевод excel, перевод epub, перевод субтитров, перевод srt, перевод текста на картинке, перевод видео, расшифровка аудио, аудио в текст, нейросеть переводчик, agent skill, claude code skill, codex skill, translation api

**Переводите файл — вёрстка остаётся.** [Agent Skill](https://agentskills.io) для [Equalang](https://equalang.com) — ИИ-переводчика, который работает с файлами целиком: PDF возвращается как PDF, презентация — как презентация, а таблицы, изображения и формулы остаются на своих местах. Он также переводит субтитры и картинки, превращает аудио и видео в переведённые субтитры или расшифровку и пакетно переводит короткие тексты. Работает в Claude Code, Codex, Cursor, CodeBuddy и любом другом агенте, который загружает Agent Skills.

## Возможности

- **Документы** — PDF, DOCX, PPTX, XLSX, EPUB, HTML и TXT возвращаются в том же формате, остаются редактируемыми, а таблицы, изображения, формулы и вёрстка страниц — на месте
- **Субтитры и картинки** — SRT и VTT сохраняют тайминг, при желании с исходной строкой над переводом; JPG, PNG, WebP и BMP возвращаются с переведённым текстом прямо на картинке
- **Аудио и видео** — MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM и MKV превращаются в переведённые субтитры или в расшифровку на языке оригинала (SRT, VTT, TXT, JSON)
- **Текст пакетом** — короткие тексты переводятся с сохранением порядка, либо один длинный текст (до 100 000 символов), который Equalang сам делит по предложениям
- **Языки** — 100+ для текста и 12 для файлов, причём исходный язык определяется автоматически, если его не указать

## Получите ключ

Зарегистрируйтесь на <https://equalang.com> и создайте ключ на <https://equalang.com/api-keys>. Новые аккаунты получают бесплатные кредиты — их хватит, чтобы попробовать на одном документе.

Сохраните его один раз на компьютер в `~/.config/equalang/.env`: этот скилл и MCP-сервер Equalang читают его оттуда, и файл остаётся на месте при переустановке или обновлении любого из них.

```bash
mkdir -p ~/.config/equalang
echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env
chmod 600 ~/.config/equalang/.env
```

Переменная окружения `EQUALANG_API_KEY` имеет приоритет — так можно задать другой ключ для отдельного проекта.

## Установка

Нужен `python3` 3.8 или новее, и больше ничего: скрипт использует только стандартную библиотеку.

Самый короткий путь — вставьте это своему агенту:

> Установите скилл Equalang, следуя инструкциям на https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (плагин)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (вручную)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Нужен только в одном проекте? Клонируйте в `.claude/skills/equalang` внутри репозитория.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex также читает `.agents/skills/` внутри репозитория — так скилл можно ограничить одним проектом.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Для одного проекта: клонируйте в `.codebuddy/skills/equalang` в корне проекта.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro и другие</b></summary>

Это обычный [Agent Skill](https://agentskills.io): папка, в которой лежит `SKILL.md`. Любой клиент, реализующий стандарт, загружает одну и ту же папку — различается только каталог, который он просматривает, и у каждого клиента он описан в документации. Клонируйте репозиторий в этот каталог — и скилл установлен.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Предпочитаете MCP-сервер? [equalang-mcp](https://github.com/equalang/equalang-mcp) предлагает те же операции в виде инструментов и работает ещё и в Claude Desktop, Cursor, Windsurf, Cline и OpenCode.

## Команды

```bash
# Сколько это будет стоить? Бесплатно, и перевод не начинается
python3 scripts/equalang.py estimate report.pdf

# Перевести файл; результат появится рядом с исходником
python3 scripts/equalang.py translate report.pdf --to zh-CN

# По публичному URL (Equalang скачивает его сам), в папку
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Что говорится в записи — текстом с таймкодами
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Короткие тексты, с сохранением порядка
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Один длинный текст, Equalang делит его по предложениям
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Оставленное в работе задание, баланс и коды языков
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Каждая команда печатает JSON: куда записаны файлы и сколько это стоило — или что пошло не так. Добавьте `--help` к любой команде, чтобы увидеть её флаги. [SKILL.md](../SKILL.md) — это то, что читает агент.

Коды языков выглядят так: `en`, `zh-CN`, `ja`. Выполните `languages`, чтобы увидеть список, или `languages chinese`, чтобы найти нужный. Задания занимают минуты — команда ждёт, а если её прервать, `status <job_id>` возвращается к заданию.

## Ссылки

- [Equalang](https://equalang.com) · [Цены](https://equalang.com/pricing) · [Документация для разработчиков](https://equalang.com/developers)
- API для агентов: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) — те же операции в виде MCP-сервера
- Вопросы: <support@equalang.com>

## Лицензия

[Apache-2.0](../LICENSE) © Equalang
