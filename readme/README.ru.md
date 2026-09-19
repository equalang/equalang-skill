# Скилл Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · **Русский** · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Agent Skill](https://github.com/anthropics/skills), который подключает [Equalang](https://equalang.com) к Claude Code, Codex, Cursor и другим агентам: перевод файлов целиком с сохранением вёрстки, расшифровка записей, пакетный перевод строк.

- **Документы** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - возвращаются в том же формате.
- **Субтитры** (SRT, VTT) и **изображения** (JPG, PNG, WebP, BMP).
- **Аудио и видео** возвращаются в виде переведённых субтитров или расшифровки на языке оригинала.

## Установка

Вставьте это своему агенту:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Или вручную - скилл это просто папка:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # создайте ключ на https://equalang.com/api-keys
```

Как плагин Claude Code: `/plugin marketplace add equalang/equalang-skill`, затем `/plugin install equalang@equalang`.

Нужен только `python3` (3.8+); ничего ставить через `pip install` не требуется.

## Что запускает агент

```bash
python3 scripts/equalang.py estimate report.pdf                  # сколько это будет стоить? (бесплатно)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # результат появится рядом с исходником
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # один длинный текст, Equalang делит его по предложениям
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Языки.** Коды выглядят так: `en`, `zh-CN`, `ja`. Списка в самом скилле нет: `languages` читает коды и названия из работающего API (`--kind text` - для более широкого набора, который принимает `text`), поэтому язык, добавленный в Equalang, доступен без обновления.

**Кредиты.** Работа расходует кредиты аккаунта - тот же баланс, что и на сайте. SKILL.md требует, чтобы агент сначала назвал стоимость - из `estimate` - и получил согласие.

Каждая команда печатает один JSON-объект - пути и кредиты, но никогда не содержимое файлов - либо `{"error", "code", "retryable"}` с кодом выхода 1. [SKILL.md](../SKILL.md) - это то, что читает агент.

## Как это устроено

Те же три решения, что и в [MCP-сервере](https://github.com/equalang/equalang-mcp), который предлагает те же операции в виде инструментов:

1. **Файл никогда не проходит через модель** - команды принимают то, где лежит файл (путь или публичный URL, который Equalang скачивает сам), и печатают, куда записаны результаты.
2. **Задание живёт внутри одной команды** - загрузка, ожидание (с паузами такой длины, какую просит `Retry-After` из API), скачивание. Прерывание ожидания не отменяет задание; `status` к нему возвращается.
3. **Ответы API повторяются, а не угадываются** - повторяется только то, что API помечает как `retryable`; стоимость - это `quote` из API; список языков читается из его OpenAPI-документа; один `Idempotency-Key` на каждое создаваемое задание, поэтому потерянный ответ не превратится во второе, оплаченное задание.

`python3 scripts/check_api.py` проверяет, без ключа, что каждый путь и каждое поле, которые использует скрипт, - и каждый формат, обещанный в SKILL.md, - по-прежнему есть в контракте API. Сам API: <https://equalang.com/llms.txt>.

Apache-2.0.
