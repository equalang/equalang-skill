# Skill Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · **Tiếng Việt** · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Một [Agent Skill](https://github.com/anthropics/skills) trao [Equalang](https://equalang.com) cho Claude Code, Codex, Cursor và các agent khác: dịch trọn tệp mà vẫn giữ bố cục, chép lời bản ghi âm, dịch hàng loạt chuỗi văn bản.

- **Tài liệu** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - trả về đúng định dạng cũ.
- **Phụ đề** (SRT, VTT) và **hình ảnh** (JPG, PNG, WebP, BMP).
- **Âm thanh và video** trả về dưới dạng phụ đề đã dịch, hoặc bản chép lời bằng chính ngôn ngữ được nói.

## Cài đặt

Dán câu này cho agent của bạn:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Hoặc làm thủ công - một skill chỉ là một thư mục:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # tạo khóa tại https://equalang.com/api-keys
```

Dưới dạng plugin Claude Code: `/plugin marketplace add equalang/equalang-skill`, rồi `/plugin install equalang@equalang`.

Chỉ cần `python3` (3.8+); không phải `pip install` gì cả.

## Những gì agent chạy

```bash
python3 scripts/equalang.py estimate report.pdf                  # sẽ tốn bao nhiêu? (miễn phí)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # kết quả nằm ngay cạnh tệp nguồn
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Ngôn ngữ.** Mã có dạng `en`, `zh-CN`, `ja`. Skill không kèm sẵn danh sách nào: `languages` đọc mã và tên từ API đang chạy (`--kind text` cho tập rộng hơn mà `text` nhận), nên ngôn ngữ Equalang mới thêm dùng được ngay mà không cần cập nhật.

**Credit.** Công việc tiêu credit của tài khoản, cùng số dư với trang web. SKILL.md yêu cầu agent nêu chi phí - lấy từ `estimate` - và được đồng ý trước.

Mỗi lệnh in ra một đối tượng JSON - đường dẫn và credit, không bao giờ là nội dung tệp - hoặc `{"error", "code", "retryable"}` với mã thoát 1. [SKILL.md](../SKILL.md) là thứ agent đọc.

## Cách nó được xây dựng

Vẫn ba quyết định như của [máy chủ MCP](https://github.com/equalang/equalang-mcp), nơi cung cấp cùng các thao tác dưới dạng công cụ:

1. **Tệp không bao giờ đi qua mô hình** - lệnh nhận tệp nằm ở đâu (một đường dẫn, hoặc một URL công khai mà Equalang tự tải) và in ra kết quả được ghi ở đâu.
2. **Một tác vụ nằm gọn trong một lệnh** - tải lên, chờ (nghỉ đúng bằng thời gian `Retry-After` của API yêu cầu), tải về. Ngắt việc chờ không hủy tác vụ; `status` sẽ tiếp tục theo dõi nó.
3. **Câu trả lời của API được thuật lại, không phải đoán** - chỉ thử lại những gì API đánh dấu `retryable`; chi phí là `quote` của API; danh sách ngôn ngữ được đọc từ tài liệu OpenAPI của nó; mỗi tác vụ được tạo có một `Idempotency-Key`, nên một câu trả lời bị mất không thể biến thành tác vụ thứ hai bị tính phí.

`python3 scripts/check_api.py` kiểm tra, không cần khóa, rằng mọi đường dẫn và trường mà script dùng - cùng mọi định dạng SKILL.md cam kết - vẫn còn trong hợp đồng của API. Bản thân API: <https://equalang.com/llms.txt>.

Apache-2.0.
