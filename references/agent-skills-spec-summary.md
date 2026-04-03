# Resume de la specification Agent Skills

Ce depot suit le format public Agent Skills et ses principes generaux de redaction.

## Regles de base

- Une competence est un dossier contenant au minimum `SKILL.md`.
- `SKILL.md` doit contenir un frontmatter YAML suivi d instructions en Markdown.
- Les champs de frontmatter requis sont `name` et `description`.
- `name` doit utiliser uniquement des lettres minuscules, des chiffres et des traits d union.
- Garder `SKILL.md` concis et deplacer le detail dans `references/`, `assets/` ou `scripts/` si necessaire.
- Rediger `description` pour le declenchement, pas seulement pour la documentation.
- Utiliser des scripts seulement si le determinisme ou la repetabilite le justifient.
- Preferer des evaluations realistes a des prompts artificiels.

## Politique du depot

- La documentation du depot peut etre redigee en francais.
- Les competences du depot peuvent etre redigees en francais quand cela sert clairement l usage cible.
- Les champs optionnels du frontmatter au dela de `name` et `description` doivent rester minimaux.
- Si `allowed-tools` est utilise, le traiter comme experimental et le documenter explicitement.
