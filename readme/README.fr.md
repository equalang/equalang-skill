# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Site web](https://equalang.com) · [Tarifs](https://equalang.com/pricing) · [Documentation développeur](https://equalang.com/developers) · [Clés API](https://equalang.com/api-keys)

> **Mots-clés :** traduire un pdf, traducteur pdf, traduire un pdf en gardant la mise en page, traduction de documents, traduire un document word, traduire un docx, traduire un powerpoint, traduire un fichier excel, traduire un epub, traduire des sous-titres, traducteur srt, traduire une image, traduire le texte d'une image, traduire une vidéo, transcription audio en texte, traducteur ia, agent skill, claude code skill, codex skill, translation api

**Traduisez le fichier, gardez la mise en page.** Un [Agent Skill](https://agentskills.io) pour [Equalang](https://equalang.com), un traducteur IA qui travaille sur des fichiers entiers : un PDF revient en PDF, une présentation en présentation, tableaux, images et formules à leur place. Il traduit aussi les sous-titres et les images, transforme l'audio et la vidéo en sous-titres traduits ou en transcription, et traduit des textes courts par lots. Fonctionne dans Claude Code, Codex, Cursor, CodeBuddy et tout autre agent qui charge des Agent Skills.

## Fonctionnalités

- **Documents** : PDF, DOCX, PPTX, XLSX, EPUB, HTML et TXT reviennent dans le même format, toujours modifiables, tableaux, images, formules et mise en page à leur place
- **Sous-titres et images** : SRT et VTT gardent leur minutage, avec au besoin la ligne d'origine au-dessus de la traduction ; JPG, PNG, WebP et BMP reviennent avec le texte de l'image traduit
- **Audio et vidéo** : MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM et MKV deviennent des sous-titres traduits, ou une transcription dans la langue parlée (SRT, VTT, TXT, JSON)
- **Texte par lots** : des textes courts traduits dans l'ordre, ou un seul long texte (jusqu'à 100 000 caractères) qu'Equalang découpe lui-même par phrases
- **Langues** : plus de 100 pour le texte et 12 pour les fichiers, avec la langue source détectée quand vous l'omettez

## Obtenir une clé

Inscrivez-vous sur <https://equalang.com> et créez une clé sur <https://equalang.com/api-keys>. Les nouveaux comptes reçoivent des crédits gratuits, de quoi traduire un document pour essayer.

```bash
export EQUALANG_API_KEY=el_your_key
```

Ou copiez `.env.example` vers `.env` dans ce répertoire ; il est ignoré par git.

## Installation

Nécessite `python3` 3.8 ou plus récent, et rien d'autre : le script n'utilise que la bibliothèque standard.

Le plus court : collez ceci à votre agent.

> Installez le skill Equalang en suivant les instructions sur https://equalang.com/install/skill-install.md

<details open>
<summary><b>Claude Code</b> (plugin)</summary>

```
/plugin marketplace add equalang/equalang-skill
/plugin install equalang@equalang
```
</details>

<details>
<summary><b>Claude Code</b> (à la main)</summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang
```

Plutôt pour un seul projet ? Clonez dans `.claude/skills/equalang` au sein du dépôt.
</details>

<details>
<summary><b>OpenAI Codex</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.agents/skills/equalang
```

Codex lit aussi `.agents/skills/` à l'intérieur d'un dépôt, pour le limiter à un seul projet.
</details>

<details>
<summary><b>CodeBuddy / WorkBuddy</b></summary>

```bash
git clone https://github.com/equalang/equalang-skill ~/.codebuddy/skills/equalang
```

Pour un seul projet : clonez dans `.codebuddy/skills/equalang` à la racine du projet.
</details>

<details>
<summary><b>Cursor, Gemini CLI, OpenCode, Copilot, Goose, Amp, Kiro et les autres</b></summary>

C'est un simple [Agent Skill](https://agentskills.io) : un dossier contenant un `SKILL.md`. Tout client qui implémente le standard charge le même dossier ; seul change le répertoire qu'il parcourt, et chacun documente le sien. Clonez le dépôt dans ce répertoire et le skill est installé.

```bash
git clone https://github.com/equalang/equalang-skill
```
</details>

Vous préférez un serveur MCP ? [equalang-mcp](https://github.com/equalang/equalang-mcp) propose les mêmes opérations sous forme d'outils, et fonctionne aussi dans Claude Desktop, Cursor, Windsurf, Cline et OpenCode.

## Commandes

```bash
# Combien cela coûterait-il ? Gratuit, et aucune traduction ne démarre
python3 scripts/equalang.py estimate report.pdf

# Traduire un fichier ; le résultat arrive à côté de la source
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Depuis une URL publique (Equalang la récupère lui-même), vers un dossier
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Ce que dit un enregistrement, sous forme de texte horodaté
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Des textes courts, dans l'ordre
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Un seul long texte, découpé par phrases par Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Une tâche laissée en cours, le solde et les codes de langue
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Chaque commande affiche du JSON : où les fichiers ont été écrits et ce qu'ils ont coûté, ou ce qui n'a pas marché. Ajoutez `--help` à n'importe quelle commande pour voir ses options. L'agent, lui, lit [SKILL.md](../SKILL.md).

Les codes de langue ressemblent à `en`, `zh-CN`, `ja`. Lancez `languages` pour les lister, ou `languages chinese` pour chercher. Une tâche prend des minutes : la commande attend, et `status <job_id>` la reprend si vous l'interrompez.

## Liens

- [Equalang](https://equalang.com) · [Tarifs](https://equalang.com/pricing) · [Documentation développeur](https://equalang.com/developers)
- API pour les agents : [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) : les mêmes opérations sous forme de serveur MCP
- Questions : <support@equalang.com>

## Licence

[Apache-2.0](../LICENSE) © Equalang
