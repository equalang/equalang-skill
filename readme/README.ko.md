# Equalang 스킬

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Claude Code, Codex, Cursor 등의 에이전트에게 [Equalang](https://equalang.com)을 붙여 주는 [Agent Skill](https://github.com/anthropics/skills)입니다. 레이아웃을 유지한 채 파일을 통째로 번역하고, 녹음을 받아쓰고, 문자열을 대량으로 번역합니다.

- **문서** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - 는 같은 형식으로 돌아옵니다.
- **자막**(SRT, VTT)과 **이미지**(JPG, PNG, WebP, BMP).
- **오디오와 비디오**는 번역된 자막으로, 또는 원래 말한 언어의 전사문으로 돌아옵니다.

## 설치

에이전트에게 다음을 붙여 넣으세요.

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

직접 설치할 수도 있습니다 - 스킬은 폴더 하나입니다.

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # https://equalang.com/api-keys 에서 만드세요
```

Claude Code 플러그인으로 설치: `/plugin marketplace add equalang/equalang-skill`, 그다음 `/plugin install equalang@equalang`.

`python3`(3.8+)만 있으면 됩니다. `pip install`할 것은 없습니다.

## 에이전트가 실행하는 명령

```bash
python3 scripts/equalang.py estimate report.pdf                  # 비용이 얼마나 들까? (무료)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # 결과는 원본 옆에 저장됩니다
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # 긴 텍스트 하나, Equalang이 문장 단위로 나눔
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**언어.** 코드는 `en`, `zh-CN`, `ja`처럼 생겼습니다. 스킬에는 언어 목록이 내장되어 있지 않습니다. `languages`가 실제 API에서 코드와 이름을 읽어 오므로(`text`가 받는 더 넓은 목록은 `--kind text`), Equalang이 언어를 추가하면 업데이트 없이 바로 쓸 수 있습니다.

**크레딧.** 작업은 계정의 크레딧, 즉 웹사이트와 같은 잔액을 씁니다. SKILL.md는 에이전트가 `estimate`로 얻은 비용을 먼저 밝히고 동의를 받도록 합니다.

모든 명령은 JSON 객체 하나를 출력합니다 - 경로와 크레딧일 뿐 파일 내용은 절대 아닙니다 - 실패하면 `{"error", "code", "retryable"}`과 함께 종료 코드 1을 냅니다. 에이전트가 읽는 것은 [SKILL.md](../SKILL.md)입니다.

## 만든 방식

같은 작업을 도구로 제공하는 [MCP 서버](https://github.com/equalang/equalang-mcp)와 똑같은 세 가지 결정입니다.

1. **파일은 절대 모델을 거치지 않습니다** - 명령은 파일이 어디 있는지(경로 또는 Equalang이 직접 가져오는 공개 URL)를 받고 결과가 어디에 쓰였는지를 출력합니다.
2. **작업은 명령 하나 안에서 끝납니다** - 업로드, 대기(API의 `Retry-After`가 요구하는 만큼 쉬면서), 다운로드. 대기를 중단해도 작업은 취소되지 않으며 `status`로 다시 이어받습니다.
3. **API의 답은 추측하지 않고 그대로 전합니다** - API가 `retryable`로 표시한 것만 재시도하고, 비용은 API의 `quote`이며, 언어 목록은 API의 OpenAPI 문서에서 읽고, 생성하는 작업마다 `Idempotency-Key`를 하나씩 써서 응답이 유실되어도 과금되는 두 번째 작업이 생기지 않습니다.

`python3 scripts/check_api.py`는 스크립트가 쓰는 모든 경로와 필드, 그리고 SKILL.md가 약속하는 모든 형식이 여전히 API 계약에 있는지를 키 없이 검증합니다. API 자체: <https://equalang.com/llms.txt>.

Apache-2.0.
