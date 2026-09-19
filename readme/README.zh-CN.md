# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · **简体中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[官网](https://equalang.com) · [价格](https://equalang.com/pricing) · [开发者文档](https://equalang.com/developers) · [API 密钥](https://equalang.com/api-keys)

> **关键词：** 文档翻译、PDF翻译、PDF翻译保留排版、文档翻译保留格式、Word文档翻译、PPT翻译、Excel翻译、EPUB电子书翻译、论文翻译、字幕翻译、SRT字幕翻译、图片翻译、视频翻译、音频转文字、语音转文字、AI翻译、agent skill、claude code skill、codex skill、translation api

**翻译文件，版式不变。** 这是 [Equalang](https://equalang.com) 的 [Agent Skill](https://agentskills.io)。Equalang 是一款整份文件直接翻译的 AI 翻译工具：PDF 进去，PDF 出来；演示文稿进去，演示文稿出来，表格、图片和公式都在原位。它还能翻译字幕和图片，把音频和视频变成翻译好的字幕或转写文本，并批量翻译字符串。可用于 Claude Code、Codex、Cursor、CodeBuddy，以及其他所有能加载 Agent Skills 的智能体。

## 功能

- **什么格式进，什么格式出**：PDF、DOCX、PPTX、XLSX、EPUB、HTML 和 TXT 译完仍是原格式，依然可编辑，表格、图片、公式和页面版式都在原位
- **字幕和图片**：SRT 和 VTT 保留时间轴，还可以选择把原文放在译文上方；JPG、PNG、WebP 和 BMP 返回时，图中的文字已经译好
- **音频和视频**：MP3、M4A、WAV、FLAC、OGG、AAC、Opus、MP4、MOV、WebM 和 MKV 可变成翻译好的字幕，或原语言的转写文本（SRT、VTT、TXT、JSON）
- **批量文本**：多条独立的字符串按顺序翻译，或一整篇长文本（最多 100,000 字符），由 Equalang 自行按句切分；文本支持 100+ 种语言，文件支持 12 种
- **整份文件，不用粘贴**：单个文件最大 100 MB，来自路径或公开 URL；不必拆开了往文本框里贴
- **不花 token**：文件交给 Equalang，回来的是一个路径；一份 300 页的 PDF 从头到尾不进入对话
- **先报价，再开工**：`estimate` 免费告诉你一个任务最多要花多少；失败和取消的任务不收费；录音按实际听到的语音计费；积分永不过期
- **无需安装任何东西**：一个 Python 脚本，只用标准库，Python 3.8+

## 获取密钥

在 <https://equalang.com> 注册，然后在 <https://equalang.com/api-keys> 创建密钥。新账户自带免费积分——足够翻一份文档，看看效果如何。

```bash
export EQUALANG_API_KEY=el_your_key
```

也可以把本目录下的 `.env.example` 复制为 `.env`——它已被 git 忽略。密钥只显示一次；Equalang 只保存它的哈希值。

## 安装

最省事的办法——把这句话粘贴给你的智能体：

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b>（插件）</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b>（手动）</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

只想在某个项目里用？克隆到该仓库的 `.claude/skills/equalang`。
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex 也会读取仓库内的 `.agents/skills/`，可以借此把技能限定在单个项目。
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

项目级安装：克隆到项目根目录的 `.codebuddy/skills/equalang`。
</details>

<details>
<summary><b>Cursor、Gemini CLI、OpenCode、Copilot、Goose、Amp、Kiro 等</b></summary>

这是一个标准的 [Agent Skill](https://agentskills.io)：一个文件夹，里面有一份 `SKILL.md`。凡是实现了该标准的客户端，加载的都是同一个文件夹——区别只在于各自扫描的目录，具体位置见各客户端的文档。把仓库克隆到那个目录，技能就装好了。

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

更想用 MCP 服务器？[equalang-mcp](https://github.com/equalang/equalang-mcp) 以工具的形式提供同样的操作，还支持 Claude Desktop、Cursor、Windsurf、Cline 和 OpenCode。

## 命令

```bash
# 要花多少？免费，且不会启动任何任务
python3 scripts/equalang.py estimate report.pdf

# 翻译一个文件；结果保存在源文件旁边
python3 scripts/equalang.py translate report.pdf --to zh-CN

# 来自公开 URL（由 Equalang 自己抓取），保存到指定文件夹
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# 录音里说了什么，写成带时间轴的文本
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# 多条独立的字符串，按顺序翻译
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# 一整篇长文本，由 Equalang 按句切分
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# 还在运行的任务、余额，以及语言代码
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

每条命令输出一个 JSON 对象——只有路径和积分，绝不含文件内容——或者输出 `{"error", "code", "retryable"}` 并以退出码 1 结束。任何命令加上 `--help` 都会列出它的参数。[SKILL.md](../SKILL.md) 是智能体读的那份文件。

## 值得知道的三件事

**语言。** 代码形如 `en`、`zh-CN`、`ja`。技能不内置语言列表：`languages` 从线上 API 读取代码和名称（用 `--kind text` 查看 `text` 支持的更大集合），所以 Equalang 新增的语言无需更新即可使用。不填源语言则自动检测。

**积分。** 任务消耗账户的积分，与网站是同一个余额。SKILL.md 要求智能体在启动任务前先报出费用（来自 `estimate`）并征得同意。

**任务要跑几分钟。** 命令会一直等，每次暂停的时长按 API 的 `Retry-After` 来。中断命令不会取消任务——用 `status <job_id>` 可以重新接上，并下载结果。

## 常见问题

**翻译后的 PDF 还保留原来的排版吗？**
保留——这正是它的意义所在。文字放回原来的位置，表格、图片和公式原地不动；DOCX、PPTX 和 XLSX 仍可编辑。

**我的文档会被发给模型吗？**
不会。脚本把文件上传到 Equalang，然后输出一个路径。一篇 300 页的论文不花一个 token。

**能翻译图片里的文字吗？**
能。JPG、PNG、WebP 或 BMP 中的文字会被识别、翻译，再画回图片里。

**一个任务要花多少？**
`estimate` 会在任何任务开始之前告诉你，而且免费。价格见 <https://equalang.com/pricing>。

## 设计思路

与 [MCP 服务器](https://github.com/equalang/equalang-mcp)相同的三个决定：

1. **文件从不经过模型**：命令接收的是文件在哪里（路径，或由 Equalang 自己抓取的公开 URL），输出的是结果写到了哪里。
2. **一个任务活在一条命令里**：上传、等待、下载。等待被中断的任务，用 `status` 可以重新接上。
3. **API 的回答是转述的，不是猜的**：只重试 API 标为 `retryable` 的失败；费用是 API 的 `quote`；语言列表读自它的 OpenAPI 文档；每个创建的任务对应一个 `Idempotency-Key`，所以一次丢失的响应不会变成第二个被计费的任务。

`python3 scripts/check_api.py` 无需密钥即可验证：脚本用到的每个路径和字段，以及 SKILL.md 承诺的每种格式，仍在 API 的契约里。

## 链接

- [Equalang](https://equalang.com) · [价格](https://equalang.com/pricing) · [开发者文档](https://equalang.com/developers)
- 面向智能体的 API：[llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp)：同样的操作，以 MCP 服务器的形式提供
- 有问题：<support@equalang.com>

## 许可证

[Apache-2.0](../LICENSE) © Equalang
