# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · **Русский** · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Сайт](https://equalang.com) · [Цены](https://equalang.com/pricing) · [Документация для разработчиков](https://equalang.com/developers) · [API-ключи](https://equalang.com/api-keys)

> **Ключевые слова:** перевод документов, переводчик документов, перевод pdf, переводчик pdf, перевод pdf с сохранением форматирования, перевод word, перевод презентации pptx, перевод excel, перевод epub, перевод субтитров, перевод srt, перевод текста на картинке, перевод видео, расшифровка аудио, аудио в текст, нейросеть переводчик, agent skill, claude code skill, codex skill, translation api

**Переводите файл — вёрстка остаётся.** [Agent Skill](https://agentskills.io) для [Equalang](https://equalang.com) — ИИ-переводчика, который работает с файлами целиком: PDF возвращается как PDF, презентация — как презентация, а таблицы, изображения и формулы остаются на своих местах. Он также переводит субтитры и картинки, превращает аудио и видео в переведённые субтитры или расшифровку и пакетно переводит строки. Работает в Claude Code, Codex, Cursor, CodeBuddy и любом другом агенте, который загружает Agent Skills.

## Возможности

- **Какой формат пришёл, такой и вернулся** — PDF, DOCX, PPTX, XLSX, EPUB, HTML и TXT возвращаются в том же формате, остаются редактируемыми, а таблицы, изображения, формулы и вёрстка страниц — на месте
- **Субтитры и картинки** — SRT и VTT сохраняют тайминг, при желании с исходной строкой над переводом; JPG, PNG, WebP и BMP возвращаются с переведённым текстом прямо на картинке
- **Аудио и видео** — MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM и MKV превращаются в переведённые субтитры или в расшифровку на языке оригинала (SRT, VTT, TXT, JSON)
- **Текст пакетом** — отдельные строки переводятся с сохранением порядка, либо один длинный текст (до 100 000 символов), который Equalang сам делит по предложениям; 100+ языков для текста, 12 для файлов
- **Файлы целиком, без копирования** — до 100 MB на файл, по пути или публичному URL; ничего не нужно резать на куски и вставлять в текстовые поля
- **Не тратит токены** — файл уходит в Equalang, обратно приходит путь; PDF на 300 страниц в диалог не попадает
- **Цена до запуска** — `estimate` бесплатно называет максимальную стоимость задания; за неудавшиеся и отменённые задания ничего не списывается; за запись списывается только реально услышанная речь; кредиты не сгорают
- **Ничего не нужно устанавливать** — один скрипт на Python, только стандартная библиотека, Python 3.8+

## Получите ключ

Зарегистрируйтесь на <https://equalang.com> и создайте ключ на <https://equalang.com/api-keys>. Новые аккаунты получают бесплатные кредиты — их хватит, чтобы прогнать документ и посмотреть, что вернётся.

```bash
export EQUALANG_API_KEY=el_your_key
```

Или скопируйте `.env.example` в `.env` в этом каталоге — он в gitignore. Ключ показывается один раз; Equalang хранит только его хеш.

## Установка

Самый короткий путь — вставьте это своему агенту:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# Сколько это будет стоить? Бесплатно, и ничего не запускается
python3 scripts/equalang.py estimate report.pdf

# Перевести файл; результат появится рядом с исходником
python3 scripts/equalang.py translate report.pdf --to zh-CN

# По публичному URL (Equalang скачивает его сам), в папку
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Что говорится в записи — текстом с таймкодами
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Отдельные строки, с сохранением порядка
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Один длинный текст, Equalang делит его по предложениям
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Оставленное в работе задание, баланс и коды языков
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Каждая команда печатает один JSON-объект — пути и кредиты, но никогда не содержимое файлов — либо `{"error", "code", "retryable"}` с кодом выхода 1. `--help` у любой команды перечисляет её флаги. [SKILL.md](../SKILL.md) — это то, что читает агент.

## Три вещи, которые стоит знать

**Языки.** Коды выглядят так: `en`, `zh-CN`, `ja`. Списка в самом скилле нет: `languages` читает коды и названия из работающего API (`--kind text` — для более широкого набора, который принимает `text`), поэтому язык, добавленный в Equalang, доступен без обновления. Не указывайте исходный язык, чтобы он определился автоматически.

**Кредиты.** Работа расходует кредиты аккаунта — тот же баланс, что и на сайте. SKILL.md требует, чтобы агент назвал стоимость — из `estimate` — и получил согласие, прежде чем запускать задание.

**Задания занимают минуты.** Команда ждёт, делая паузы такой длины, какую просит `Retry-After` из API. Прерывание команды не отменяет задание — `status <job_id>` возвращается к нему и скачивает результат.

## Частые вопросы

**Сохраняется ли вёрстка в переведённом PDF?**
Да — в этом весь смысл. Текст возвращается туда, где он был, а таблицы, изображения и формулы остаются на месте; DOCX, PPTX и XLSX остаются редактируемыми.

**Мой документ отправляется в модель?**
Нет. Скрипт загружает файл в Equalang и печатает путь. Статья на 300 страниц не стоит ни одного токена.

**Может ли он перевести текст на картинке?**
Да. Текст в JPG, PNG, WebP или BMP распознаётся, переводится и отрисовывается обратно на картинке.

**Сколько стоит задание?**
`estimate` скажет об этом до запуска чего-либо, и это бесплатно. Цены — на <https://equalang.com/pricing>.

## Как это устроено

Те же три решения, что и в [MCP-сервере](https://github.com/equalang/equalang-mcp):

1. **Файл никогда не проходит через модель** — команды принимают то, где лежит файл (путь или публичный URL, который Equalang скачивает сам), и печатают, куда записаны результаты.
2. **Задание живёт внутри одной команды** — загрузка, ожидание, скачивание. `status` возвращается к заданию, ожидание которого было прервано.
3. **Ответы API повторяются, а не угадываются** — повторяется только то, что API помечает как `retryable`; стоимость — это `quote` из API; список языков читается из его OpenAPI-документа; один `Idempotency-Key` на каждое создаваемое задание, поэтому потерянный ответ не превратится во второе, оплаченное задание.

`python3 scripts/check_api.py` проверяет, без ключа, что каждый путь и каждое поле, которые использует скрипт, — и каждый формат, обещанный в SKILL.md, — по-прежнему есть в контракте API.

## Ссылки

- [Equalang](https://equalang.com) · [Цены](https://equalang.com/pricing) · [Документация для разработчиков](https://equalang.com/developers)
- API для агентов: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) — те же операции в виде MCP-сервера
- Вопросы: <support@equalang.com>

## Лицензия

[Apache-2.0](../LICENSE) © Equalang
