# Reference structure conventions

Utiliser `references/` seulement quand le skill a besoin d un appui stable et local.

## Quand ajouter des references

- un gabarit de sortie doit etre applique toujours de la meme maniere;
- une taxonomie locale influence la classification ou l extraction;
- un glossaire obligatoire change le vocabulaire de sortie;
- une grille de validation doit etre relue a la demande.

## Quand ne pas en ajouter

- pour des conseils generiques deja presents dans le `SKILL.md`;
- pour stocker des brouillons longs et non stabilises;
- pour compenser un skill trop flou.

## Structure recommandee

```text
skills/mon-skill/
|-- SKILL.md
`-- references/
    |-- output-template.md
    `-- glossary.md
```

Rester sur un niveau de profondeur faible et des noms explicites.
