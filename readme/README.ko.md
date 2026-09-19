# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[웹사이트](https://equalang.com) · [요금](https://equalang.com/pricing) · [개발자 문서](https://equalang.com/developers) · [API 키](https://equalang.com/api-keys)

> **키워드:** 문서 번역, PDF 번역, PDF 번역 레이아웃 유지, 서식 유지 번역, 워드 번역, PPT 번역, 엑셀 번역, EPUB 번역, 논문 번역, 자막 번역, SRT 자막 번역, 이미지 번역, 영상 번역, 음성 텍스트 변환, 녹음 받아쓰기, AI 번역기, agent skill, claude code skill, codex skill, translation api

**파일은 번역하고, 레이아웃은 그대로.** [Equalang](https://equalang.com)을 위한 [Agent Skill](https://agentskills.io)입니다. Equalang은 파일을 통째로 다루는 AI 번역기입니다. PDF는 PDF로, 슬라이드는 슬라이드로 돌아오고 표와 이미지, 수식은 제자리에 남습니다. 자막과 이미지도 번역하고, 오디오와 비디오를 번역된 자막이나 전사문으로 바꾸며, 문자열을 대량으로 번역합니다. Claude Code, Codex, Cursor, CodeBuddy를 비롯해 Agent Skills를 불러오는 모든 에이전트에서 동작합니다.

## 기능

- **넣은 형식 그대로** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT는 같은 형식으로, 편집 가능한 상태로 돌아오며 표와 이미지, 수식, 페이지 레이아웃이 제자리에 남습니다
- **자막과 이미지** - SRT와 VTT는 타이밍을 유지하고, 원하면 번역문 위에 원문을 함께 넣을 수 있습니다. JPG, PNG, WebP, BMP는 이미지 속 글자가 번역된 채로 돌아옵니다
- **오디오와 비디오** - MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM, MKV는 번역된 자막으로, 또는 원래 말한 언어의 전사문(SRT, VTT, TXT, JSON)으로 바뀝니다
- **대량 텍스트** - 개별 문자열을 순서대로 번역하거나, 긴 텍스트 하나(최대 100,000자)를 Equalang이 직접 문장 단위로 나눠 번역합니다. 텍스트는 100개 이상, 파일은 12개 언어를 지원합니다
- **파일 통째로, 붙여넣기 없이** - 파일당 최대 100 MB, 경로나 공개 URL로 넘기면 됩니다. 텍스트 상자에 쪼개 넣을 필요가 없습니다
- **토큰이 들지 않습니다** - 파일은 Equalang으로 가고 경로만 돌아옵니다. 300쪽짜리 PDF도 대화에는 들어오지 않습니다
- **작업 전에 가격부터** - `estimate`가 작업에 들 수 있는 최대 비용을 무료로 알려 줍니다. 실패하거나 취소된 작업은 과금되지 않고, 녹음은 실제로 들린 음성만큼만 과금되며, 크레딧은 만료되지 않습니다
- **설치할 것이 없습니다** - Python 스크립트 하나, 표준 라이브러리만 사용, Python 3.8+

## 키 받기

<https://equalang.com>에서 가입하고 <https://equalang.com/api-keys>에서 키를 만드세요. 새 계정에는 무료 크레딧이 들어 있습니다. 문서 하나를 돌려 보고 결과를 확인하기에 충분한 양입니다.

```bash
export EQUALANG_API_KEY=el_your_key
```

또는 이 디렉터리의 `.env.example`을 `.env`로 복사하세요. 이 파일은 gitignore에 들어 있습니다. 키는 한 번만 표시되며, Equalang은 키의 해시만 보관합니다.

## 설치

가장 빠른 방법은 에이전트에게 다음을 붙여 넣는 것입니다.

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# 비용이 얼마나 들까? 무료이며 아무 작업도 시작되지 않습니다
python3 scripts/equalang.py estimate report.pdf

# 파일을 번역합니다. 결과는 원본 옆에 저장됩니다
python3 scripts/equalang.py translate report.pdf --to zh-CN

# 공개 URL에서 (Equalang이 직접 가져옵니다), 지정한 폴더로
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# 녹음에서 말한 내용을 타임코드가 붙은 텍스트로
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# 개별 문자열을 순서대로
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# 긴 텍스트 하나, Equalang이 문장 단위로 나눕니다
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# 실행 중인 채로 남은 작업, 잔액, 언어 코드
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

모든 명령은 JSON 객체 하나를 출력합니다. 경로와 크레딧일 뿐 파일 내용은 절대 담기지 않습니다. 실패하면 `{"error", "code", "retryable"}`과 함께 종료 코드 1을 냅니다. 어떤 명령이든 `--help`를 붙이면 플래그 목록이 나옵니다. 에이전트가 읽는 것은 [SKILL.md](../SKILL.md)입니다.

## 알아 두면 좋은 세 가지

**언어.** 코드는 `en`, `zh-CN`, `ja`처럼 생겼습니다. 스킬에는 언어 목록이 내장되어 있지 않습니다. `languages`가 실제 API에서 코드와 이름을 읽어 오므로(`text`가 받는 더 넓은 목록은 `--kind text`), Equalang이 언어를 추가하면 업데이트 없이 바로 쓸 수 있습니다. 원본 언어를 생략하면 자동으로 감지합니다.

**크레딧.** 작업은 계정의 크레딧, 즉 웹사이트와 같은 잔액을 씁니다. SKILL.md는 에이전트가 작업을 시작하기 전에 `estimate`로 얻은 비용을 밝히고 동의를 받도록 합니다.

**작업은 몇 분씩 걸립니다.** 명령은 API의 `Retry-After`가 요구하는 만큼 쉬어 가며 기다립니다. 명령을 중단해도 작업은 취소되지 않습니다. `status <job_id>`로 다시 이어받으면 결과까지 내려받습니다.

## 자주 묻는 질문

**번역된 PDF의 레이아웃이 유지되나요?**
네, 바로 그것이 핵심입니다. 텍스트는 원래 자리에 다시 들어가고 표와 이미지, 수식은 제자리에 남습니다. DOCX, PPTX, XLSX는 편집 가능한 상태 그대로입니다.

**제 문서가 모델로 전송되나요?**
아니요. 스크립트는 파일을 Equalang에 업로드하고 경로를 출력할 뿐입니다. 300쪽짜리 논문에도 토큰은 들지 않습니다.

**이미지 속 글자도 번역할 수 있나요?**
네. JPG, PNG, WebP, BMP 속 글자를 인식해 번역한 뒤 이미지에 다시 그려 넣습니다.

**작업 비용은 얼마인가요?**
무엇이든 시작되기 전에 `estimate`가 알려 주며, 무료입니다. 요금은 <https://equalang.com/pricing>에서 확인하세요.

## 만든 방식

[MCP 서버](https://github.com/equalang/equalang-mcp)와 똑같은 세 가지 결정입니다.

1. **파일은 절대 모델을 거치지 않습니다** - 명령은 파일이 어디 있는지(경로 또는 Equalang이 직접 가져오는 공개 URL)를 받고 결과가 어디에 쓰였는지를 출력합니다.
2. **작업은 명령 하나 안에서 끝납니다** - 업로드, 대기, 다운로드. 대기가 중단된 작업은 `status`로 다시 이어받습니다.
3. **API의 답은 추측하지 않고 그대로 전합니다** - API가 `retryable`로 표시한 것만 재시도하고, 비용은 API의 `quote`이며, 언어 목록은 API의 OpenAPI 문서에서 읽고, 생성하는 작업마다 `Idempotency-Key`를 하나씩 써서 응답이 유실되어도 과금되는 두 번째 작업이 생기지 않습니다.

`python3 scripts/check_api.py`는 스크립트가 쓰는 모든 경로와 필드, 그리고 SKILL.md가 약속하는 모든 형식이 여전히 API 계약에 있는지를 키 없이 검증합니다.

## 링크

- [Equalang](https://equalang.com) · [요금](https://equalang.com/pricing) · [개발자 문서](https://equalang.com/developers)
- 에이전트용 API: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) - 같은 작업을 MCP 서버로 제공
- 문의: <support@equalang.com>

## 라이선스

[Apache-2.0](../LICENSE) © Equalang
