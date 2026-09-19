# Skill Equalang

[English](../README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Türkçe](README.tr.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

Un [Agent Skill](https://github.com/anthropics/skills) qui donne [Equalang](https://equalang.com) à Claude Code, Codex, Cursor et d'autres agents : traduire des fichiers entiers en conservant leur mise en page, transcrire des enregistrements, traduire des chaînes de texte par lots.

- **Documents** - PDF, DOCX, PPTX, XLSX, EPUB, HTML, TXT - reviennent dans le même format.
- **Sous-titres** (SRT, VTT) et **images** (JPG, PNG, WebP, BMP).
- **Audio et vidéo** reviennent sous forme de sous-titres traduits, ou de transcription dans la langue parlée.

## Installation

Collez ceci à votre agent :

> Install the Equalang skill by following the instructions at https://equalang.com/install/skill-install.md

Ou à la main - un skill est un dossier :

```bash
git clone https://github.com/equalang/equalang-skill ~/.claude/skills/equalang     # Claude Code
git clone https://github.com/equalang/equalang-skill ~/.codex/skills/equalang      # Codex
export EQUALANG_API_KEY=el_...        # créez-en une sur https://equalang.com/api-keys
```

En tant que plugin Claude Code : `/plugin marketplace add equalang/equalang-skill`, puis `/plugin install equalang@equalang`.

`python3` (3.8+) suffit ; il n'y a rien à installer avec `pip install`.

## Ce que l'agent exécute

```bash
python3 scripts/equalang.py estimate report.pdf                  # combien cela coûterait-il ? (gratuit)
python3 scripts/equalang.py translate report.pdf --to zh-CN      # le résultat arrive à côté de la source
python3 scripts/equalang.py translate https://example.com/deck.pptx --to ja -o ./out
python3 scripts/equalang.py transcribe interview.mp3 --format srt --format txt
python3 scripts/equalang.py text "Save changes" "Delete project" --to de
python3 scripts/equalang.py text --file notes.md --to ja -o notes.ja.md   # un seul long texte, découpé par phrases par Equalang
python3 scripts/equalang.py status <job_id> · cancel <job_id> · balance · languages chinese
```

**Langues.** Les codes ressemblent à `en`, `zh-CN`, `ja`. Aucune liste n'est intégrée au skill : `languages` lit les codes et les noms depuis l'API en direct (`--kind text` pour l'ensemble plus large qu'accepte `text`), de sorte qu'une langue ajoutée par Equalang est disponible sans mise à jour.

**Crédits.** Le travail consomme les crédits du compte, le même solde que sur le site web. SKILL.md fait annoncer le coût par l'agent - d'après `estimate` - et obtenir un accord d'abord.

Chaque commande affiche un seul objet JSON - des chemins et des crédits, jamais le contenu des fichiers - ou `{"error", "code", "retryable"}` avec le code de sortie 1. [SKILL.md](../SKILL.md) est ce que lit l'agent.

## Comment il est construit

Les trois mêmes décisions que le [serveur MCP](https://github.com/equalang/equalang-mcp), qui propose les mêmes opérations sous forme d'outils :

1. **Un fichier ne passe jamais par le modèle** - les commandes reçoivent où se trouve un fichier (un chemin, ou une URL publique qu'Equalang récupère lui-même) et affichent où les résultats ont été écrits.
2. **Une tâche vit à l'intérieur d'une seule commande** - envoi, attente (avec les pauses que demande le `Retry-After` de l'API), téléchargement. Interrompre l'attente n'annule pas la tâche ; `status` la reprend.
3. **Les réponses de l'API sont répétées, pas devinées** - on ne retente que ce que l'API marque `retryable` ; le coût est le `quote` de l'API ; la liste des langues est lue dans son document OpenAPI ; un `Idempotency-Key` par tâche créée, de sorte qu'une réponse perdue ne peut pas devenir une seconde tâche facturée.

`python3 scripts/check_api.py` vérifie, sans clé, que chaque chemin et chaque champ utilisés par le script - et chaque format promis par SKILL.md - figurent toujours dans le contrat de l'API. L'API elle-même : <https://equalang.com/llms.txt>.

Apache-2.0.
