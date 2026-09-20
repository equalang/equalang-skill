# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · **ไทย** · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[เว็บไซต์](https://equalang.com) · [ราคา](https://equalang.com/pricing) · [เอกสารสำหรับนักพัฒนา](https://equalang.com/developers) · [คีย์ API](https://equalang.com/api-keys)

> **คีย์เวิร์ด:** แปลเอกสาร, แปล pdf, แปล pdf รูปแบบเดิม, แปลไฟล์ word, แปลไฟล์ docx, แปล powerpoint, แปลไฟล์ excel, แปล epub, แปลซับไตเติ้ล, แปลไฟล์ srt, แปลข้อความในรูปภาพ, แปลวิดีโอ, ถอดเสียงเป็นข้อความ, แปลงเสียงเป็นข้อความ, โปรแกรมแปลภาษา ai, api แปลภาษา, agent skill, claude code skill, codex skill, translation api

**แปลทั้งไฟล์ เลย์เอาต์อยู่ครบ** [Agent Skill](https://agentskills.io) สำหรับ [Equalang](https://equalang.com) - เครื่องมือแปลภาษาด้วย AI ที่ทำงานกับไฟล์ทั้งไฟล์: ส่ง PDF ไปก็ได้ PDF กลับมา ส่งสไลด์ไปก็ได้สไลด์กลับมา ตาราง รูปภาพ และสูตรอยู่ที่เดิมครบ นอกจากนี้ยังแปลคำบรรยายและรูปภาพ เปลี่ยนเสียงและวิดีโอเป็นคำบรรยายที่แปลแล้วหรือบทถอดเสียง และแปลข้อความจำนวนมากในคราวเดียว ใช้ได้ใน Claude Code, Codex, Cursor, CodeBuddy และเอเจนต์อื่นทุกตัวที่โหลด Agent Skills ได้

## ฟีเจอร์

- **เข้ารูปแบบไหน ออกรูปแบบนั้น** - PDF, DOCX, PPTX, XLSX, EPUB, HTML และ TXT ได้กลับมาในรูปแบบเดิม ยังแก้ไขต่อได้ ตาราง รูปภาพ สูตร และเลย์เอาต์ของหน้าอยู่ครบ
- **คำบรรยายและรูปภาพ** - SRT และ VTT คงเวลากำกับไว้ตามเดิม เลือกให้แสดงบรรทัดต้นฉบับไว้เหนือคำแปลได้ ส่วน JPG, PNG, WebP และ BMP ได้กลับมาโดยข้อความในภาพถูกแปลแล้ว
- **เสียงและวิดีโอ** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM และ MKV กลายเป็นคำบรรยายที่แปลแล้ว หรือบทถอดเสียงในภาษาที่พูด (SRT, VTT, TXT, JSON)
- **ข้อความจำนวนมาก** - สตริงที่แยกกันถูกแปลตามลำดับ หรือข้อความยาวหนึ่งข้อความ (สูงสุด 100,000 อักขระ) ที่ Equalang ตัดตามประโยคเอง
- **กว่า 100 ภาษา** - กว่า 100 ภาษาสำหรับข้อความ และ 12 ภาษาสำหรับไฟล์ โดยตรวจจับภาษาต้นทางให้เองเมื่อไม่ได้ระบุ

## รับคีย์

สมัครที่ <https://equalang.com> แล้วสร้างคีย์ที่ <https://equalang.com/api-keys> บัญชีใหม่มีเครดิตฟรีให้ตั้งแต่เริ่ม - พอสำหรับลองแปลเอกสารหนึ่งฉบับแล้วดูผลที่ได้กลับมา

```bash
export EQUALANG_API_KEY=el_your_key
```

หรือคัดลอก `.env.example` เป็น `.env` ในไดเรกทอรีนี้ - ไฟล์นี้อยู่ใน gitignore แล้ว คีย์จะแสดงเพียงครั้งเดียว Equalang เก็บไว้เฉพาะค่าแฮชของคีย์เท่านั้น

## ติดตั้ง

ต้องใช้ `python3` 3.8 ขึ้นไป และไม่ต้องใช้อะไรอีกเลย สคริปต์ใช้แต่ไลบรารีมาตรฐาน

วิธีที่สั้นที่สุด - วางข้อความนี้ให้เอเจนต์ของคุณ:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (ปลั๊กอิน)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (ติดตั้งเอง)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

ต้องการใช้เฉพาะโปรเจกต์เดียว? โคลนลงใน `.claude/skills/equalang` ภายใน repository
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex ยังอ่าน `.agents/skills/` ภายใน repository ด้วย เพื่อจำกัดให้ใช้เฉพาะโปรเจกต์เดียว
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

ใช้เฉพาะโปรเจกต์: โคลนลงใน `.codebuddy/skills/equalang` ที่รากของโปรเจกต์
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro และอื่น ๆ</b></summary>

นี่คือ [Agent Skill](https://agentskills.io) แบบธรรมดา: โฟลเดอร์หนึ่งโฟลเดอร์ที่มี `SKILL.md` อยู่ข้างใน ไคลเอนต์ทุกตัวที่รองรับมาตรฐานนี้โหลดโฟลเดอร์เดียวกัน - ต่างกันแค่ไดเรกทอรีที่แต่ละตัวสแกน ซึ่งดูได้จากเอกสารของไคลเอนต์นั้น ๆ โคลน repository ลงในไดเรกทอรีดังกล่าว สกิลก็ติดตั้งเสร็จ

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

อยากใช้เซิร์ฟเวอร์ MCP มากกว่า? [equalang-mcp](https://github.com/equalang/equalang-mcp) ให้การทำงานชุดเดียวกันในรูปของเครื่องมือ และใช้ได้ใน Claude Desktop, Cursor, Windsurf, Cline และ OpenCode ด้วย

## คำสั่ง

```bash
# จะมีค่าใช้จ่ายเท่าไร? ฟรี และยังไม่เริ่มงานใด ๆ
python3 scripts/equalang.py estimate report.pdf

# แปลไฟล์ ผลลัพธ์อยู่ข้างไฟล์ต้นฉบับ
python3 scripts/equalang.py translate report.pdf --to zh-CN

# จาก URL สาธารณะ (Equalang ไปดึงเอง) บันทึกลงโฟลเดอร์
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# สิ่งที่พูดในไฟล์บันทึกเสียง เป็นข้อความพร้อมเวลากำกับ
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# สตริงที่แยกกัน ตามลำดับ
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# ข้อความยาวหนึ่งข้อความ Equalang ตัดตามประโยคให้
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# งานที่ยังทำอยู่ ยอดคงเหลือ และรหัสภาษา
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

ทุกคำสั่งพิมพ์ออบเจกต์ JSON หนึ่งตัว - มีแต่พาธและเครดิต ไม่มีเนื้อหาไฟล์เด็ดขาด - หรือ `{"error", "code", "retryable"}` พร้อมรหัสออก 1 ใส่ `--help` กับคำสั่งใดก็ได้เพื่อดูแฟล็กของคำสั่งนั้น [SKILL.md](../SKILL.md) คือสิ่งที่เอเจนต์อ่าน

รหัสภาษามีหน้าตาแบบ `en`, `zh-CN`, `ja` โดย `languages` อ่านรหัสเหล่านี้จาก API ที่ใช้งานจริง ภาษาที่ Equalang เพิ่มเข้ามาจึงไม่ต้องอัปเดตที่นี่ งานใช้เวลาหลายนาที - คำสั่งจะรอให้ และถ้าคุณขัดจังหวะ `status <job_id>` ก็กลับมาติดตามต่อได้

## ลิงก์

- [Equalang](https://equalang.com) · [ราคา](https://equalang.com/pricing) · [เอกสารสำหรับนักพัฒนา](https://equalang.com/developers)
- API สำหรับเอเจนต์: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - การทำงานชุดเดียวกันในรูปของเซิร์ฟเวอร์ MCP
- สอบถาม: <support@equalang.com>

## สัญญาอนุญาต

[Apache-2.0](../LICENSE) © Equalang
