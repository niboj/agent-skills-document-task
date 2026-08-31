# Competences

Ce dossier contient le catalogue principal des competences de transformation de texte.

## Regles communes

- un dossier par competence;
- un `SKILL.md` obligatoire;
- un nom de dossier identique au champ `name`;
- une description orientee declenchement;
- des references uniquement si elles changent vraiment la maniere d executer la competence;
- un coeur portable prioritaire pour `.agents/skills/`, `.claude/skills/` et `.opencode/skills/`.

## Competences fournies

- `analyse-documentation`
- `redaction-documentation-informationnelle`
- `traduction-anglais-francais`
- `texte-nettoyage-normalisation`
- `texte-reformulation-ciblee`
- `texte-synthese-structuree`
- `texte-extraction-structuree`

## Ligne editoriale

Chaque competence doit resoudre une transformation textuelle principale avec:

- une entree textuelle identifiable;
- une procedure simple;
- une sortie textuelle observable;
- une validation legere mais concrete.
