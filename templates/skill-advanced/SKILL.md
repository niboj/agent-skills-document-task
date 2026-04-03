---
name: replace-me
description: Use this skill when you need a high-quality text transformation workflow with local rules, reusable references, or structured validation.
---

# Skill: replace me

## Goal

Produire une transformation textuelle fiable quand le resultat depend de conventions locales, de gabarits ou de validations supplementaires.

## When to use

- Quand la sortie doit suivre un schema fixe.
- Quand un glossaire, une taxonomie ou un gabarit local change l execution.
- Quand une validation explicite doit etre appliquee avant finalisation.

## Inputs

- Le texte source
- Le resultat attendu
- Les references locales utiles

## Workflow

Progress:
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

## Escalation cases

- source trop incomplete;
- contraintes contradictoires;
- format de sortie non defini et impossible a inferer proprement.
