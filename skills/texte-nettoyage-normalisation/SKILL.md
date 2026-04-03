---
name: texte-nettoyage-normalisation
description: Use this skill when you need to clean up raw text, normalize formatting, remove noise, and preserve the original meaning.
---

# Skill: texte-nettoyage-normalisation

## Goal

Transformer un texte brut ou degrade en une version propre, lisible et coherente sans en changer le fond.

## When to use

- Quand le texte contient du bruit: doublons, artefacts de copier-coller, espaces erratiques, retours de ligne parasites ou ponctuation incoherente.
- Quand il faut harmoniser la casse, la structure des paragraphes, les listes ou les titres.
- Quand la priorite est la lisibilite et la fidelite, pas la reformulation de fond.

## Inputs

- Le texte source
- Les contraintes de preservation du sens
- Les preferences de format de sortie, si elles sont connues

## Procedure

1. Identifier le bruit a supprimer sans toucher au sens utile.
2. Recomposer la structure logique: titres, paragraphes, listes, sequences.
3. Normaliser la ponctuation, les espacements, les repetitions et les labels.
4. Preserver les termes, noms propres, chiffres et formulations qui portent un risque de sens.
5. Signaler explicitement les zones ambiguës si le texte source est degrade au point d imposer une interpretation.

## Validation

- Le texte final est plus lisible que la source.
- Les informations factuelles et nuances utiles sont conservees.
- Les artefacts de forme ont disparu ou sont reduits.
- Les corrections lourdes ou incertaines sont explicitees.
