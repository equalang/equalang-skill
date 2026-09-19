# Equalang 技能

[English](../README.md) · **简体中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

一个 [Agent Skill](https://github.com/anthropics/skills)，让 Claude Code、Codex、Cursor 等智能体用上 [Equalang](https://equalang.com)：整份文件翻译并保留版式，转写录音，批量翻译文本。

- **文档** - PDF、DOCX、PPTX、XLSX、EPUB、HTML、TXT - 译文保持原格式。
- **字幕**（SRT、VTT）和**图片**（JPG、PNG、WebP、BMP）。
- **音频和视频**返回翻译好的字幕，或原语言的转写文本。

## 安装

把这句话粘贴给你的智能体：

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

或者手动安装 - 技能就是一个文件夹：

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # 在 https://equalang.com/api-keys 创建
```

作为 Claude Code 插件：先 `/plugin marketplace add equalang/equalang-skill`，再 `/plugin install equalang@equalang`。

只需要 `python3`（3.8+）；不用 `pip install` 任何东西。

## 智能体运行的命令

```bash
python3 scripts/equalang.py estimate report.pdf                  # 要花多少？（免费）
python3 scripts/equalang.py translate report.pdf --to zh-CN      # 结果保存在源文件旁边
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # 一整篇长文本，由 Equalang 按句切分
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**语言。** 代码形如 `en`、`zh-CN`、`ja`。技能不内置语言列表：`languages` 从线上 API 读取代码和名称（用 `--kind text` 查看 `text` 支持的更大集合），所以 Equalang 新增的语言无需更新即可使用。

**积分。** 任务消耗账户的积分，与网站是同一个余额。SKILL.md 要求智能体先报出费用 - 来自 `estimate` - 并征得同意。

每条命令输出一个 JSON 对象 - 只有路径和积分，绝不含文件内容 - 或者输出 `{"error", "code", "retryable"}` 并以退出码 1 结束。[SKILL.md](../SKILL.md) 是智能体读的那份文件。

## 设计思路

与 [MCP 服务器](https://github.com/equalang/equalang-mcp)相同的三个决定，后者以工具的形式提供同样的操作：

1. **文件从不经过模型** - 命令接收的是文件在哪里（路径，或由 Equalang 自己抓取的公开 URL），输出的是结果写到了哪里。
2. **一个任务活在一条命令里** - 上传、等待（按 API 的 `Retry-After` 要求的时长暂停）、下载。中断等待不会取消任务；用 `status` 可以重新接上。
3. **API 的回答是转述的，不是猜的** - 只重试 API 标为 `retryable` 的失败；费用是 API 的 `quote`；语言列表读自它的 OpenAPI 文档；每个创建的任务对应一个 `Idempotency-Key`，所以一次丢失的响应不会变成第二个被计费的任务。

`python3 scripts/check_api.py` 无需密钥即可验证：脚本用到的每个路径和字段 - 以及 SKILL.md 承诺的每种格式 - 仍在 API 的契约里。API 本身：<https://equalang.com/llms.txt>。

Apache-2.0。
