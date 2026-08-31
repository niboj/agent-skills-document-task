# Playbook de conception

Ce guide explique comment creer de nouveaux skills dans ce depot sans perdre le positionnement "transformation de texte".

## 1. Partir d une transformation observable

Un bon skill de ce depot doit repondre a une question simple:

- quel texte entre;
- quelle transformation principale est attendue;
- quelle forme de sortie doit etre produite.

Exemples utiles:

- texte brut -> texte nettoye;
- note longue -> synthese structuree;
- texte libre -> tableau Markdown;
- brouillon -> version reformulee pour une audience cible.

Exemples a eviter:

- "mieux ecrire";
- "aider avec la documentation";
- "gerer les communications".

## 2. Garder un perimetre etroit

Si un skill commence a faire a la fois nettoyage, synthese, tonalite, extraction et classification, il est trop large.

Dans ce depot, il vaut mieux:

- un skill simple, bien declenchable;
- plusieurs skills complementaires;
- une description qui dit clairement quand l utiliser.

## 3. Rendre la sortie observable

Le resultat doit etre verifiable sans debat interminable:

- liste de points cles;
- tableau Markdown;
- texte reformule;
- fiche a sections fixes.

Eviter les formulations trop vagues sur la "qualite" sans format de sortie.

## 4. Ajouter des references avec parcimonie

Ajouter `references/` seulement si cela change l execution:

- glossaire obligatoire;
- gabarit de sortie stable;
- regles de ton ou de structure;
- taxonomie locale.

Ne pas deplacer dans `references/` de longues explications generiques que le skill peut porter lui-meme.

## 5. Evaluer avec des demandes reelles

Chaque nouveau skill devrait etre teste avec:

- un cas simple;
- un cas ambigu;
- un cas qui force les limites du skill.

Les attentes doivent porter sur le comportement observable, pas sur des formulations exactes.
