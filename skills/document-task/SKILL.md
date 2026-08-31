---
name: document-task
description: Utiliser cette competence lorsqu il faut analyser, transformer ou extraire des informations a partir de documents, particulierement lorsqu ils sont volumineux ou doivent etre traites avec reprise.
---

# document-task

## Objectif

Analyser, transformer ou extraire des informations a partir de documents sans charger inutilement le contenu complet dans le contexte du modele.

## Quand utiliser cette competence

- Quand un document est volumineux ou doit etre lu progressivement.
- Quand une tache documentaire doit pouvoir reprendre apres interruption.
- Quand la conversion, l indexation, la recherche, l ecriture et la validation doivent etre gerees par du code.

## Actions

- `prepare`
- `process`
- `resume`
- `status`
- `finalize`

## Procedure

1. Utiliser `bin/document-task prepare <fichier>` pour preparer le document.
2. Utiliser `bin/document-task process <document_id> <instruction> --output <fichier>` pour creer ou avancer une tache.
3. Utiliser `bin/document-task resume <task_id>` apres interruption ou compactage.
4. Utiliser `bin/document-task status <task_id>` pour lire l etat compact.
5. Utiliser `bin/document-task finalize <task_id>` pour assembler et valider le resultat.

Le skill gere automatiquement la resolution des fichiers, la conversion, l indexation, la lecture progressive, la recherche locale, les points de reprise, l ecriture securisee et la validation.

Ne pas lire manuellement un document volumineux si ce skill peut etre utilise.
Ne pas conserver l etat d une tache documentaire uniquement dans le contexte.

## Validation

- Les retours restent compacts.
- L etat persistant existe sur disque.
- Les fichiers generes sont UTF-8 et non vides.
- La reprise s appuie sur `state.json`, pas sur l historique de conversation.
