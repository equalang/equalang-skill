# Skill do Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português** · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Uma [Agent Skill](https://github.com/anthropics/skills) que dá o [Equalang](https://equalang.com) ao Claude Code, Codex, Cursor e outros agentes: traduzir arquivos inteiros mantendo o layout, transcrever gravações, traduzir strings em lote.

- **Documentos** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - voltam no mesmo formato.
- **Legendas** (SRT, VTT) e **imagens** (JPG, PNG, WebP, BMP).
- **Áudio e vídeo** voltam como legendas traduzidas ou como transcrição no idioma falado.

## Instalação

Cole isto no seu agente:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Ou manualmente - uma skill é uma pasta:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # crie uma em https://equalang.com/api-keys
```

Como plugin do Claude Code: `/plugin marketplace add equalang/equalang-skill` e depois `/plugin install equalang@equalang`.

Só precisa de `python3` (3.8+); não há nada para instalar com `pip install`.

## O que o agente executa

```bash
python3 scripts/equalang.py estimate report.pdf                  # quanto custaria? (gratuito)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # o resultado fica ao lado do original
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # um único texto longo, cortado por frases pelo Equalang
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Idiomas.** Os códigos têm o formato `en`, `zh-CN`, `ja`. Não há lista embutida na skill: `languages` lê os códigos e nomes da API em produção (`--kind text` para o conjunto mais amplo que `text` aceita), então um idioma que o Equalang adicionar fica disponível sem atualização.

**Créditos.** O trabalho consome os créditos da conta, o mesmo saldo do site. O SKILL.md faz o agente informar o custo - obtido com `estimate` - e obter a concordância antes.

Todo comando imprime um único objeto JSON - caminhos e créditos, nunca o conteúdo dos arquivos - ou `{"error", "code", "retryable"}` com código de saída 1. [SKILL.md](../SKILL.md) é o que o agente lê.

## Como foi construída

As mesmas três decisões do [servidor MCP](https://github.com/equalang/equalang-mcp), que oferece as mesmas operações como ferramentas:

1. **Um arquivo nunca passa pelo modelo** - os comandos recebem onde o arquivo está (um caminho ou uma URL pública que o próprio Equalang busca) e imprimem onde os resultados foram gravados.
2. **Um job vive dentro de um único comando** - envio, espera (pausando pelo tempo que o `Retry-After` da API pedir), download. Interromper a espera não cancela o job; `status` o retoma.
3. **As respostas da API são repetidas, não adivinhadas** - tentar de novo só o que a API marca como `retryable`; o custo é o `quote` da API; a lista de idiomas é lida do documento OpenAPI dela; uma `Idempotency-Key` por job criado, de modo que uma resposta perdida não vira um segundo job cobrado.

`python3 scripts/check_api.py` verifica, sem chave, que todo caminho e campo usado pelo script - e todo formato que o SKILL.md promete - continua no contrato da API. A API em si: <https://equalang.com/llms.txt>.

Apache-2.0.
