# สกิล Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · **ไทย** · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Agent Skill](https://github.com/anthropics/skills) ที่ทำให้ Claude Code, Codex, Cursor และเอเจนต์อื่น ๆ ใช้ [Equalang](https://equalang.com) ได้: แปลไฟล์ทั้งไฟล์โดยคงเลย์เอาต์ไว้ ถอดเสียงจากไฟล์บันทึก และแปลข้อความจำนวนมากในคราวเดียว

- **เอกสาร** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - ได้กลับมาในรูปแบบเดิม
- **คำบรรยาย** (SRT, VTT) และ**รูปภาพ** (JPG, PNG, WebP, BMP)
- **เสียงและวิดีโอ** ได้กลับมาเป็นคำบรรยายที่แปลแล้ว หรือเป็นบทถอดเสียงในภาษาที่พูด

## ติดตั้ง

วางข้อความนี้ให้เอเจนต์ของคุณ:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

หรือทำเอง - สกิลก็คือโฟลเดอร์หนึ่งโฟลเดอร์:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # สร้างคีย์ได้ที่ https://equalang.com/api-keys
```

ในรูปแบบปลั๊กอินของ Claude Code: `/plugin marketplace add equalang/equalang-skill` แล้วตามด้วย `/plugin install equalang@equalang`

ใช้แค่ `python3` (3.8+) เท่านั้น ไม่ต้อง `pip install` อะไรเลย

## สิ่งที่เอเจนต์รัน

```bash
python3 scripts/equalang.py estimate report.pdf                  # จะมีค่าใช้จ่ายเท่าไร? (ฟรี)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # ผลลัพธ์อยู่ข้างไฟล์ต้นฉบับ
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**ภาษา** รหัสมีหน้าตาแบบ `en`, `zh-CN`, `ja` สกิลนี้ไม่ได้ฝังรายการภาษาไว้: `languages` อ่านรหัสและชื่อจาก API ที่ใช้งานจริง (`--kind text` สำหรับชุดที่กว้างกว่าซึ่ง `text` รองรับ) ภาษาที่ Equalang เพิ่มเข้ามาจึงใช้ได้ทันทีโดยไม่ต้องอัปเดต

**เครดิต** งานแต่ละงานใช้เครดิตของบัญชี ซึ่งเป็นยอดคงเหลือเดียวกับบนเว็บไซต์ SKILL.md กำหนดให้เอเจนต์แจ้งค่าใช้จ่าย - จาก `estimate` - และขอความยินยอมก่อน

ทุกคำสั่งพิมพ์ออบเจกต์ JSON หนึ่งตัว - มีแต่พาธและเครดิต ไม่มีเนื้อหาไฟล์เด็ดขาด - หรือ `{"error", "code", "retryable"}` พร้อมรหัสออก 1 [SKILL.md](../SKILL.md) คือสิ่งที่เอเจนต์อ่าน

## ออกแบบมาอย่างไร

การตัดสินใจสามข้อเดียวกับ[เซิร์ฟเวอร์ MCP](https://github.com/equalang/equalang-mcp) ซึ่งให้การทำงานชุดเดียวกันในรูปของเครื่องมือ:

1. **ไฟล์ไม่ผ่านโมเดลเลย** - คำสั่งรับตำแหน่งของไฟล์ (พาธ หรือ URL สาธารณะที่ Equalang ไปดึงเอง) แล้วพิมพ์ตำแหน่งที่เขียนผลลัพธ์ไว้
2. **งานหนึ่งงานอยู่ภายในคำสั่งเดียว** - อัปโหลด รอ (เว้นช่วงนานเท่าที่ `Retry-After` ของ API ระบุ) แล้วดาวน์โหลด การขัดจังหวะระหว่างรอไม่ได้ยกเลิกงาน ใช้ `status` กลับมาติดตามต่อได้
3. **คำตอบของ API ถูกถ่ายทอดต่อ ไม่ใช่เดาเอา** - ลองใหม่เฉพาะสิ่งที่ API ระบุว่า `retryable` ค่าใช้จ่ายคือ `quote` ของ API รายการภาษาอ่านจากเอกสาร OpenAPI ของมัน และใช้ `Idempotency-Key` หนึ่งค่าต่องานที่สร้างหนึ่งงาน คำตอบที่หายไปจึงไม่มีทางกลายเป็นงานที่สองที่ถูกคิดค่าใช้จ่าย

`python3 scripts/check_api.py` ตรวจสอบได้โดยไม่ต้องใช้คีย์ ว่าทุกพาธและฟิลด์ที่สคริปต์ใช้ - รวมถึงทุกรูปแบบที่ SKILL.md สัญญาไว้ - ยังอยู่ในสัญญาของ API ตัว API เอง: <https://equalang.com/llms.txt>

Apache-2.0
