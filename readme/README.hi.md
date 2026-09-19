# Equalang स्किल

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · **हिन्दी** · [العربية](README.ar.md)

एक [Agent Skill](https://github.com/anthropics/skills) जो Claude Code, Codex, Cursor और दूसरे एजेंटों को [Equalang](https://equalang.com) देता है: लेआउट बनाए रखते हुए पूरी फ़ाइलों का अनुवाद, रिकॉर्डिंग का ट्रांसक्रिप्शन, स्ट्रिंग का थोक में अनुवाद।

- **दस्तावेज़** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - उसी फ़ॉर्मैट में लौटते हैं।
- **सबटाइटल** (SRT, VTT) और **चित्र** (JPG, PNG, WebP, BMP)।
- **ऑडियो और वीडियो** अनूदित सबटाइटल के रूप में, या बोली गई भाषा में ट्रांसक्रिप्ट के रूप में लौटते हैं।

## इंस्टॉल

इसे अपने एजेंट को पेस्ट करें:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

या हाथ से - स्किल बस एक फ़ोल्डर है:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # https://equalang.com/api-keys पर बनाएँ
```

Claude Code प्लगइन के रूप में: `/plugin marketplace add equalang/equalang-skill`, फिर `/plugin install equalang@equalang`।

इसे सिर्फ़ `python3` (3.8+) चाहिए; `pip install` करने को कुछ नहीं है।

## एजेंट क्या चलाता है

```bash
python3 scripts/equalang.py estimate report.pdf                  # कितनी लागत आएगी? (निःशुल्क)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # नतीजा स्रोत फ़ाइल के बगल में सहेजा जाता है
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # एक लंबा टेक्स्ट, जिसे Equalang वाक्यों पर काटता है
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**भाषाएँ।** कोड `en`, `zh-CN`, `ja` जैसे होते हैं। स्किल में कोई सूची पहले से नहीं रखी गई है: `languages` कोड और नाम लाइव API से पढ़ता है (`text` जो बड़ा सेट लेता है उसके लिए `--kind text`), इसलिए Equalang जो भाषा जोड़ता है वह बिना अपडेट के उपलब्ध हो जाती है।

**क्रेडिट।** काम में खाते के क्रेडिट खर्च होते हैं, वही बैलेंस जो वेबसाइट पर है। SKILL.md के अनुसार एजेंट पहले लागत बताता है - `estimate` से - और सहमति लेता है।

हर कमांड एक JSON ऑब्जेक्ट प्रिंट करता है - पाथ और क्रेडिट, फ़ाइल की सामग्री कभी नहीं - या एग्ज़िट कोड 1 के साथ `{"error", "code", "retryable"}`। एजेंट [SKILL.md](../SKILL.md) पढ़ता है।

## यह कैसे बना है

वही तीन फ़ैसले जो [MCP सर्वर](https://github.com/equalang/equalang-mcp) के हैं, जो यही ऑपरेशन टूल के रूप में देता है:

1. **फ़ाइल कभी मॉडल से होकर नहीं गुज़रती** - कमांड यह लेते हैं कि फ़ाइल कहाँ है (एक पाथ, या एक सार्वजनिक URL जिसे Equalang ख़ुद लाता है) और प्रिंट करते हैं कि नतीजे कहाँ लिखे गए।
2. **जॉब एक ही कमांड के भीतर रहता है** - अपलोड, इंतज़ार (उतनी देर रुककर जितना API का `Retry-After` कहता है), डाउनलोड। इंतज़ार बीच में रोकने से जॉब रद्द नहीं होता; `status` उसे दोबारा पकड़ लेता है।
3. **API के जवाब दोहराए जाते हैं, अंदाज़े से नहीं बताए जाते** - दोबारा सिर्फ़ वही आज़माया जाता है जिसे API `retryable` बताता है; लागत API का `quote` है; भाषाओं की सूची उसके OpenAPI दस्तावेज़ से पढ़ी जाती है; हर बनाए गए जॉब के लिए एक `Idempotency-Key`, ताकि खोया हुआ जवाब दूसरा, शुल्क वाला जॉब न बन जाए।

`python3 scripts/check_api.py` बिना कुंजी के जाँचता है कि स्क्रिप्ट जिस भी पाथ और फ़ील्ड का उपयोग करती है - और SKILL.md जिस भी फ़ॉर्मैट का वादा करता है - वह अब भी API के कॉन्ट्रैक्ट में है। API स्वयं: <https://equalang.com/llms.txt>।

Apache-2.0.
