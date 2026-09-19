# مهارة Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · **العربية**

[Agent Skill](https://github.com/anthropics/skills) تمنح Claude Code وCodex وCursor وغيرها من الوكلاء [Equalang](https://equalang.com): ترجمة ملفات كاملة مع الحفاظ على تنسيقها، وتفريغ التسجيلات نصيًا، وترجمة السلاسل النصية بالجملة.

- **المستندات** - PDF وDOCX وPPTX وXLSX وEPUB وHTML وTXT - تعود بالصيغة نفسها.
- **الترجمات المصاحبة** (SRT وVTT) و**الصور** (JPG وPNG وWebP وBMP).
- **الصوت والفيديو** يعودان على هيئة ترجمة مصاحبة مترجمة، أو نص مفرَّغ باللغة المنطوقة.

## التثبيت

الصق هذا لوكيلك:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

أو يدويًا - فالمهارة مجرد مجلد:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # أنشئ مفتاحًا من https://equalang.com/api-keys
```

بوصفها إضافة لـClaude Code: `/plugin marketplace add equalang/equalang-skill`، ثم `/plugin install equalang@equalang`.

`python3` (3.8+) هو كل ما تحتاج إليه؛ ولا شيء يتطلب `pip install`.

## ما يشغّله الوكيل

```bash
python3 scripts/equalang.py estimate report.pdf                  # كم ستكون التكلفة؟ (مجاني)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # تُحفظ النتيجة بجوار الملف الأصلي
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # نص طويل واحد، تقسّمه Equalang عند حدود الجمل
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**اللغات.** تبدو الرموز هكذا: `en` و`zh-CN` و`ja`. لا توجد قائمة مضمّنة في المهارة: `languages` يقرأ الرموز والأسماء من الـAPI الحي (`--kind text` للمجموعة الأوسع التي يقبلها `text`)، فأي لغة يضيفها Equalang تصبح متاحة من دون تحديث.

**النقاط.** العمل يستهلك نقاط الحساب، وهو الرصيد نفسه في الموقع. يجعل SKILL.md الوكيل يذكر التكلفة - من `estimate` - ويحصل على الموافقة أولًا.

يطبع كل أمر كائن JSON واحدًا - مسارات ونقاطًا، لا محتويات ملفات أبدًا - أو `{"error", "code", "retryable"}` مع رمز خروج 1. [SKILL.md](../SKILL.md) هو ما يقرؤه الوكيل.

## كيف بُنيت

القرارات الثلاثة نفسها في [خادم MCP](https://github.com/equalang/equalang-mcp)، الذي يقدّم العمليات نفسها على هيئة أدوات:

1. **الملف لا يمر عبر النموذج أبدًا** - تأخذ الأوامر مكان الملف (مسارًا، أو رابط URL عامًا يجلبه Equalang بنفسه) وتطبع مكان كتابة النتائج.
2. **المهمة تعيش داخل أمر واحد** - رفع، ثم انتظار (مع التوقف المدة التي يطلبها `Retry-After` الخاص بالـAPI)، ثم تنزيل. قطع الانتظار لا يلغي المهمة؛ و`status` يستأنف متابعتها.
3. **إجابات الـAPI تُنقل كما هي، لا تُخمَّن** - لا تُعاد المحاولة إلا فيما يضع عليه الـAPI علامة `retryable`؛ والتكلفة هي `quote` الخاص بالـAPI؛ وقائمة اللغات تُقرأ من مستند OpenAPI الخاص به؛ و`Idempotency-Key` واحد لكل مهمة مُنشأة، فلا يمكن أن تتحول إجابة ضائعة إلى مهمة ثانية مدفوعة.

يتحقق `python3 scripts/check_api.py`، من دون مفتاح، من أن كل مسار وحقل يستخدمه السكربت - وكل صيغة يعد بها SKILL.md - ما زال ضمن عقد الـAPI. الـAPI نفسه: <https://equalang.com/llms.txt>.

Apache-2.0.
