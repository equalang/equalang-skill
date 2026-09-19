# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · **العربية**

[الموقع](https://equalang.com) · [الأسعار](https://equalang.com/pricing) · [وثائق المطورين](https://equalang.com/developers) · [مفاتيح API](https://equalang.com/api-keys)

> **كلمات مفتاحية:** ترجمة المستندات، ترجمة pdf، ترجمة ملف pdf مع الحفاظ على التنسيق، ترجمة ملف وورد، ترجمة docx، ترجمة بوربوينت، ترجمة ملف اكسل، ترجمة epub، ترجمة ملفات srt، ترجمة الترجمة المصاحبة للفيديو، ترجمة النص في الصور، ترجمة فيديو، تحويل الصوت إلى نص، تفريغ صوتي، مترجم بالذكاء الاصطناعي، واجهة برمجة للترجمة، agent skill، claude code skill، codex skill، translation api

**ترجم الملف، واحتفظ بالتنسيق.** [Agent Skill](https://agentskills.io) لـ[Equalang](https://equalang.com) - مترجم بالذكاء الاصطناعي يعمل على الملفات كاملة: ملف PDF يعود PDF، والعرض التقديمي يعود عرضًا تقديميًا، والجداول والصور والمعادلات في أماكنها. كما يترجم الترجمات المصاحبة والصور، ويحوّل الصوت والفيديو إلى ترجمة مصاحبة مترجمة أو نص مفرَّغ، ويترجم السلاسل النصية بالجملة. يعمل في Claude Code وCodex وCursor وCodeBuddy وكل وكيل آخر يحمّل Agent Skills.

## المزايا

- **الصيغة التي تدخل هي التي تخرج** - PDF وDOCX وPPTX وXLSX وEPUB وHTML وTXT تعود بالصيغة نفسها، قابلة للتحرير كما كانت، والجداول والصور والمعادلات وتخطيط الصفحة في أماكنها
- **الترجمات المصاحبة والصور** - SRT وVTT تحتفظان بتوقيتهما، مع إمكانية إظهار السطر الأصلي فوق الترجمة؛ وJPG وPNG وWebP وBMP تعود وقد تُرجم النص الموجود داخل الصورة
- **الصوت والفيديو** - MP3 وM4A وWAV وFLAC وOGG وAAC وOpus وMP4 وMOV وWebM وMKV تصبح ترجمة مصاحبة مترجمة، أو نصًا مفرَّغًا باللغة المنطوقة (SRT وVTT وTXT وJSON)
- **نصوص بالجملة** - سلاسل نصية منفصلة تُترجم بالترتيب، أو نص طويل واحد (حتى 100,000 حرف) يقسّمه Equalang بنفسه عند حدود الجمل؛ أكثر من 100 لغة للنصوص، و12 للملفات
- **ملفات كاملة، بلا نسخ ولصق** - حتى 100 MB للملف، من مسار أو رابط URL عام؛ لا شيء تقسّمه على مربعات النص
- **لا يستهلك أي توكنات** - يذهب الملف إلى Equalang ويعود مسار؛ ملف PDF من 300 صفحة لا يدخل المحادثة أبدًا
- **السعر قبل المهمة** - يجيب `estimate` بأقصى ما يمكن أن تكلفه المهمة، مجانًا؛ المهام الفاشلة والملغاة لا تكلف شيئًا؛ ويُحتسب التسجيل بحسب الكلام المسموع فعلًا؛ والنقاط لا تنتهي صلاحيتها أبدًا
- **لا شيء للتثبيت** - سكربت Python واحد، بالمكتبة القياسية وحدها، Python 3.8+

## احصل على مفتاح

سجّل في <https://equalang.com> وأنشئ مفتاحًا من <https://equalang.com/api-keys>. تبدأ الحسابات الجديدة بنقاط مجانية - تكفي لتجربة مستند ورؤية ما يعود.

```bash
export EQUALANG_API_KEY=el_your_key
```

أو انسخ `.env.example` إلى `.env` في هذا المجلد - وهو مُدرج في gitignore. يُعرض المفتاح مرة واحدة؛ ولا يحتفظ Equalang إلا بقيمة التجزئة (hash) الخاصة به.

## التثبيت

أقصر طريق - الصق هذا لوكيلك:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# كم ستكون التكلفة؟ مجاني، ولا يبدأ أي شيء
python3 scripts/equalang.py estimate report.pdf

# ترجمة ملف؛ تُحفظ النتيجة بجوار الملف الأصلي
python3 scripts/equalang.py translate report.pdf --to zh-CN

# من رابط URL عام (يجلبه Equalang بنفسه)، إلى مجلد
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# ما يُقال في تسجيل، نصًا موقوتًا
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# سلاسل نصية منفصلة، بالترتيب
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# نص طويل واحد، يقسّمه Equalang عند حدود الجمل
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# مهمة ما زالت قيد التنفيذ، والرصيد، ورموز اللغات
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

يطبع كل أمر كائن JSON واحدًا - مسارات ونقاطًا، لا محتويات ملفات أبدًا - أو `{"error", "code", "retryable"}` مع رمز خروج 1. ويعرض `--help` مع أي أمر خياراته. [SKILL.md](../SKILL.md) هو ما يقرؤه الوكيل.

## ثلاثة أمور تستحق المعرفة

**اللغات.** تبدو الرموز هكذا: `en` و`zh-CN` و`ja`. لا توجد قائمة مضمّنة في المهارة: `languages` يقرأ الرموز والأسماء من الـAPI الحي (`--kind text` للمجموعة الأوسع التي يقبلها `text`)، فأي لغة يضيفها Equalang تصبح متاحة من دون تحديث. اترك لغة المصدر فارغة ليجري اكتشافها تلقائيًا.

**النقاط.** العمل يستهلك نقاط الحساب، وهو الرصيد نفسه في الموقع. يجعل SKILL.md الوكيل يذكر التكلفة - من `estimate` - ويحصل على الموافقة قبل أن يبدأ أي مهمة.

**المهام تستغرق دقائق.** ينتظر الأمر، متوقفًا المدة التي يطلبها `Retry-After` الخاص بالـAPI. مقاطعته لا تلغي المهمة - فـ`status <job_id>` يستأنف متابعتها وينزّل النتيجة.

## أسئلة شائعة

**هل يحتفظ ملف PDF المترجَم بتنسيقه؟**
نعم - وهذا هو بيت القصيد. يُعاد النص إلى مكانه، وتبقى الجداول والصور والمعادلات في أماكنها؛ ويظل ملف DOCX أو PPTX أو XLSX قابلًا للتحرير.

**هل يُرسَل مستندي إلى النموذج؟**
لا. يرفع السكربت الملف إلى Equalang ويطبع مسارًا. ورقة بحثية من 300 صفحة لا تكلف أي توكنات.

**هل يستطيع ترجمة النص داخل الصورة؟**
نعم. يُتعرَّف على النص في JPG أو PNG أو WebP أو BMP، ثم يُترجم ويُرسم من جديد داخل الصورة.

**كم تكلف المهمة؟**
يخبرك `estimate` قبل أن يبدأ أي شيء، وهو مجاني. الأسعار في <https://equalang.com/pricing>.

## كيف بُنيت

القرارات الثلاثة نفسها في [خادم MCP](https://github.com/equalang/equalang-mcp):

1. **الملف لا يمر عبر النموذج أبدًا** - تأخذ الأوامر مكان الملف (مسارًا، أو رابط URL عامًا يجلبه Equalang بنفسه) وتطبع مكان كتابة النتائج.
2. **المهمة تعيش داخل أمر واحد** - رفع، ثم انتظار، ثم تنزيل. و`status` يستأنف متابعة مهمة قُطع انتظارها.
3. **إجابات الـAPI تُنقل كما هي، لا تُخمَّن** - لا تُعاد المحاولة إلا فيما يضع عليه الـAPI علامة `retryable`؛ والتكلفة هي `quote` الخاص بالـAPI؛ وقائمة اللغات تُقرأ من مستند OpenAPI الخاص به؛ و`Idempotency-Key` واحد لكل مهمة مُنشأة، فلا يمكن أن تتحول إجابة ضائعة إلى مهمة ثانية مدفوعة.

يتحقق `python3 scripts/check_api.py`، من دون مفتاح، من أن كل مسار وحقل يستخدمه السكربت - وكل صيغة يعد بها SKILL.md - ما زال ضمن عقد الـAPI.

## روابط

- [Equalang](https://equalang.com) · [الأسعار](https://equalang.com/pricing) · [وثائق المطورين](https://equalang.com/developers)
- الـAPI للوكلاء: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - العمليات نفسها على هيئة خادم MCP
- للاستفسارات: <support@equalang.com>

## الترخيص

[Apache-2.0](../LICENSE) © Equalang
