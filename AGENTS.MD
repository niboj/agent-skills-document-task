# AGENTS

## Portee

Ces instructions s appliquent a tout le depot.

## Objectif du depot

- Maintenir une bibliotheque de skills Markdown reutilisables pour manipuler, transformer et restructurer du texte.
- Privilegier des skills concises, stables et faciles a declencher.
- Conserver un noyau portable vers Codex, Claude Code et OpenCode.

## Regles de travail

- Avant de modifier un skill, lire son `SKILL.md` et seulement les references directement utiles.
- Preserver une responsabilite unique par skill: nettoyage, reformulation, synthese, extraction ou conversion ciblee.
- Eviter les skills fourre-tout qui melangent ton, structure, metier et format dans le meme workflow.
- Ne pas ajouter de script si une procedure Markdown suffit.
- Si une sous-arborescence contient un autre `AGENTS.MD`, cette regle locale prime.

## Workflow recommande pour une nouvelle competence

1. Cadrer la transformation textuelle principale.
2. Definir le declenchement exact dans la `description`.
3. Ecrire une procedure courte avec un chemin par defaut.
4. Ajouter des references seulement si elles changent reellement l execution.
5. Ajouter des cas d evaluation proches de demandes reelles.
6. Valider avec `utilities/check_skill.py`.

## Regles specifiques a ce depot

- Les skills peuvent etre redigees en francais quand le besoin est local, mais la `description` doit rester tres explicite pour le declenchement.
- Le `SKILL.md` doit expliquer quand utiliser le skill, quelles transformations il effectue et comment verifier la sortie.
- Preferer des formats de sortie textuels simples: listes, tableaux Markdown, fiches, sections nommees.
- Les references doivent rester courtes, stables et chargeables a la demande.
- Les utilitaires du depot doivent rester non interactifs.

## Validation minimale

- Verifier que les chemins cites existent.
- Verifier que le nom du dossier correspond au champ `name`.
- Verifier que la `description` contient une formule de declenchement explicite.
- Verifier que les sections `## Objectif`, `## Quand utiliser cette competence` et `## Procedure` sont presentes.
- Verifier que la sortie attendue est observable et evaluable.
