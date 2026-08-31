# Matrice de compatibilite des plateformes

Ce depot vise un noyau portable pour Agent Skills, avec les comportements specifiques documentes explicitement.

## Noyau portable partage

- Un dossier par competence
- Point d entree `SKILL.md`
- Frontmatter YAML
- Champs `name` et `description`
- Corps en Markdown
- `references/`, `scripts/`, `assets/`, `evals/` en option

## Chemins de decouverte

### Codex / organisation generique compatible agent

- `.agents/skills/<name>/SKILL.md`
- `~/.agents/skills/<name>/SKILL.md`

### Claude Code

- `.claude/skills/<name>/SKILL.md`
- `~/.claude/skills/<name>/SKILL.md`

### OpenCode

- `.opencode/skills/<name>/SKILL.md`
- `~/.config/opencode/skills/<name>/SKILL.md`
- lit aussi les organisations `.claude/skills/` et `.agents/skills/`

## Portabilite du frontmatter

### Portable sur tous les environnements cibles

- `name`
- `description`

### Champs optionnels documentes par OpenCode

- `license`
- `compatibility`
- `metadata`

### Champs optionnels specifiques a Claude

- `disable-model-invocation`
- `allowed-tools`
- `model`
- `effort`
- `context`
- `agent`

## Differences de comportement notables

### Claude Code

- `description` est recommandee et utilisee pour le chargement automatique.
- Les descriptions de plus d environ 250 caracteres sont tronquees dans la liste des competences.
- `name` est optionnel dans Claude, mais il vaut mieux le conserver pour la portabilite.

### OpenCode

- Seuls `name`, `description`, `license`, `compatibility` et `metadata` sont reconnus dans le frontmatter.
- Les champs de frontmatter inconnus sont ignores.
- `description` doit rester entre 1 et 1024 caracteres.

### Valeur par defaut portable du depot

- Utiliser seulement `name` et `description` dans les gabarits fournis.
- Ajouter des metadonnees specifiques a une plateforme uniquement dans des variantes assumees.

## Recommandations

- Garder les gabarits par defaut sur le noyau portable uniquement.
- Mettre les indications specifiques aux plateformes dans les references, pas dans chaque frontmatter.
- Si des champs specifiques a Claude sont utilises, isoler ce choix dans une note de compatibilite.
- Considerer tout frontmatter non portable comme une option explicite, pas comme la valeur par defaut.
