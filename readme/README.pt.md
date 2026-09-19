# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português** · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Site](https://equalang.com) · [Preços](https://equalang.com/pricing) · [Documentação para desenvolvedores](https://equalang.com/developers) · [Chaves de API](https://equalang.com/api-keys)

> **Palavras-chave:** traduzir pdf, tradutor de pdf, traduzir pdf mantendo a formatação, tradutor de documentos, traduzir documento word, traduzir docx, traduzir powerpoint, traduzir excel, traduzir epub, traduzir legendas, tradutor de legendas srt, traduzir imagem, traduzir texto de imagem, traduzir vídeo, transcrever áudio em texto, tradutor com ia, agent skill, claude code skill, codex skill, translation api

**Traduza o arquivo, mantenha o layout.** Uma [Agent Skill](https://agentskills.io) para o [Equalang](https://equalang.com), um tradutor com IA que trabalha com arquivos inteiros: um PDF volta como PDF, uma apresentação como apresentação, com tabelas, imagens e fórmulas onde estavam. Também traduz legendas e imagens, transforma áudio e vídeo em legendas traduzidas ou em transcrição, e traduz strings em lote. Funciona no Claude Code, Codex, Cursor, CodeBuddy e em qualquer outro agente que carregue Agent Skills.

## Recursos

- **O formato que entra é o que sai**: PDF, DOCX, PPTX, XLSX, EPUB, HTML e TXT voltam no mesmo formato, ainda editáveis, com tabelas, imagens, fórmulas e layout de página no lugar
- **Legendas e imagens**: SRT e VTT mantêm a sincronização, opcionalmente com a linha original acima da tradução; JPG, PNG, WebP e BMP voltam com o texto da imagem traduzido
- **Áudio e vídeo**: MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM e MKV viram legendas traduzidas ou uma transcrição no idioma falado (SRT, VTT, TXT, JSON)
- **Texto em lote**: strings separadas traduzidas em ordem, ou um único texto longo (até 100.000 caracteres) que o próprio Equalang corta por frases; mais de 100 idiomas para texto, 12 para arquivos
- **Arquivos inteiros, sem copiar e colar**: até 100 MB por arquivo, a partir de um caminho ou de uma URL pública; nada para dividir em caixas de texto
- **Não gasta tokens**: o arquivo vai para o Equalang e volta um caminho; um PDF de 300 páginas nunca entra na conversa
- **O preço antes do job**: `estimate` responde, de graça, com o máximo que um job pode custar; jobs com falha ou cancelados não custam nada; uma gravação é cobrada pela fala efetivamente ouvida; os créditos nunca expiram
- **Nada para instalar**: um único script Python, só biblioteca padrão, Python 3.8+

## Obtenha uma chave

Crie uma conta em <https://equalang.com> e gere uma chave em <https://equalang.com/api-keys>. Contas novas começam com créditos gratuitos, o suficiente para passar um documento e ver o que volta.

```bash
export EQUALANG_API_KEY=el_your_key
```

Ou copie `.env.example` para `.env` neste diretório; ele é ignorado pelo git. A chave é exibida uma única vez; o Equalang guarda apenas um hash dela.

## Instalação

O jeito mais curto é colar isto no seu agente:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# Quanto custaria? Gratuito, e nada é iniciado
python3 scripts/equalang.py estimate report.pdf

# Traduzir um arquivo; o resultado fica ao lado do original
python3 scripts/equalang.py translate report.pdf --to zh-CN

# A partir de uma URL pública (o próprio Equalang a busca), para uma pasta
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# O que uma gravação diz, como texto com marcação de tempo
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Strings separadas, em ordem
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Um único texto longo, cortado por frases pelo Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Um job que ficou em execução, o saldo e os códigos de idioma
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Todo comando imprime um único objeto JSON (caminhos e créditos, nunca o conteúdo dos arquivos) ou `{"error", "code", "retryable"}` com código de saída 1. `--help` em qualquer comando lista suas opções. [SKILL.md](../SKILL.md) é o que o agente lê.

## Três coisas que vale a pena saber

**Idiomas.** Os códigos têm o formato `en`, `zh-CN`, `ja`. Não há lista embutida na skill: `languages` lê os códigos e nomes da API em produção (`--kind text` para o conjunto mais amplo que `text` aceita), então um idioma que o Equalang adicionar fica disponível sem atualização. Deixe o idioma de origem de fora para que ele seja detectado.

**Créditos.** O trabalho consome os créditos da conta, o mesmo saldo do site. O SKILL.md faz o agente informar o custo, obtido com `estimate`, e obter a concordância antes de iniciar um job.

**Jobs levam minutos.** O comando espera, pausando pelo tempo que o `Retry-After` da API pedir. Interrompê-lo não cancela o job: `status <job_id>` o retoma e faz o download do resultado.

## Perguntas frequentes

**O PDF traduzido mantém o layout?**
Sim, essa é a ideia. O texto é recolocado onde estava, e tabelas, imagens e fórmulas ficam no lugar; um DOCX, PPTX ou XLSX continua editável.

**Meu documento é enviado ao modelo?**
Não. O script envia o arquivo ao Equalang e imprime um caminho. Um artigo de 300 páginas não gasta tokens.

**Ele consegue traduzir o texto dentro de uma imagem?**
Sim. O texto de um JPG, PNG, WebP ou BMP é reconhecido, traduzido e redesenhado na imagem.

**Quanto custa um job?**
`estimate` informa antes de qualquer coisa começar, e é gratuito. Os preços estão em <https://equalang.com/pricing>.

## Como foi construída

As mesmas três decisões do [servidor MCP](https://github.com/equalang/equalang-mcp):

1. **Um arquivo nunca passa pelo modelo**: os comandos recebem onde o arquivo está (um caminho ou uma URL pública que o próprio Equalang busca) e imprimem onde os resultados foram gravados.
2. **Um job vive dentro de um único comando**: envio, espera, download. `status` retoma um job cuja espera foi interrompida.
3. **As respostas da API são repetidas, não adivinhadas**: tentar de novo só o que a API marca como `retryable`; o custo é o `quote` da API; a lista de idiomas é lida do documento OpenAPI dela; uma `Idempotency-Key` por job criado, de modo que uma resposta perdida não vira um segundo job cobrado.

`python3 scripts/check_api.py` verifica, sem chave, que todo caminho e campo usado pelo script, e todo formato que o SKILL.md promete, continua no contrato da API.

## Links

- [Equalang](https://equalang.com) · [Preços](https://equalang.com/pricing) · [Documentação para desenvolvedores](https://equalang.com/developers)
- API para agentes: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp): as mesmas operações como servidor MCP
- Dúvidas: <support@equalang.com>

## Licença

[Apache-2.0](../LICENSE) © Equalang
