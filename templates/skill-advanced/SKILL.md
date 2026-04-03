---
name: replace-me
description: Utiliser cette competence lorsqu il faut un workflow de transformation de texte de haute qualite avec regles locales, references reutilisables ou validation structuree.
---

# Skill: replace me

## Objectif

Produire une transformation textuelle fiable quand le resultat depend de conventions locales, de gabarits ou de validations supplementaires.

## Quand utiliser cette competence

- Quand la sortie doit suivre un schema fixe.
- Quand un glossaire, une taxonomie ou un gabarit local change l execution.
- Quand une validation explicite doit etre appliquee avant finalisation.

## Entrees

- Le texte source
- Le resultat attendu
- Les references locales utiles

## Workflow

Progression:
- [ ] Identifier la transformation principale
- [ ] Charger seulement les references pertinentes
- [ ] Produire une premiere sortie
- [ ] Verifier la structure et le fond
- [ ] Corriger les ecarts

## Procedure

1. Confirmer l entree, la sortie et les contraintes de structure.
2. Lire uniquement les references qui changent la maniere de transformer le texte.
3. Suivre le chemin par defaut avant toute variante.
4. Rendre visibles les hypotheses et zones d incertitude.
5. Valider la sortie avec la checklist ou le script prevu.

## Validation

- Les sections ou champs attendus sont presents.
- Le texte final est reutilisable sans retraitement majeur.
- Les elements inventes ou supposes sont evites ou signales.
- Les references locales sont respectees.

## Cas d escalade

- source trop incomplete;
- contraintes contradictoires;
- format de sortie non defini et impossible a inferer proprement.
