# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Sitio web](https://equalang.com) · [Precios](https://equalang.com/pricing) · [Documentación para desarrolladores](https://equalang.com/developers) · [Claves de API](https://equalang.com/api-keys)

> **Palabras clave:** traducir pdf, traductor de pdf, traducir pdf manteniendo formato, traductor de documentos, traducir documento word, traducir docx, traducir powerpoint, traducir excel, traducir epub, traducir subtítulos, traductor srt, traducir imagen, traducir texto de una imagen, traducir vídeo, transcribir audio a texto, traductor con ia, agent skill, claude code skill, codex skill, translation api

**Traduce el archivo, conserva la maquetación.** Un [Agent Skill](https://agentskills.io) para [Equalang](https://equalang.com), un traductor con IA que trabaja con archivos enteros: un PDF vuelve como PDF y una presentación como presentación, con las tablas, las imágenes y las fórmulas donde estaban. También traduce subtítulos e imágenes, convierte audio y vídeo en subtítulos traducidos o en una transcripción, y traduce cadenas de texto en lote. Funciona en Claude Code, Codex, Cursor, CodeBuddy y cualquier otro agente que cargue Agent Skills.

## Características

- **El formato que entra es el que sale**: PDF, DOCX, PPTX, XLSX, EPUB, HTML y TXT vuelven en el mismo formato, todavía editables, con tablas, imágenes, fórmulas y maquetación de página en su sitio
- **Subtítulos e imágenes**: SRT y VTT conservan sus tiempos, con la línea original encima de la traducción si se quiere; JPG, PNG, WebP y BMP vuelven con el texto de la imagen traducido
- **Audio y vídeo**: MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM y MKV se convierten en subtítulos traducidos, o en una transcripción en el idioma hablado (SRT, VTT, TXT, JSON)
- **Texto en lote**: cadenas separadas traducidas en orden, o un solo texto largo (hasta 100.000 caracteres) que Equalang corta por frases por sí mismo
- **Más de 100 idiomas**: más de 100 para texto y 12 para archivos, con el idioma de origen detectado cuando no lo indicas

## Consigue una clave

Regístrate en <https://equalang.com> y crea una clave en <https://equalang.com/api-keys>. Las cuentas nuevas empiezan con créditos gratis, suficientes para pasar un documento y ver qué vuelve.

```bash
export EQUALANG_API_KEY=el_your_key
```

O copia `.env.example` a `.env` en este directorio; git lo ignora. La clave se muestra una sola vez; Equalang solo guarda un hash de ella.

## Instalación

Necesita `python3` 3.8 o posterior, y nada más: el script solo usa la biblioteca estándar.

La forma más corta es pegarle esto a tu agente:

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

¿Solo para un proyecto? Clónalo en `.claude/skills/equalang` dentro del repositorio.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex también lee `.agents/skills/` dentro de un repositorio, para limitarlo a un solo proyecto.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Solo para un proyecto: clónalo en `.codebuddy/skills/equalang`, en la raíz del proyecto.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro y otros</b></summary>

Es un [Agent Skill](https://agentskills.io) sin más: una carpeta con un `SKILL.md` dentro. Todo cliente que implementa el estándar carga la misma carpeta; solo cambia el directorio que examina, y cada uno documenta el suyo. Clona el repositorio en ese directorio y el skill queda instalado.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

¿Prefieres un servidor MCP? [equalang-mcp](https://github.com/equalang/equalang-mcp) ofrece las mismas operaciones como herramientas, y funciona también en Claude Desktop, Cursor, Windsurf, Cline y OpenCode.

## Comandos

```bash
# ¿Cuánto costaría? Gratis, y no se inicia nada
python3 scripts/equalang.py estimate report.pdf

# Traducir un archivo; el resultado queda junto al original
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Desde una URL pública (Equalang la descarga por su cuenta), a una carpeta
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Lo que dice una grabación, como texto con marcas de tiempo
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Cadenas separadas, en orden
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Un solo texto largo, que Equalang corta por frases
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Un trabajo que quedó en marcha, el saldo y los códigos de idioma
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Cada comando imprime un único objeto JSON (rutas y créditos, nunca el contenido de los archivos) o `{"error", "code", "retryable"}` con código de salida 1. `--help` en cualquier comando lista sus opciones. [SKILL.md](../SKILL.md) es lo que lee el agente.

Los códigos de idioma tienen la forma `en`, `zh-CN`, `ja`; `languages` los lee de la API en vivo, de modo que un idioma que Equalang añada está disponible sin actualizar. Los trabajos tardan minutos: el comando espera, y `status <job_id>` lo retoma si lo interrumpes.

## Preguntas frecuentes

**¿El PDF traducido conserva su maquetación?**
Sí, de eso se trata. El texto se vuelve a colocar donde estaba, y las tablas, las imágenes y las fórmulas se quedan en su sitio; un DOCX, PPTX o XLSX sigue siendo editable.

**¿Se envía mi documento al modelo?**
No. El script sube el archivo a Equalang e imprime una ruta. Un artículo de 300 páginas no gasta tokens.

**¿Puede traducir el texto que hay dentro de una imagen?**
Sí. El texto de un JPG, PNG, WebP o BMP se reconoce, se traduce y se vuelve a dibujar en la imagen.

**¿Cuánto cuesta un trabajo?**
`estimate` lo dice antes de que empiece nada, y es gratis. Los precios están en <https://equalang.com/pricing>.

## Enlaces

- [Equalang](https://equalang.com) · [Precios](https://equalang.com/pricing) · [Documentación para desarrolladores](https://equalang.com/developers)
- API para agentes: [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp): las mismas operaciones como servidor MCP
- Preguntas: <support@equalang.com>

## Licencia

[Apache-2.0](../LICENSE) © Equalang
