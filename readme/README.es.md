# Skill de Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Un [Agent Skill](https://github.com/anthropics/skills) que da [Equalang](https://equalang.com) a Claude Code, Codex, Cursor y otros agentes: traducir archivos enteros conservando su maquetación, transcribir grabaciones, traducir cadenas de texto en lote.

- **Documentos** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - vuelven en el mismo formato.
- **Subtítulos** (SRT, VTT) e **imágenes** (JPG, PNG, WebP, BMP).
- **Audio y vídeo** vuelven como subtítulos traducidos, o como transcripción en el idioma hablado.

## Instalación

Pega esto a tu agente:

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

O a mano - un skill es una carpeta:

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # crea una en https://equalang.com/api-keys
```

Como plugin de Claude Code: `/plugin marketplace add equalang/equalang-skill`, y luego `/plugin install equalang@equalang`.

`python3` (3.8+) es todo lo que necesita; no hay nada que instalar con `pip install`.

## Lo que ejecuta el agente

```bash
python3 scripts/equalang.py estimate report.pdf                  # ¿cuánto costaría? (gratis)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # el resultado queda junto al original
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # un texto largo, que Equalang corta por frases
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Idiomas.** Los códigos tienen la forma `en`, `zh-CN`, `ja`. El skill no incluye ninguna lista: `languages` lee los códigos y los nombres de la API en vivo (`--kind text` para el conjunto más amplio que admite `text`), de modo que un idioma que Equalang añada está disponible sin actualizar.

**Créditos.** El trabajo gasta los créditos de la cuenta, el mismo saldo que en el sitio web. SKILL.md hace que el agente diga el coste - a partir de `estimate` - y obtenga la conformidad primero.

Cada comando imprime un único objeto JSON - rutas y créditos, nunca el contenido de los archivos - o `{"error", "code", "retryable"}` con código de salida 1. [SKILL.md](../SKILL.md) es lo que lee el agente.

## Cómo está construido

Las mismas tres decisiones que el [servidor MCP](https://github.com/equalang/equalang-mcp), que ofrece las mismas operaciones como herramientas:

1. **Un archivo nunca pasa por el modelo** - los comandos reciben dónde está un archivo (una ruta, o una URL pública que Equalang descarga por su cuenta) e imprimen dónde se escribieron los resultados.
2. **Un trabajo vive dentro de un solo comando** - subir, esperar (con las pausas que pida el `Retry-After` de la API), descargar. Interrumpir la espera no cancela el trabajo; `status` lo retoma.
3. **Las respuestas de la API se repiten, no se adivinan** - se reintenta solo lo que la API marca como `retryable`; el coste es el `quote` de la API; la lista de idiomas se lee de su documento OpenAPI; un `Idempotency-Key` por trabajo creado, de modo que una respuesta perdida no puede convertirse en un segundo trabajo cobrado.

`python3 scripts/check_api.py` verifica, sin clave, que cada ruta y cada campo que usa el script - y cada formato que promete SKILL.md - sigue en el contrato de la API. La API en sí: <https://equalang.com/llms.txt>.

Apache-2.0.
