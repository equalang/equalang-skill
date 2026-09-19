# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · **Tiếng Việt** · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Trang web](https://equalang.com) · [Bảng giá](https://equalang.com/pricing) · [Tài liệu cho nhà phát triển](https://equalang.com/developers) · [Khóa API](https://equalang.com/api-keys)

> **Từ khóa:** dịch tài liệu, dịch pdf, dịch pdf giữ nguyên định dạng, dịch file word, dịch file docx, dịch powerpoint, dịch file excel, dịch epub, dịch phụ đề, dịch file srt, dịch chữ trong ảnh, dịch video, chuyển giọng nói thành văn bản, chép lời ghi âm, dịch bằng ai, api dịch thuật, agent skill, claude code skill, codex skill, translation api

**Dịch tệp, giữ nguyên bố cục.** Một [Agent Skill](https://agentskills.io) cho [Equalang](https://equalang.com) - trình dịch AI làm việc trên trọn tệp: PDF trả về vẫn là PDF, bản trình chiếu vẫn là bản trình chiếu, bảng, hình ảnh và công thức nằm nguyên chỗ cũ. Nó còn dịch phụ đề và hình ảnh, biến âm thanh và video thành phụ đề đã dịch hoặc bản chép lời, và dịch hàng loạt chuỗi văn bản. Dùng được trong Claude Code, Codex, Cursor, CodeBuddy và mọi agent khác có tải Agent Skills.

## Tính năng

- **Định dạng nào vào, định dạng ấy ra** - PDF, DOCX, PPTX, XLSX, EPUB, HTML và TXT trả về đúng định dạng cũ, vẫn chỉnh sửa được, bảng, hình ảnh, công thức và bố cục trang giữ nguyên
- **Phụ đề và hình ảnh** - SRT và VTT giữ nguyên mốc thời gian, tùy chọn kèm dòng gốc phía trên bản dịch; JPG, PNG, WebP và BMP trả về với phần chữ trong ảnh đã được dịch
- **Âm thanh và video** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM và MKV trở thành phụ đề đã dịch, hoặc bản chép lời bằng chính ngôn ngữ được nói (SRT, VTT, TXT, JSON)
- **Văn bản hàng loạt** - các chuỗi riêng lẻ được dịch theo đúng thứ tự, hoặc một văn bản dài (tối đa 100,000 ký tự) do Equalang tự cắt theo câu; hơn 100 ngôn ngữ cho văn bản, 12 cho tệp
- **Trọn tệp, không cần dán** - tối đa 100 MB mỗi tệp, từ một đường dẫn hoặc URL công khai; không phải chia nhỏ vào các ô văn bản
- **Không tốn token** - tệp đi thẳng đến Equalang và thứ trả về là một đường dẫn; một PDF 300 trang không bao giờ đi vào cuộc hội thoại
- **Biết giá trước khi chạy** - `estimate` cho biết mức tối đa một tác vụ có thể tốn, miễn phí; tác vụ thất bại hoặc bị hủy không mất gì; bản ghi âm được tính phí theo phần lời nói thực sự nghe được; credit không bao giờ hết hạn
- **Không phải cài gì** - một script Python, chỉ dùng thư viện chuẩn, Python 3.8+

## Lấy khóa

Đăng ký tại <https://equalang.com> và tạo khóa tại <https://equalang.com/api-keys>. Tài khoản mới có sẵn credit miễn phí - đủ để chạy thử một tài liệu và xem kết quả trả về.

```bash
export EQUALANG_API_KEY=el_your_key
```

Hoặc sao chép `.env.example` thành `.env` trong thư mục này - tệp đó đã được gitignore. Khóa chỉ hiển thị một lần; Equalang chỉ lưu giá trị băm của nó.

## Cài đặt

Cách ngắn nhất - dán câu này cho agent của bạn:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# Sẽ tốn bao nhiêu? Miễn phí, và chưa có gì được khởi chạy
python3 scripts/equalang.py estimate report.pdf

# Dịch một tệp; kết quả nằm ngay cạnh tệp nguồn
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Từ một URL công khai (Equalang tự tải), lưu vào một thư mục
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Bản ghi âm nói gì, dưới dạng văn bản có mốc thời gian
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Các chuỗi riêng lẻ, theo đúng thứ tự
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Một văn bản dài, Equalang tự cắt theo câu
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Tác vụ còn đang chạy, số dư, và mã ngôn ngữ
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Mỗi lệnh in ra một đối tượng JSON - đường dẫn và credit, không bao giờ là nội dung tệp - hoặc `{"error", "code", "retryable"}` với mã thoát 1. Thêm `--help` vào bất kỳ lệnh nào để xem các cờ của nó. [SKILL.md](../SKILL.md) là thứ agent đọc.

## Ba điều nên biết

**Ngôn ngữ.** Mã có dạng `en`, `zh-CN`, `ja`. Skill không kèm sẵn danh sách nào: `languages` đọc mã và tên từ API đang chạy (`--kind text` cho tập rộng hơn mà `text` nhận), nên ngôn ngữ Equalang mới thêm dùng được ngay mà không cần cập nhật. Bỏ trống ngôn ngữ nguồn để tự động phát hiện.

**Credit.** Công việc tiêu credit của tài khoản, cùng số dư với trang web. SKILL.md yêu cầu agent nêu chi phí - lấy từ `estimate` - và được đồng ý trước khi bắt đầu tác vụ.

**Tác vụ mất vài phút.** Lệnh sẽ chờ, nghỉ đúng bằng thời gian `Retry-After` của API yêu cầu. Ngắt lệnh không hủy tác vụ - `status <job_id>` tiếp tục theo dõi nó và tải kết quả về.

## Câu hỏi thường gặp

**PDF đã dịch có giữ nguyên bố cục không?**
Có - đó chính là mục đích. Văn bản được đặt lại đúng chỗ cũ, bảng, hình ảnh và công thức nằm nguyên vị trí; DOCX, PPTX hay XLSX vẫn chỉnh sửa được.

**Tài liệu của tôi có bị gửi cho mô hình không?**
Không. Script tải tệp lên Equalang và in ra một đường dẫn. Một bài báo 300 trang không tốn token nào.

**Có dịch được chữ bên trong hình ảnh không?**
Có. Chữ trong JPG, PNG, WebP hoặc BMP được nhận dạng, dịch và vẽ lại vào ảnh.

**Một tác vụ tốn bao nhiêu?**
`estimate` cho biết trước khi bất cứ thứ gì bắt đầu, và hoàn toàn miễn phí. Bảng giá có tại <https://equalang.com/pricing>.

## Cách nó được xây dựng

Vẫn ba quyết định như của [máy chủ MCP](https://github.com/equalang/equalang-mcp):

1. **Tệp không bao giờ đi qua mô hình** - lệnh nhận tệp nằm ở đâu (một đường dẫn, hoặc một URL công khai mà Equalang tự tải) và in ra kết quả được ghi ở đâu.
2. **Một tác vụ nằm gọn trong một lệnh** - tải lên, chờ, tải về. `status` tiếp tục theo dõi tác vụ bị ngắt giữa lúc chờ.
3. **Câu trả lời của API được thuật lại, không phải đoán** - chỉ thử lại những gì API đánh dấu `retryable`; chi phí là `quote` của API; danh sách ngôn ngữ được đọc từ tài liệu OpenAPI của nó; mỗi tác vụ được tạo có một `Idempotency-Key`, nên một câu trả lời bị mất không thể biến thành tác vụ thứ hai bị tính phí.

`python3 scripts/check_api.py` kiểm tra, không cần khóa, rằng mọi đường dẫn và trường mà script dùng - cùng mọi định dạng SKILL.md cam kết - vẫn còn trong hợp đồng của API.

## Liên kết

- [Equalang](https://equalang.com) · [Bảng giá](https://equalang.com/pricing) · [Tài liệu cho nhà phát triển](https://equalang.com/developers)
- API dành cho agent: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - cùng các thao tác, dưới dạng máy chủ MCP
- Thắc mắc: <support@equalang.com>

## Giấy phép

[Apache-2.0](../LICENSE) © Equalang
