# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · **हिन्दी** · [العربية](README.ar.md)

[वेबसाइट](https://equalang.com) · [कीमतें](https://equalang.com/pricing) · [डेवलपर दस्तावेज़](https://equalang.com/developers) · [API कुंजियाँ](https://equalang.com/api-keys)

> **कीवर्ड:** दस्तावेज़ अनुवाद, PDF अनुवाद, PDF ट्रांसलेट कैसे करें, लेआउट बनाए रखते हुए PDF अनुवाद, Word फ़ाइल अनुवाद, PPT अनुवाद, Excel अनुवाद, EPUB अनुवाद, सबटाइटल अनुवाद, SRT ट्रांसलेटर, इमेज ट्रांसलेट, फोटो से टेक्स्ट अनुवाद, वीडियो अनुवाद, ऑडियो से टेक्स्ट, स्पीच टू टेक्स्ट, AI ट्रांसलेटर, agent skill, claude code skill, codex skill, translation api

**फ़ाइल का अनुवाद करें, लेआउट वैसा ही रखें।** [Equalang](https://equalang.com) के लिए एक [Agent Skill](https://agentskills.io)। Equalang एक AI ट्रांसलेटर है जो पूरी फ़ाइलों पर काम करता है: PDF वापस PDF बनकर आता है, प्रेज़ेंटेशन वापस प्रेज़ेंटेशन बनकर, और तालिकाएँ, चित्र और सूत्र अपनी जगह पर रहते हैं। यह सबटाइटल और चित्रों का भी अनुवाद करता है, ऑडियो और वीडियो को अनूदित सबटाइटल या ट्रांसक्रिप्ट में बदलता है, और स्ट्रिंग का थोक में अनुवाद करता है। Claude Code, Codex, Cursor, CodeBuddy और Agent Skills लोड करने वाले हर दूसरे एजेंट में चलता है।

## ख़ूबियाँ

- **जो फ़ॉर्मैट गया, वही लौटा** - PDF, DOCX, PPTX, XLSX, EPUB, HTML और TXT उसी फ़ॉर्मैट में लौटते हैं, संपादन योग्य रहते हैं, और तालिकाएँ, चित्र, सूत्र और पेज लेआउट अपनी जगह पर रहते हैं
- **सबटाइटल और चित्र** - SRT और VTT की टाइमिंग बनी रहती है, चाहें तो अनुवाद के ऊपर मूल पंक्ति भी रखी जा सकती है; JPG, PNG, WebP और BMP इस तरह लौटते हैं कि चित्र के भीतर का टेक्स्ट अनूदित हो चुका होता है
- **ऑडियो और वीडियो** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM और MKV अनूदित सबटाइटल बन जाते हैं, या बोली गई भाषा में ट्रांसक्रिप्ट (SRT, VTT, TXT, JSON)
- **थोक में टेक्स्ट** - अलग-अलग स्ट्रिंग का उसी क्रम में अनुवाद, या एक लंबा टेक्स्ट (100,000 वर्णों तक) जिसे Equalang ख़ुद वाक्यों पर काटता है; टेक्स्ट के लिए 100+ भाषाएँ, फ़ाइलों के लिए 12
- **पूरी फ़ाइल, कॉपी-पेस्ट नहीं** - प्रति फ़ाइल 100 MB तक, किसी पाथ से या सार्वजनिक URL से; टेक्स्ट बॉक्स में टुकड़े-टुकड़े करके डालने की ज़रूरत नहीं
- **कोई टोकन खर्च नहीं** - फ़ाइल Equalang को जाती है और बदले में एक पाथ आता है; 300 पन्नों का PDF कभी बातचीत में नहीं आता
- **काम से पहले कीमत** - `estimate` निःशुल्क बताता है कि किसी जॉब की अधिकतम लागत कितनी हो सकती है; विफल और रद्द किए गए जॉब का कोई शुल्क नहीं; रिकॉर्डिंग का शुल्क वास्तव में सुनी गई वाणी के हिसाब से लगता है; क्रेडिट कभी एक्सपायर नहीं होते
- **इंस्टॉल करने को कुछ नहीं** - एक Python स्क्रिप्ट, सिर्फ़ स्टैंडर्ड लाइब्रेरी, Python 3.8+

## कुंजी पाएँ

<https://equalang.com> पर साइन अप करें और <https://equalang.com/api-keys> पर एक कुंजी बनाएँ। नए खातों को शुरुआत में मुफ़्त क्रेडिट मिलते हैं - इतने कि एक दस्तावेज़ का अनुवाद करके देख सकें कि नतीजा कैसा आता है।

```bash
export EQUALANG_API_KEY=el_your_key
```

या इसी डायरेक्टरी में `.env.example` को `.env` नाम से कॉपी करें - यह gitignore में है। कुंजी सिर्फ़ एक बार दिखाई जाती है; Equalang उसका केवल हैश रखता है।

## इंस्टॉल

सबसे छोटा रास्ता - इसे अपने एजेंट को पेस्ट करें:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (प्लगइन)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (हाथ से)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

सिर्फ़ एक प्रोजेक्ट के लिए चाहिए? रिपॉज़िटरी के भीतर `.claude/skills/equalang` में क्लोन करें।
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex रिपॉज़िटरी के भीतर का `.agents/skills/` भी पढ़ता है, जिससे स्किल को एक ही प्रोजेक्ट तक सीमित रखा जा सकता है।
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

प्रोजेक्ट के स्तर पर: प्रोजेक्ट रूट के `.codebuddy/skills/equalang` में क्लोन करें।
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro और अन्य</b></summary>

यह एक सीधा-सादा [Agent Skill](https://agentskills.io) है: एक फ़ोल्डर जिसमें `SKILL.md` रखा है। इस मानक को लागू करने वाला हर क्लाइंट वही फ़ोल्डर लोड करता है - फ़र्क़ बस उस डायरेक्टरी का है जिसे वह स्कैन करता है, और हर क्लाइंट अपने दस्तावेज़ों में उसे बताता है। रिपॉज़िटरी को उसी डायरेक्टरी में क्लोन करें और स्किल इंस्टॉल हो गया।

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

MCP सर्वर ज़्यादा पसंद है? [equalang-mcp](https://github.com/equalang/equalang-mcp) यही ऑपरेशन टूल के रूप में देता है, और Claude Desktop, Cursor, Windsurf, Cline और OpenCode में भी चलता है।

## कमांड

```bash
# लागत कितनी आएगी? निःशुल्क, और कुछ भी शुरू नहीं होता
python3 scripts/equalang.py estimate report.pdf

# फ़ाइल का अनुवाद करें; नतीजा मूल फ़ाइल के बगल में सहेजा जाता है
python3 scripts/equalang.py translate report.pdf --to zh-CN

# सार्वजनिक URL से (Equalang उसे ख़ुद लाता है), एक फ़ोल्डर में
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# रिकॉर्डिंग में क्या बोला गया है, समय-चिह्नित टेक्स्ट के रूप में
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# अलग-अलग स्ट्रिंग, उसी क्रम में
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# एक लंबा टेक्स्ट, जिसे Equalang वाक्यों पर काटता है
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# चलता हुआ छोड़ा गया जॉब, बैलेंस, और भाषा कोड
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

हर कमांड एक JSON ऑब्जेक्ट प्रिंट करता है - पाथ और क्रेडिट, फ़ाइल की सामग्री कभी नहीं - या एग्ज़िट कोड 1 के साथ `{"error", "code", "retryable"}`। किसी भी कमांड पर `--help` उसके फ़्लैग की सूची देता है। एजेंट [SKILL.md](../SKILL.md) पढ़ता है।

## जानने लायक़ तीन बातें

**भाषाएँ।** कोड `en`, `zh-CN`, `ja` जैसे होते हैं। स्किल में कोई सूची पहले से नहीं रखी गई है: `languages` कोड और नाम लाइव API से पढ़ता है (`text` जो बड़ा सेट लेता है उसके लिए `--kind text`), इसलिए Equalang जो भाषा जोड़ता है वह बिना अपडेट के उपलब्ध हो जाती है। स्रोत भाषा न दें तो वह अपने-आप पहचान ली जाती है।

**क्रेडिट।** काम में खाते के क्रेडिट खर्च होते हैं, वही बैलेंस जो वेबसाइट पर है। SKILL.md के अनुसार एजेंट जॉब शुरू करने से पहले लागत बताता है - `estimate` से - और सहमति लेता है।

**जॉब में कुछ मिनट लगते हैं।** कमांड इंतज़ार करता है, और उतनी देर रुकता है जितना API का `Retry-After` कहता है। कमांड को बीच में रोकने से जॉब रद्द नहीं होता - `status <job_id>` उसे दोबारा पकड़ लेता है और नतीजा डाउनलोड कर देता है।

## अक्सर पूछे जाने वाले सवाल

**क्या अनूदित PDF का लेआउट बना रहता है?**
हाँ - यही तो इसका मक़सद है। टेक्स्ट वहीं वापस रखा जाता है जहाँ वह था, और तालिकाएँ, चित्र और सूत्र अपनी जगह पर रहते हैं; DOCX, PPTX या XLSX संपादन योग्य रहता है।

**क्या मेरा दस्तावेज़ मॉडल को भेजा जाता है?**
नहीं। स्क्रिप्ट फ़ाइल को Equalang पर अपलोड करती है और एक पाथ प्रिंट करती है। 300 पन्नों के शोध-पत्र पर भी कोई टोकन खर्च नहीं होता।

**क्या यह चित्र के भीतर के टेक्स्ट का अनुवाद कर सकता है?**
हाँ। JPG, PNG, WebP या BMP के भीतर का टेक्स्ट पहचाना जाता है, अनूदित होता है और वापस चित्र में बना दिया जाता है।

**एक जॉब की लागत कितनी होती है?**
कुछ भी शुरू होने से पहले `estimate` बता देता है, और यह निःशुल्क है। कीमतें <https://equalang.com/pricing> पर हैं।

## यह कैसे बना है

वही तीन फ़ैसले जो [MCP सर्वर](https://github.com/equalang/equalang-mcp) के हैं:

1. **फ़ाइल कभी मॉडल से होकर नहीं गुज़रती** - कमांड यह लेते हैं कि फ़ाइल कहाँ है (एक पाथ, या एक सार्वजनिक URL जिसे Equalang ख़ुद लाता है) और प्रिंट करते हैं कि नतीजे कहाँ लिखे गए।
2. **जॉब एक ही कमांड के भीतर रहता है** - अपलोड, इंतज़ार, डाउनलोड। जिस जॉब का इंतज़ार बीच में रुक गया हो, उसे `status` दोबारा पकड़ लेता है।
3. **API के जवाब दोहराए जाते हैं, अंदाज़े से नहीं बताए जाते** - दोबारा सिर्फ़ वही आज़माया जाता है जिसे API `retryable` बताता है; लागत API का `quote` है; भाषाओं की सूची उसके OpenAPI दस्तावेज़ से पढ़ी जाती है; हर बनाए गए जॉब के लिए एक `Idempotency-Key`, ताकि खोया हुआ जवाब दूसरा, शुल्क वाला जॉब न बन जाए।

`python3 scripts/check_api.py` बिना कुंजी के जाँचता है कि स्क्रिप्ट जिस भी पाथ और फ़ील्ड का उपयोग करती है - और SKILL.md जिस भी फ़ॉर्मैट का वादा करता है - वह अब भी API के कॉन्ट्रैक्ट में है।

## लिंक

- [Equalang](https://equalang.com) · [कीमतें](https://equalang.com/pricing) · [डेवलपर दस्तावेज़](https://equalang.com/developers)
- एजेंटों के लिए API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - यही ऑपरेशन MCP सर्वर के रूप में
- सवाल: <support@equalang.com>

## लाइसेंस

[Apache-2.0](../LICENSE) © Equalang
