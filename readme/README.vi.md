# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · **Tiếng Việt** · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Trang web](https://equalang.com) · [Bảng giá](https://equalang.com/pricing) · [Tài liệu cho nhà phát triển](https://equalang.com/developers) · [Khóa API](https://equalang.com/api-keys)

> **Từ khóa:** dịch tài liệu, dịch pdf, dịch pdf giữ nguyên định dạng, dịch file word, dịch file docx, dịch powerpoint, dịch file excel, dịch epub, dịch phụ đề, dịch file srt, dịch chữ trong ảnh, dịch video, chuyển giọng nói thành văn bản, chép lời ghi âm, dịch bằng ai, api dịch thuật, agent skill, claude code skill, codex skill, translation api

**Dịch tệp, giữ nguyên bố cục.** Một [Agent Skill](https://agentskills.io) cho [Equalang](https://equalang.com) - trình dịch AI làm việc trên trọn tệp: PDF trả về vẫn là PDF, bản trình chiếu vẫn là bản trình chiếu, bảng, hình ảnh và công thức nằm nguyên chỗ cũ. Nó còn dịch phụ đề và hình ảnh, biến âm thanh và video thành phụ đề đã dịch hoặc bản chép lời, và dịch hàng loạt văn bản ngắn. Dùng được trong Claude Code, Codex, Cursor, CodeBuddy và mọi agent khác có tải Agent Skills.

## Thử nói thế này

- “Dịch ~/Documents/contract.pdf sang tiếng Việt, giữ nguyên bố cục.”
- “Dịch pitch-deck.pptx sang tiếng Anh và tiếng Nhật.”
- “Dịch https://example.com/whitepaper.pdf sang tiếng Việt rồi lưu vào ~/Downloads.”
- “Dịch thesis.docx sang tiếng Anh thì tốn bao nhiêu?”
- “Làm phụ đề tiếng Việt cho interview.mp4, giữ dòng gốc phía trên mỗi dòng dịch.”
- “Chép lời standup.m4a kèm mốc thời gian.”
- “Dịch chữ trong menu.jpg sang tiếng Việt.”
- “Dịch các chuỗi trong locales/en.json sang tiếng Hàn, tiếng Nhật và tiếng Thái.”

## Tính năng

- **Tài liệu** - PDF, DOCX, PPTX, XLSX, EPUB, HTML và TXT trả về đúng định dạng cũ, vẫn chỉnh sửa được, bảng, hình ảnh, công thức và bố cục trang giữ nguyên
- **Phụ đề và hình ảnh** - SRT và VTT giữ nguyên mốc thời gian, tùy chọn kèm dòng gốc phía trên bản dịch; JPG, PNG, WebP và BMP trả về với phần chữ trong ảnh đã được dịch
- **Âm thanh và video** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM và MKV trở thành phụ đề đã dịch, hoặc bản chép lời bằng chính ngôn ngữ được nói (SRT, VTT, TXT, JSON)
- **Văn bản hàng loạt** - các văn bản ngắn được dịch theo đúng thứ tự, hoặc một văn bản dài (tối đa 100,000 ký tự) do Equalang tự cắt theo câu
- **Ngôn ngữ** - hơn 100 cho văn bản và 12 cho tệp, tự động phát hiện ngôn ngữ nguồn khi bạn bỏ trống

## Lấy khóa

Đăng ký tại <https://equalang.com> và tạo khóa tại <https://equalang.com/api-keys>. Tài khoản mới có sẵn credit miễn phí, đủ để dịch thử một tài liệu.

Lưu khóa một lần vào `~/.config/equalang/.env` là dùng được mãi: trong mọi agent - Claude Code, Codex, WorkBuddy, Cursor hay agent khác - ở mọi phiên mới, kể cả sau khi cài lại hay cập nhật, không cần export. Máy chủ MCP của Equalang cũng đọc chính tệp này.

```bash
# Thay el_your_key bằng khóa của bạn
mkdir -p ~/.config/equalang && echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env && chmod 600 ~/.config/equalang/.env
```

Biến môi trường `EQUALANG_API_KEY` được xem trước; chỉ khi không có mới đọc tệp này - nhờ vậy một dự án có thể dùng khóa khác.

## Cài đặt

Cần `python3` 3.8 trở lên, và không cần gì khác: script chỉ dùng thư viện chuẩn.

Cách ngắn nhất - dán câu này cho agent của bạn:

> Cài đặt skill Equalang bằng cách làm theo hướng dẫn tại https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (thủ công)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Chỉ muốn dùng trong một dự án? Clone vào `.claude/skills/equalang` trong repository.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex cũng đọc `.agents/skills/` bên trong repository, để giới hạn skill trong một dự án.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Theo từng dự án: clone vào `.codebuddy/skills/equalang` ở thư mục gốc của dự án.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro và các client khác</b></summary>

Đây là một [Agent Skill](https://agentskills.io) thuần túy: một thư mục có tệp `SKILL.md` bên trong. Mọi client triển khai chuẩn này đều tải cùng thư mục đó - chỉ khác ở thư mục mà nó quét, và mỗi client có tài liệu riêng về điều này. Clone repository vào thư mục ấy là skill đã được cài.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Thích máy chủ MCP hơn? [equalang-mcp](https://github.com/equalang/equalang-mcp) cung cấp cùng các thao tác dưới dạng công cụ, và dùng được cả trong Claude Desktop, Cursor, Windsurf, Cline và OpenCode.

## Lệnh

```bash
# Sẽ tốn bao nhiêu? Miễn phí, và chưa dịch gì cả
python3 scripts/equalang.py estimate report.pdf

# Dịch một tệp; kết quả nằm ngay cạnh tệp nguồn
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Từ một URL công khai (Equalang tự tải), lưu vào một thư mục
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Bản ghi âm nói gì, dưới dạng văn bản có mốc thời gian
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Các văn bản ngắn, theo đúng thứ tự
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Một văn bản dài, Equalang tự cắt theo câu
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Tác vụ còn đang chạy, số dư, và mã ngôn ngữ
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Mỗi lệnh đều in ra JSON: tệp được ghi ở đâu và tốn bao nhiêu, hoặc có gì trục trặc. Thêm `--help` vào bất kỳ lệnh nào để xem các cờ của nó. [SKILL.md](../SKILL.md) là thứ agent tự đọc.

Mã ngôn ngữ có dạng `en`, `zh-CN`, `ja`. Chạy `languages` để xem toàn bộ, hoặc `languages chinese` để tìm. Tác vụ mất vài phút - lệnh sẽ chờ, và `status <job_id>` tiếp tục theo dõi nó nếu bạn ngắt giữa chừng.

## Liên kết

- [Equalang](https://equalang.com) · [Bảng giá](https://equalang.com/pricing) · [Tài liệu cho nhà phát triển](https://equalang.com/developers)
- API dành cho agent: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - cùng các thao tác, dưới dạng máy chủ MCP
- Thắc mắc: <support@equalang.com>

## Giấy phép

[Apache-2.0](../LICENSE) © Equalang
