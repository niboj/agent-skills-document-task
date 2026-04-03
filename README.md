# agent-skills-textes-utilitaires

Bibliotheque de skills Markdown pour conserver, creer et faire evoluer des skills utilitaires orientees manipulation et transformation de texte.

## Objectif

Ce depot sert de base de travail pour:

- capitaliser des skills reutilisables autour du texte;
- maintenir une structure simple, portable et validable;
- demarrer rapidement de nouveaux skills avec des gabarits et des utilitaires;
- installer le catalogue dans Codex ou OpenCode.

Le coeur du depot reste portable. Les skills publiees ici peuvent etre copiees ou synchronisees dans `.agents/skills/`, `.claude/skills/` ou `.opencode/skills/`.

## Positionnement

Le catalogue cible surtout les usages suivants:

- nettoyage et normalisation de texte brut;
- reformulation selon un ton, un public ou une contrainte;
- synthese et condensation d information;
- extraction de structure depuis un texte libre;
- conversion entre formats textuels simples comme notes, listes, tableaux Markdown ou fiches.

Il ne vise pas a stocker de la logique applicative, des workflows metier lourds ou des scripts complexes qui depassent le cadre d une transformation textuelle.

## Structure du depot

```text
.
|-- AGENTS.MD
|-- README.md
|-- docs/
|   `-- skill-authoring-playbook.md
|-- evals/
|   `-- evals.json
|-- examples/
|   |-- derived-skills/
|   `-- raw-sources/
|-- references/
|   |-- agent-skills-spec-summary.md
|   |-- description-conventions.md
|   |-- naming-conventions.md
|   |-- platform-compatibility-matrix.md
|   |-- reference-structure-conventions.md
|   `-- script-decision-matrix.md
|-- skills/
|   |-- traduction-anglais-francais/
|   |-- texte-extraction-structuree/
|   |-- texte-nettoyage-normalisation/
|   |-- texte-reformulation-ciblee/
|   `-- texte-synthese-structuree/
|-- templates/
|   |-- skill-minimal/
|   |-- skill-advanced/
|   |-- evals.json
|   |-- platform-compatibility.md
|   |-- reference-index.md
|   `-- review-checklist.md
`-- utilities/
    |-- check_all_skills.py
    |-- check_skill.py
    |-- init_skill.py
    |-- install_codex_skills.py
    `-- install_opencode_skills.py
```

## Skills de depart

- `traduction-anglais-francais`: traduit un texte de l anglais vers le francais avec plusieurs modes de traduction.
- `texte-nettoyage-normalisation`: nettoie un texte brut, harmonise la forme et preserve le sens.
- `texte-reformulation-ciblee`: adapte un contenu a un public, un ton ou une contrainte editoriale.
- `texte-synthese-structuree`: condense un contenu long en sortie concise et exploitable.
- `texte-extraction-structuree`: transforme un texte libre en listes, champs, tableaux ou fiches.

## Workflow recommande

1. Creer ou choisir le skill adapte au besoin.
2. Garder un perimetre etroit: une transformation principale par skill.
3. Placer les details stables dans `references/` seulement si cela change vraiment l execution.
4. Ajouter des cas d evaluation realistes avant d etendre un skill.
5. Valider la structure localement.

## Creer un nouveau skill

Initialisation minimale:

```bash
python3 utilities/init_skill.py \
  --name texte-conversion-compte-rendu \
  --description "Use this skill when you need a repeatable workflow to convert rough notes into a clean meeting summary."
```

Avec references et evaluations:

```bash
python3 utilities/init_skill.py \
  --name texte-fiche-decision \
  --description "Use this skill when you need to transform unstructured discussion notes into a decision brief with explicit sections." \
  --with-references \
  --with-evals
```

## Validation

Verifier un skill:

```bash
python3 utilities/check_skill.py skills/texte-synthese-structuree
```

Verifier tout le depot:

```bash
python3 utilities/check_all_skills.py
```

## Installation locale

Installer dans un repertoire de skills compatible Codex:

```bash
python3 utilities/install_codex_skills.py --source skills
```

Installer dans OpenCode:

```bash
python3 utilities/install_opencode_skills.py --source skills
```

## Regles de qualite

- un skill par responsabilite principale;
- un `SKILL.md` court, procedural et declenchable;
- une `description` qui dit explicitement quand utiliser le skill;
- des references chargees a la demande, jamais en vrac;
- des sorties observables et verifiables;
- des exemples et evaluations qui ressemblent a de vraies demandes de transformation de texte.
