# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · **हिन्दी** · [العربية](README.ar.md)

[वेबसाइट](https://equalang.com) · [कीमतें](https://equalang.com/pricing) · [डेवलपर दस्तावेज़](https://equalang.com/developers) · [API कुंजियाँ](https://equalang.com/api-keys)

> **कीवर्ड:** दस्तावेज़ अनुवाद, PDF अनुवाद, PDF ट्रांसलेट कैसे करें, लेआउट बनाए रखते हुए PDF अनुवाद, Word फ़ाइल अनुवाद, PPT अनुवाद, Excel अनुवाद, EPUB अनुवाद, सबटाइटल अनुवाद, SRT ट्रांसलेटर, इमेज ट्रांसलेट, फोटो से टेक्स्ट अनुवाद, वीडियो अनुवाद, ऑडियो से टेक्स्ट, स्पीच टू टेक्स्ट, AI ट्रांसलेटर, agent skill, claude code skill, codex skill, translation api

**फ़ाइल का अनुवाद करें, लेआउट वैसा ही रखें।** [Equalang](https://equalang.com) के लिए एक [Agent Skill](https://agentskills.io)। Equalang एक AI ट्रांसलेटर है जो पूरी फ़ाइलों पर काम करता है: PDF वापस PDF बनकर आता है, प्रेज़ेंटेशन वापस प्रेज़ेंटेशन बनकर, और तालिकाएँ, चित्र और सूत्र अपनी जगह पर रहते हैं। यह सबटाइटल और चित्रों का भी अनुवाद करता है, ऑडियो और वीडियो को अनूदित सबटाइटल या ट्रांसक्रिप्ट में बदलता है, और छोटे-छोटे टेक्स्ट का थोक में अनुवाद करता है। Claude Code, Codex, Cursor, CodeBuddy और Agent Skills लोड करने वाले हर दूसरे एजेंट में चलता है।

## ऐसे कहकर देखें

- “~/Documents/contract.pdf का हिंदी में अनुवाद करो, लेआउट वैसा ही रखना।”
- “pitch-deck.pptx का अंग्रेज़ी और जापानी में अनुवाद करो।”
- “https://example.com/whitepaper.pdf का हिंदी में अनुवाद करके ~/Downloads में सेव करो।”
- “thesis.docx का अंग्रेज़ी में अनुवाद करने में कितना ख़र्च आएगा?”
- “interview.mp4 के लिए हिंदी सबटाइटल बनाओ, हर पंक्ति के ऊपर मूल पंक्ति भी रहे।”
- “standup.m4a को टाइमस्टैंप के साथ टेक्स्ट में बदलो।”
- “menu.jpg में लिखे टेक्स्ट का हिंदी में अनुवाद करो।”
- “locales/en.json की स्ट्रिंग्स का बंगाली, तमिल और मराठी में अनुवाद करो।”

## ख़ूबियाँ

- **दस्तावेज़** - PDF, DOCX, PPTX, XLSX, EPUB, HTML और TXT उसी फ़ॉर्मैट में लौटते हैं, संपादन योग्य रहते हैं, और तालिकाएँ, चित्र, सूत्र और पेज लेआउट अपनी जगह पर रहते हैं
- **सबटाइटल और चित्र** - SRT और VTT की टाइमिंग बनी रहती है, चाहें तो अनुवाद के ऊपर मूल पंक्ति भी रखी जा सकती है; JPG, PNG, WebP और BMP इस तरह लौटते हैं कि चित्र के भीतर का टेक्स्ट अनूदित हो चुका होता है
- **ऑडियो और वीडियो** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM और MKV अनूदित सबटाइटल बन जाते हैं, या बोली गई भाषा में ट्रांसक्रिप्ट (SRT, VTT, TXT, JSON)
- **थोक में टेक्स्ट** - छोटे-छोटे टेक्स्ट का उसी क्रम में अनुवाद, या एक लंबा टेक्स्ट (100,000 वर्णों तक) जिसे Equalang ख़ुद वाक्यों पर काटता है
- **भाषाएँ** - टेक्स्ट के लिए 100+ और फ़ाइलों के लिए 12, और स्रोत भाषा न दें तो वह अपने-आप पहचान ली जाती है

## कुंजी पाएँ

<https://equalang.com> पर साइन अप करें और <https://equalang.com/api-keys> पर एक कुंजी बनाएँ। नए खातों को मुफ़्त क्रेडिट मिलते हैं - एक दस्तावेज़ अनुवाद करके देखने के लिए काफ़ी।

इसे एक बार `~/.config/equalang/.env` में सहेज दें, फिर यह हमेशा काम करती रहेगी: किसी भी एजेंट में - Claude Code, Codex, WorkBuddy, Cursor या कोई और - हर नए सेशन में, और दोबारा इंस्टॉल या अपडेट करने के बाद भी, बिना export किए। Equalang MCP सर्वर भी यही फ़ाइल पढ़ता है।

```bash
mkdir -p ~/.config/equalang
echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env
chmod 600 ~/.config/equalang/.env
```

एनवायरनमेंट में सेट `EQUALANG_API_KEY` को प्राथमिकता मिलती है - किसी एक प्रोजेक्ट में अलग कुंजी के लिए इसे इस्तेमाल करें।

## इंस्टॉल

`python3` 3.8 या उससे नया चाहिए, और कुछ नहीं: स्क्रिप्ट सिर्फ़ स्टैंडर्ड लाइब्रेरी का उपयोग करती है।

सबसे छोटा रास्ता - इसे अपने एजेंट को पेस्ट करें:

> https://equalang.com/install/skill-install.md पर दिए गए निर्देशों के अनुसार Equalang स्किल इंस्टॉल करें।

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
# लागत कितनी आएगी? निःशुल्क, और अनुवाद शुरू नहीं होता
python3 scripts/equalang.py estimate report.pdf

# फ़ाइल का अनुवाद करें; नतीजा मूल फ़ाइल के बगल में सहेजा जाता है
python3 scripts/equalang.py translate report.pdf --to zh-CN

# सार्वजनिक URL से (Equalang उसे ख़ुद लाता है), एक फ़ोल्डर में
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# रिकॉर्डिंग में क्या बोला गया है, समय-चिह्नित टेक्स्ट के रूप में
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# छोटे-छोटे टेक्स्ट, उसी क्रम में
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# एक लंबा टेक्स्ट, जिसे Equalang वाक्यों पर काटता है
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# चलता हुआ छोड़ा गया जॉब, बैलेंस, और भाषा कोड
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

हर कमांड JSON प्रिंट करता है: फ़ाइलें कहाँ लिखी गईं और उन पर कितना ख़र्च हुआ, या क्या गड़बड़ हुई। किसी भी कमांड पर `--help` लगाएँ तो उसके फ़्लैग दिख जाते हैं। एजेंट ख़ुद [SKILL.md](../SKILL.md) पढ़ता है।

भाषा कोड `en`, `zh-CN`, `ja` जैसे होते हैं; सूची देखने के लिए `languages` चलाएँ, या खोजने के लिए `languages chinese`। जॉब में कुछ मिनट लगते हैं - कमांड इंतज़ार करता है, और बीच में रोकने पर `status <job_id>` उसे दोबारा पकड़ लेता है।

## लिंक

- [Equalang](https://equalang.com) · [कीमतें](https://equalang.com/pricing) · [डेवलपर दस्तावेज़](https://equalang.com/developers)
- एजेंटों के लिए API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - यही ऑपरेशन MCP सर्वर के रूप में
- सवाल: <support@equalang.com>

## लाइसेंस

[Apache-2.0](../LICENSE) © Equalang
