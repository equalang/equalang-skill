# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português** · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Site](https://equalang.com) · [Preços](https://equalang.com/pricing) · [Documentação para desenvolvedores](https://equalang.com/developers) · [Chaves de API](https://equalang.com/api-keys)

> **Palavras-chave:** traduzir pdf, tradutor de pdf, traduzir pdf mantendo a formatação, tradutor de documentos, traduzir documento word, traduzir docx, traduzir powerpoint, traduzir excel, traduzir epub, traduzir legendas, tradutor de legendas srt, traduzir imagem, traduzir texto de imagem, traduzir vídeo, transcrever áudio em texto, tradutor com ia, agent skill, claude code skill, codex skill, translation api

**Traduza o arquivo, mantenha o layout.** Uma [Agent Skill](https://agentskills.io) para o [Equalang](https://equalang.com), um tradutor com IA que trabalha com arquivos inteiros: um PDF volta como PDF, uma apresentação como apresentação, com tabelas, imagens e fórmulas onde estavam. Também traduz legendas e imagens, transforma áudio e vídeo em legendas traduzidas ou em transcrição, e traduz textos curtos em lote. Funciona no Claude Code, Codex, Cursor, CodeBuddy e em qualquer outro agente que carregue Agent Skills.

## Experimente pedir

- “Traduza ~/Documents/contract.pdf para o português, mantendo o layout.”
- “Traduza pitch-deck.pptx para o inglês e o espanhol.”
- “Traduza https://example.com/whitepaper.pdf para o português e salve em ~/Downloads.”
- “Quanto custaria traduzir thesis.docx para o inglês?”
- “Faça legendas em português para interview.mp4, com a linha original acima de cada tradução.”
- “Transcreva standup.m4a com marcações de tempo.”
- “Traduza para o português o texto de menu.jpg.”
- “Traduza os textos de locales/en.json para espanhol, francês e alemão.”

## Recursos

- **Documentos**: PDF, DOCX, PPTX, XLSX, EPUB, HTML e TXT voltam no mesmo formato, ainda editáveis, com tabelas, imagens, fórmulas e layout de página no lugar
- **Legendas e imagens**: SRT e VTT mantêm a sincronização, opcionalmente com a linha original acima da tradução; JPG, PNG, WebP e BMP voltam com o texto da imagem traduzido
- **Áudio e vídeo**: MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM e MKV viram legendas traduzidas ou uma transcrição no idioma falado (SRT, VTT, TXT, JSON)
- **Texto em lote**: textos curtos traduzidos em ordem, ou um único texto longo (até 100.000 caracteres) que o próprio Equalang corta por frases
- **Idiomas**: mais de 100 para texto e 12 para arquivos, com o idioma de origem detectado quando você o omite

## Obtenha uma chave

Crie uma conta em <https://equalang.com> e gere uma chave em <https://equalang.com/api-keys>. Contas novas vêm com créditos gratuitos, o suficiente para traduzir um documento e experimentar.

Salve-a uma vez em `~/.config/equalang/.env` e ela continua valendo: em qualquer agente (Claude Code, Codex, WorkBuddy, Cursor ou outro), em cada nova sessão e depois de reinstalar ou atualizar, sem export. O servidor MCP do Equalang lê o mesmo arquivo.

```bash
# Troque el_your_key pela sua chave
mkdir -p ~/.config/equalang && echo 'EQUALANG_API_KEY=el_your_key' > ~/.config/equalang/.env && chmod 600 ~/.config/equalang/.env
```

Primeiro é verificada a variável de ambiente `EQUALANG_API_KEY`; o arquivo só é lido quando ela não existe - assim um projeto pode usar outra chave.

## Instalação

Requer `python3` 3.8 ou superior, e nada mais: o script usa apenas a biblioteca padrão.

O jeito mais curto é colar isto no seu agente:

> Instale a skill do Equalang seguindo as instruções em https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (manual)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Prefere só para um projeto? Clone em `.claude/skills/equalang` dentro do repositório.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

O Codex também lê `.agents/skills/` dentro de um repositório, para restringir a skill a um projeto.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Só para um projeto: clone em `.codebuddy/skills/equalang` na raiz do projeto.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro e outros</b></summary>

Esta é uma [Agent Skill](https://agentskills.io) comum: uma pasta com um `SKILL.md` dentro. Todo cliente que implementa o padrão carrega a mesma pasta; só muda o diretório que ele examina, e cada um documenta o seu. Clone o repositório nesse diretório e a skill está instalada.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Prefere um servidor MCP? O [equalang-mcp](https://github.com/equalang/equalang-mcp) oferece as mesmas operações como ferramentas e funciona também no Claude Desktop, Cursor, Windsurf, Cline e OpenCode.

## Comandos

```bash
# Quanto custaria? Gratuito, e nada começa a ser traduzido
python3 scripts/equalang.py estimate report.pdf

# Traduzir um arquivo; o resultado fica ao lado do original
python3 scripts/equalang.py translate report.pdf --to zh-CN

# A partir de uma URL pública (o próprio Equalang a busca), para uma pasta
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# O que uma gravação diz, como texto com marcação de tempo
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Textos curtos, em ordem
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Um único texto longo, cortado por frases pelo Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Um job que ficou em execução, o saldo e os códigos de idioma
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Todo comando imprime JSON: onde os arquivos foram escritos e quanto custaram, ou o que deu errado. Acrescente `--help` a qualquer comando para ver suas opções. O próprio agente lê [SKILL.md](../SKILL.md).

Os códigos de idioma têm o formato `en`, `zh-CN`, `ja`. Rode `languages` para listá-los, ou `languages chinese` para buscar. Um job leva minutos: o comando espera, e `status <job_id>` o retoma se você interromper.

## Links

- [Equalang](https://equalang.com) · [Preços](https://equalang.com/pricing) · [Documentação para desenvolvedores](https://equalang.com/developers)
- API para agentes: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp): as mesmas operações como servidor MCP
- Dúvidas: <support@equalang.com>

## Licença

[Apache-2.0](../LICENSE) © Equalang
