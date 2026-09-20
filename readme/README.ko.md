# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[웹사이트](https://equalang.com) · [요금](https://equalang.com/pricing) · [개발자 문서](https://equalang.com/developers) · [API 키](https://equalang.com/api-keys)

> **키워드:** 문서 번역, PDF 번역, PDF 번역 레이아웃 유지, 서식 유지 번역, 워드 번역, PPT 번역, 엑셀 번역, EPUB 번역, 논문 번역, 자막 번역, SRT 자막 번역, 이미지 번역, 영상 번역, 음성 텍스트 변환, 녹음 받아쓰기, AI 번역기, agent skill, claude code skill, codex skill, translation api

**파일은 번역하고, 레이아웃은 그대로.** [Equalang](https://equalang.com)을 위한 [Agent Skill](https://agentskills.io)입니다. Equalang은 파일을 통째로 다루는 AI 번역기입니다. PDF는 PDF로, 슬라이드는 슬라이드로 돌아오고 표와 이미지, 수식은 제자리에 남습니다. 자막과 이미지도 번역하고, 오디오와 비디오를 번역된 자막이나 전사문으로 바꾸며, 짧은 텍스트를 대량으로 번역합니다. Claude Code, Codex, Cursor, CodeBuddy를 비롯해 Agent Skills를 불러오는 모든 에이전트에서 동작합니다.

## 기능

- **문서** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT는 같은 형식으로, 편집 가능한 상태로 돌아오며 표와 이미지, 수식, 페이지 레이아웃이 제자리에 남습니다
- **자막과 이미지** - SRT와 VTT는 타이밍을 유지하고, 원하면 번역문 위에 원문을 함께 넣을 수 있습니다. JPG, PNG, WebP, BMP는 이미지 속 글자가 번역된 채로 돌아옵니다
- **오디오와 비디오** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM, MKV는 번역된 자막으로, 또는 원래 말한 언어의 전사문(SRT, VTT, TXT, JSON)으로 바뀝니다
- **대량 텍스트** - 짧은 텍스트를 순서대로 번역하거나, 긴 텍스트 하나(최대 100,000자)를 Equalang이 직접 문장 단위로 나눠 번역합니다
- **언어** - 텍스트는 100개 이상, 파일은 12개 언어를 지원하며, 원본 언어를 생략하면 자동으로 감지합니다

## 키 받기

<https://equalang.com>에서 가입하고 <https://equalang.com/api-keys>에서 키를 만드세요. 새 계정에는 무료 크레딧이 들어 있어, 문서 하나쯤은 번역해 볼 수 있습니다.

```bash
export EQUALANG_API_KEY=el_your_key
```

또는 이 디렉터리의 `.env.example`을 `.env`로 복사하세요. 이 파일은 gitignore에 들어 있습니다.

## 설치

`python3` 3.8 이상만 있으면 되고, 그 밖에는 아무것도 필요 없습니다. 스크립트는 표준 라이브러리만 씁니다.

가장 빠른 방법은 에이전트에게 다음을 붙여 넣는 것입니다.

> https://equalang.com/install/skill-install.md 의 안내에 따라 Equalang 스킬을 설치해 주세요.

<details open>
<summary><b>Claude Code</b> (플러그인)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (수동)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

프로젝트 단위로 쓰고 싶다면 저장소 안의 `.claude/skills/equalang`에 클론하세요.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex는 저장소 안의 `.agents/skills/`도 읽으므로, 한 프로젝트로 범위를 좁힐 수도 있습니다.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

프로젝트 단위: 프로젝트 루트의 `.codebuddy/skills/equalang`에 클론하세요.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro 등</b></summary>

이것은 평범한 [Agent Skill](https://agentskills.io), 즉 `SKILL.md`가 들어 있는 폴더입니다. 이 표준을 구현한 클라이언트는 모두 같은 폴더를 불러옵니다. 다른 점은 각자 살펴보는 디렉터리뿐이며, 그 위치는 클라이언트마다 문서에 나와 있습니다. 그 디렉터리에 저장소를 클론하면 스킬 설치가 끝납니다.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

MCP 서버가 더 편하신가요? [equalang-mcp](https://github.com/equalang/equalang-mcp)가 같은 작업을 도구로 제공하며, Claude Desktop, Cursor, Windsurf, Cline, OpenCode에서도 동작합니다.

## 명령

```bash
# 비용이 얼마나 들까? 무료이고, 번역이 시작되지는 않습니다
python3 scripts/equalang.py estimate report.pdf

# 파일을 번역합니다. 결과는 원본 옆에 저장됩니다
python3 scripts/equalang.py translate report.pdf --to zh-CN

# 공개 URL에서 (Equalang이 직접 가져옵니다), 지정한 폴더로
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# 녹음에서 말한 내용을 타임코드가 붙은 텍스트로
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# 짧은 텍스트를 순서대로
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# 긴 텍스트 하나, Equalang이 문장 단위로 나눕니다
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# 실행 중인 채로 남은 작업, 잔액, 언어 코드
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

모든 명령은 JSON을 출력합니다. 파일을 어디에 저장했고 얼마가 들었는지, 잘못됐다면 무엇이 잘못됐는지 알려 줍니다. 어떤 명령이든 `--help`를 붙이면 플래그 목록이 나옵니다. 에이전트가 읽는 것은 [SKILL.md](../SKILL.md)입니다.

언어 코드는 `en`, `zh-CN`, `ja`처럼 생겼습니다. `languages`를 실행하면 목록이 나오고, `languages chinese`로 검색할 수 있습니다. 작업은 몇 분씩 걸립니다. 명령은 끝날 때까지 기다리고, 중간에 끊어도 `status <job_id>`로 다시 이어받습니다.

## 링크

- [Equalang](https://equalang.com) · [요금](https://equalang.com/pricing) · [개발자 문서](https://equalang.com/developers)
- 에이전트용 API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - 같은 작업을 MCP 서버로 제공
- 문의: <support@equalang.com>

## 라이선스

[Apache-2.0](../LICENSE) © Equalang
