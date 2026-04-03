# Skills

Ce dossier contient le catalogue principal des skills de transformation de texte.

## Regles communes

- un dossier par skill;
- un `SKILL.md` obligatoire;
- un nom de dossier identique au champ `name`;
- une description orientee declenchement;
- des references uniquement si elles changent vraiment la maniere d executer le skill;
- un coeur portable prioritaire pour `.agents/skills/`, `.claude/skills/` et `.opencode/skills/`.

## Skills fournies

- `traduction-anglais-francais`
- `texte-nettoyage-normalisation`
- `texte-reformulation-ciblee`
- `texte-synthese-structuree`
- `texte-extraction-structuree`

## Ligne editoriale

Chaque skill doit resoudre une transformation textuelle principale avec:

- une entree textuelle identifiable;
- une procedure simple;
- une sortie textuelle observable;
- une validation legere mais concrete.
