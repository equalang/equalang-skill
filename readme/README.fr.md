# equalang-skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skills-open_standard-6E56CF.svg)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-3776AB.svg)](https://python.org)

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[Site web](https://equalang.com) · [Tarifs](https://equalang.com/pricing) · [Documentation développeur](https://equalang.com/developers) · [Clés API](https://equalang.com/api-keys)

> **Mots-clés :** traduire un pdf, traducteur pdf, traduire un pdf en gardant la mise en page, traduction de documents, traduire un document word, traduire un docx, traduire un powerpoint, traduire un fichier excel, traduire un epub, traduire des sous-titres, traducteur srt, traduire une image, traduire le texte d'une image, traduire une vidéo, transcription audio en texte, traducteur ia, agent skill, claude code skill, codex skill, translation api

**Traduisez le fichier, gardez la mise en page.** Un [Agent Skill](https://agentskills.io) pour [Equalang](https://equalang.com), un traducteur IA qui travaille sur des fichiers entiers : un PDF revient en PDF, une présentation en présentation, tableaux, images et formules à leur place. Il traduit aussi les sous-titres et les images, transforme l'audio et la vidéo en sous-titres traduits ou en transcription, et traduit des chaînes de texte par lots. Fonctionne dans Claude Code, Codex, Cursor, CodeBuddy et tout autre agent qui charge des Agent Skills.

## Fonctionnalités

- **Le format à l'entrée, le même à la sortie** : PDF, DOCX, PPTX, XLSX, EPUB, HTML et TXT reviennent dans le même format, toujours modifiables, tableaux, images, formules et mise en page à leur place
- **Sous-titres et images** : SRT et VTT gardent leur minutage, avec au besoin la ligne d'origine au-dessus de la traduction ; JPG, PNG, WebP et BMP reviennent avec le texte de l'image traduit
- **Audio et vidéo** : MP3, M4A, WAV, FLAC, OGG, AAC, Opus, MP4, MOV, WebM et MKV deviennent des sous-titres traduits, ou une transcription dans la langue parlée (SRT, VTT, TXT, JSON)
- **Texte par lots** : des chaînes séparées traduites dans l'ordre, ou un seul long texte (jusqu'à 100 000 caractères) qu'Equalang découpe lui-même par phrases ; plus de 100 langues pour le texte, 12 pour les fichiers
- **Des fichiers entiers, sans copier-coller** : jusqu'à 100 MB par fichier, depuis un chemin ou une URL publique ; rien à découper dans des zones de texte
- **Aucun token consommé** : le fichier part chez Equalang et un chemin revient ; un PDF de 300 pages n'entre jamais dans la conversation
- **Le prix avant la tâche** : `estimate` répond, gratuitement, avec le coût maximal d'une tâche ; les tâches échouées ou annulées ne coûtent rien ; un enregistrement est facturé pour la parole réellement entendue ; les crédits n'expirent jamais
- **Rien à installer** : un seul script Python, bibliothèque standard uniquement, Python 3.8+

## Obtenir une clé

Inscrivez-vous sur <https://equalang.com> et créez une clé sur <https://equalang.com/api-keys>. Les nouveaux comptes démarrent avec des crédits gratuits, de quoi faire passer un document et voir ce qui en ressort.

```bash
export EQUALANG_API_KEY=el_your_key
```

Ou copiez `.env.example` vers `.env` dans ce répertoire ; il est ignoré par git. La clé n'est affichée qu'une fois ; Equalang n'en conserve qu'un hash.

## Installation

Le plus court : collez ceci à votre agent.

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

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
# Combien cela coûterait-il ? Gratuit, et rien n'est lancé
python3 scripts/equalang.py estimate report.pdf

# Traduire un fichier ; le résultat arrive à côté de la source
python3 scripts/equalang.py translate report.pdf --to zh-CN

# Depuis une URL publique (Equalang la récupère lui-même), vers un dossier
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out

# Ce que dit un enregistrement, sous forme de texte horodaté
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt

# Des chaînes séparées, dans l'ordre
python3 scripts/equalang.py text "Save changes" "Delete project" --to de

# Un seul long texte, découpé par phrases par Equalang
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md

# Une tâche laissée en cours, le solde et les codes de langue
python3 scripts/equalang.py status <job_id>
python3 scripts/equalang.py cancel <job_id>
python3 scripts/equalang.py balance
python3 scripts/equalang.py languages chinese
```

Chaque commande affiche un seul objet JSON (des chemins et des crédits, jamais le contenu des fichiers) ou `{"error", "code", "retryable"}` avec le code de sortie 1. `--help` sur n'importe quelle commande liste ses options. [SKILL.md](../SKILL.md) est ce que lit l'agent.

## Trois choses à savoir

**Langues.** Les codes ressemblent à `en`, `zh-CN`, `ja`. Aucune liste n'est intégrée au skill : `languages` lit les codes et les noms depuis l'API en direct (`--kind text` pour l'ensemble plus large qu'accepte `text`), de sorte qu'une langue ajoutée par Equalang est disponible sans mise à jour. N'indiquez pas la langue source pour qu'elle soit détectée.

**Crédits.** Le travail consomme les crédits du compte, le même solde que sur le site web. SKILL.md fait annoncer le coût par l'agent, d'après `estimate`, et obtenir un accord avant de lancer une tâche.

**Les tâches prennent des minutes.** La commande attend, en marquant les pauses que demande le `Retry-After` de l'API. L'interrompre n'annule pas la tâche : `status <job_id>` la reprend et télécharge le résultat.

## Questions fréquentes

**Le PDF traduit garde-t-il sa mise en page ?**
Oui, c'est tout l'intérêt. Le texte est remis là où il était, et les tableaux, images et formules restent en place ; un DOCX, PPTX ou XLSX reste modifiable.

**Mon document est-il envoyé au modèle ?**
Non. Le script envoie le fichier à Equalang et affiche un chemin. Un article de 300 pages ne coûte aucun token.

**Peut-il traduire le texte à l'intérieur d'une image ?**
Oui. Le texte d'un JPG, PNG, WebP ou BMP est reconnu, traduit puis redessiné dans l'image.

**Combien coûte une tâche ?**
`estimate` le dit avant que quoi que ce soit ne démarre, et c'est gratuit. Les tarifs sont sur <https://equalang.com/pricing>.

## Comment il est construit

Les trois mêmes décisions que le [serveur MCP](https://github.com/equalang/equalang-mcp) :

1. **Un fichier ne passe jamais par le modèle** : les commandes reçoivent où se trouve un fichier (un chemin, ou une URL publique qu'Equalang récupère lui-même) et affichent où les résultats ont été écrits.
2. **Une tâche vit à l'intérieur d'une seule commande** : envoi, attente, téléchargement. `status` reprend une tâche dont l'attente a été interrompue.
3. **Les réponses de l'API sont répétées, pas devinées** : on ne retente que ce que l'API marque `retryable` ; le coût est le `quote` de l'API ; la liste des langues est lue dans son document OpenAPI ; un `Idempotency-Key` par tâche créée, de sorte qu'une réponse perdue ne peut pas devenir une seconde tâche facturée.

`python3 scripts/check_api.py` vérifie, sans clé, que chaque chemin et chaque champ utilisés par le script, ainsi que chaque format promis par SKILL.md, figurent toujours dans le contrat de l'API.

## Liens

- [Equalang](https://equalang.com) · [Tarifs](https://equalang.com/pricing) · [Documentation développeur](https://equalang.com/developers)
- API pour les agents : [llms.txt](https://equalang.com/llms.txt) · [llms-full.txt](https://equalang.com/llms-full.txt) · [OpenAPI](https://equalang.com/api/backend/v1/openapi.json)
- [equalang-mcp](https://github.com/equalang/equalang-mcp) : les mêmes opérations sous forme de serveur MCP
- Questions : <support@equalang.com>

## Licence

[Apache-2.0](../LICENSE) © Equalang
