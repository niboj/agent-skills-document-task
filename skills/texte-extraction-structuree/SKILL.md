---
name: texte-extraction-structuree
description: Use this skill when you need to extract structured fields, lists, tables, or factual elements from unstructured text.
---

# Skill: texte-extraction-structuree

## Goal

Transformer un texte libre en structure exploitable: champs, tableau Markdown, liste de faits, fiche ou sectionnement stable.

## When to use

- Quand l information est melangee dans un texte narratif ou conversationnel.
- Quand il faut isoler des entites, attributs, decisions, dates, actions, contraintes ou questions.
- Quand le resultat attendu doit etre reutilisable dans un autre artefact.

## Inputs

- Le texte source
- Le schema de sortie attendu, s il est connu
- Les regles de classement ou de priorisation, si elles existent

## Procedure

1. Reperer les informations observables qui peuvent etre sorties sans speculation.
2. Definir un schema minimal si aucun schema n est fourni.
3. Extraire les elements et les ranger dans des champs ou sections stables.
4. Distinguer les faits explicites, les inférences faibles et les inconnues.
5. Preferer un format simple et reutilisable, par exemple une table Markdown ou une fiche a rubriques.

## Validation

- Chaque element extrait est rattachable a la source.
- Le schema de sortie est coherent et stable.
- Les zones non determinees sont laissees vides ou marquees explicitement.
- La sortie peut etre reutilisee sans relire tout le texte source.
