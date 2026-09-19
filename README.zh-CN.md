# Equalang skill

[English](README.md)

一个 [Agent Skill](https://github.com/anthropics/skills)，让 Claude Code、Codex、Cursor 等 Agent 用上 [Equalang](https://equalang.com)：整份文件翻译并保留版式、音视频转写、批量文本翻译。

- **文档**（PDF、DOCX、PPTX、XLSX、EPUB、HTML、TXT）译完仍是原格式。
- **字幕**（SRT、VTT）和**图片**（JPG、PNG、WebP、BMP）。
- **音频和视频**：得到翻译后的字幕，或原语言的转写稿。

## 安装

把这句话粘贴给你的 Agent：

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

或者手动安装——skill 就是一个文件夹：

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # 在 https://equalang.com/api-keys 创建
```

作为 Claude Code 插件：`/plugin marketplace add equalang/equalang-skill`，再 `/plugin install equalang@equalang`。

只需要 `python3`（3.8+），不用 `pip install` 任何东西。

## Agent 会执行的命令

```bash
python3 scripts/equalang.py estimate report.pdf                  # 先问价（免费）
python3 scripts/equalang.py translate report.pdf --to zh-CN      # 结果存到原文件旁边
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

每条命令输出一个 JSON 对象——路径和积分，从不输出文件内容；失败时输出 `{"error", "code", "retryable"}` 并以 1 退出。Agent 读的是 [SKILL.md](SKILL.md)。

## 设计

与 [MCP 服务器](https://github.com/equalang/equalang-mcp)相同的三条（后者把同样的操作做成工具）：

1. **文件不经过模型**：命令收的是"文件在哪"（路径，或由 Equalang 自己去取的公开 URL），输出的是"结果写到了哪"。
2. **一个任务活在一条命令里**：上传、等待（按 API 的 `Retry-After` 停顿）、下载。中断等待不会取消任务，`status` 可以接着看。
3. **复述 API 的答案，而不是自己猜**：只重试 API 标了 `retryable` 的失败；花费取自 API 的 `quote`；语言列表读自它的 OpenAPI 文档；每个创建任务的请求带一个 `Idempotency-Key`，应答丢失也不会变成第二个被扣费的任务。

`python3 scripts/check_api.py` 无需密钥即可核对：脚本用到的每个路径和字段仍在 API 契约里。API 本身见 <https://equalang.com/llms.txt>。

Apache-2.0。
