# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · **العربية**

[الموقع](https://equalang.com) · [الأسعار](https://equalang.com/pricing) · [وثائق المطورين](https://equalang.com/developers) · [مفاتيح API](https://equalang.com/api-keys)

> **كلمات مفتاحية:** ترجمة المستندات، ترجمة pdf، ترجمة ملف pdf مع الحفاظ على التنسيق، ترجمة ملف وورد، ترجمة docx، ترجمة بوربوينت، ترجمة ملف اكسل، ترجمة epub، ترجمة ملفات srt، ترجمة الترجمة المصاحبة للفيديو، ترجمة النص في الصور، ترجمة فيديو، تحويل الصوت إلى نص، تفريغ صوتي، مترجم بالذكاء الاصطناعي، واجهة برمجة للترجمة، agent skill، claude code skill، codex skill، translation api

**ترجم الملف، واحتفظ بالتنسيق.** [Agent Skill](https://agentskills.io) لـ[Equalang](https://equalang.com) - مترجم بالذكاء الاصطناعي يعمل على الملفات كاملة: ملف PDF يعود PDF، والعرض التقديمي يعود عرضًا تقديميًا، والجداول والصور والمعادلات في أماكنها. كما يترجم الترجمات المصاحبة والصور، ويحوّل الصوت والفيديو إلى ترجمة مصاحبة مترجمة أو نص مفرَّغ، ويترجم النصوص القصيرة بالجملة. يعمل في Claude Code وCodex وCursor وCodeBuddy وكل وكيل آخر يحمّل Agent Skills.

## جرّب أن تطلب

- «ترجم ~/Documents/contract.pdf إلى العربية مع الحفاظ على التنسيق.»
- «ترجم pitch-deck.pptx إلى الإنجليزية والفرنسية.»
- «ترجم https://example.com/whitepaper.pdf إلى العربية واحفظه في ~/Downloads.»
- «كم ستكلّف ترجمة thesis.docx إلى الإنجليزية؟»
- «اصنع ترجمة مصاحبة عربية لـ interview.mp4، مع إبقاء السطر الأصلي فوق كل سطر.»
- «حوّل standup.m4a إلى نص مكتوب مع الطوابع الزمنية.»
- «ترجم النص الموجود في menu.jpg إلى العربية.»
- «ترجم النصوص في locales/en.json إلى الفرنسية والألمانية والإسبانية.»

## المزايا

- **المستندات** - PDF وDOCX وPPTX وXLSX وEPUB وHTML وTXT تعود بالصيغة نفسها، قابلة للتحرير كما كانت، والجداول والصور والمعادلات وتخطيط الصفحة في أماكنها
- **الترجمات المصاحبة والصور** - SRT وVTT تحتفظان بتوقيتهما، مع إمكانية إظهار السطر الأصلي فوق الترجمة؛ وJPG وPNG وWebP وBMP تعود وقد تُرجم النص الموجود داخل الصورة
- **الصوت والفيديو** - MP3 وM4A وWAV وFLAC وOGG وAAC وOpus وMP4 وMOV وWebM وMKV تصبح ترجمة مصاحبة مترجمة، أو نصًا مفرَّغًا باللغة المنطوقة (SRT وVTT وTXT وJSON)
- **نصوص بالجملة** - نصوص قصيرة تُترجم بالترتيب، أو نص طويل واحد (حتى 100,000 حرف) يقسّمه Equalang بنفسه عند حدود الجمل
- **اللغات** - أكثر من 100 للنصوص و12 للملفات، مع اكتشاف لغة المصدر تلقائيًا حين تتركها فارغة

## احصل على مفتاح

سجّل في <https://equalang.com> وأنشئ مفتاحًا من <https://equalang.com/api-keys>. تبدأ الحسابات الجديدة بنقاط مجانية تكفي لترجمة مستند واحد للتجربة.

احفظه مرة واحدة في `~/.config/equalang/.env` فيبقى نافذًا: في أي وكيل - Claude Code أو Codex أو WorkBuddy أو Cursor أو غيرها - وفي كل جلسة جديدة، وبعد إعادة التثبيت والتحديث، دون أي export. ويقرأ خادم Equalang MCP الملف نفسه.

```bash
# استبدل el_your_key بمفتاحك
mkdir -p ~/.config/equalang && echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env && chmod 600 ~/.config/equalang/.env
```

يُفحص متغير البيئة `EQUALANG_API_KEY` أولًا، ولا يُقرأ الملف إلا إذا لم يكن موجودًا - وهكذا يمكن لمشروع ما أن يستخدم مفتاحًا مختلفًا.

## التثبيت

يتطلب `python3` 3.8 أو أحدث، ولا شيء غيره: السكربت يستخدم المكتبة القياسية وحدها.

أقصر طريق - الصق هذا لوكيلك:

> ثبّت مهارة Equalang باتّباع التعليمات في https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (إضافة)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (يدويًا)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

تريدها على مستوى مشروع واحد؟ انسخ المستودع إلى `.claude/skills/equalang` داخل مستودع المشروع.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

يقرأ Codex أيضًا `.agents/skills/` داخل المستودع، لحصر المهارة في مشروع واحد.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

على مستوى المشروع: انسخ المستودع إلى `.codebuddy/skills/equalang` في جذر المشروع.
</details>

<details>
<summary><b>Cursor وGemini CLI وOpenCode وCopilot وGoose وAmp وKiro وغيرها</b></summary>

هذه [Agent Skill](https://agentskills.io) عادية: مجلد بداخله ملف `SKILL.md`. كل عميل يطبّق هذا المعيار يحمّل المجلد نفسه - ولا يختلف إلا المجلد الذي يفحصه كل عميل، وهو مذكور في وثائقه. انسخ المستودع إلى ذلك المجلد فتصبح المهارة مثبّتة.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

تفضّل خادم MCP؟ يقدّم [equalang-mcp](https://github.com/equalang/equalang-mcp) العمليات نفسها على هيئة أدوات، ويعمل كذلك في Claude Desktop وCursor وWindsurf وCline وOpenCode.

## الأوامر

```bash
# كم ستكون التكلفة؟ مجاني، ولا تبدأ أي ترجمة
python3 scripts/equalang.py estimate report.pdf

# ترجمة ملف؛ تُحفظ النتيجة بجوار الملف الأصلي
python3 scripts/equalang.py translate report.pdf --to zh-CN

# من رابط URL عام (يجلبه Equalang بنفسه)، إلى مجلد
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# ما يُقال في تسجيل، نصًا موقوتًا
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# نصوص قصيرة، بالترتيب
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# نص طويل واحد، يقسّمه Equalang عند حدود الجمل
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# مهمة ما زالت قيد التنفيذ، والرصيد، ورموز اللغات
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

يطبع كل أمر JSON: أين كُتبت الملفات وكم كلّفت، أو ما الذي أخفق. ويعرض `--help` مع أي أمر خياراته. والوكيل نفسه يقرأ [SKILL.md](../SKILL.md).

تبدو رموز اللغات هكذا: `en` و`zh-CN` و`ja`. شغّل `languages` لعرضها كلها، أو `languages chinese` للبحث. المهام تستغرق دقائق - ينتظر الأمر، وإذا قاطعته فـ`status <job_id>` يستأنف متابعتها.

## روابط

- [Equalang](https://equalang.com) · [الأسعار](https://equalang.com/pricing) · [وثائق المطورين](https://equalang.com/developers)
- الـAPI للوكلاء: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - العمليات نفسها على هيئة خادم MCP
- للاستفسارات: <support@equalang.com>

## الترخيص

[Apache-2.0](../LICENSE) © Equalang
