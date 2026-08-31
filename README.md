# agent-skills-textes-utilitaires

Bibliotheque de competences Markdown pour conserver, creer et faire evoluer des competences utilitaires orientees manipulation et transformation de texte.

## Objectif

Ce depot sert de base de travail pour:

- capitaliser des competences reutilisables autour du texte;
- maintenir une structure simple, portable et validable;
- demarrer rapidement de nouvelles competences avec des gabarits et des utilitaires;
- installer le catalogue dans Codex ou OpenCode.

Le coeur du depot reste portable. Les competences publiees ici peuvent etre copiees ou synchronisees dans `.agents/skills/`, `.claude/skills/` ou `.opencode/skills/`.

## Positionnement

Le catalogue cible surtout les usages suivants:

- analyse de documentation et extraction de constats;
- redaction de documentation informationnelle;
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
|   `-- guide-redaction-competences.md
|-- evals/
|   `-- evaluations.json
|-- examples/
|   |-- derived-skills/
|   `-- raw-sources/
|-- references/
|   |-- resume-specification-agent-skills.md
|   |-- conventions-description.md
|   |-- conventions-nommage.md
|   |-- matrice-compatibilite-plateformes.md
|   |-- conventions-structure-references.md
|   `-- matrice-decision-scripts.md
|-- skills/
|   |-- analyse-documentation/
|   |-- redaction-documentation-informationnelle/
|   |-- traduction-anglais-francais/
|   |-- texte-extraction-structuree/
|   |-- texte-nettoyage-normalisation/
|   |-- texte-reformulation-ciblee/
|   `-- texte-synthese-structuree/
|-- templates/
|   |-- skill-minimal/
|   |-- skill-advanced/
|   |-- evaluations.json
|   |-- compatibilite-plateformes.md
|   |-- index-references.md
|   `-- checklist-revue.md
`-- utilities/
    |-- verifier_toutes_competences.py
    |-- verifier_competence.py
    |-- initialiser_competence.py
    |-- installer_competences_codex.py
    `-- installer_competences_opencode.py
```

## Competences de depart

- `analyse-documentation`: analyse un texte documentaire et produit une synthese structuree avec constats, risques, limites et conclusions.
- `redaction-documentation-informationnelle`: redige ou normalise un article de documentation informationnelle clair, neutre et reutilisable.
- `traduction-anglais-francais`: traduit un texte de l anglais vers le francais avec plusieurs modes de traduction.
- `texte-nettoyage-normalisation`: nettoie un texte brut, harmonise la forme et preserve le sens.
- `texte-reformulation-ciblee`: adapte un contenu a un public, un ton ou une contrainte editoriale.
- `texte-synthese-structuree`: condense un contenu long en sortie concise et exploitable.
- `texte-extraction-structuree`: transforme un texte libre en listes, champs, tableaux ou fiches.

## Workflow recommande

1. Creer ou choisir la competence adaptee au besoin.
2. Garder un perimetre etroit: une transformation principale par competence.
3. Placer les details stables dans `references/` seulement si cela change vraiment l execution.
4. Ajouter des cas d evaluation realistes avant d etendre un skill.
5. Valider la structure localement.

## Creer une nouvelle competence

Initialisation minimale:

```bash
python3 utilities/initialiser_competence.py \
  --name texte-conversion-compte-rendu \
  --description "Utiliser cette competence lorsqu il faut convertir des notes brutes en compte rendu propre et repetable."
```

Avec references et evaluations:

```bash
python3 utilities/initialiser_competence.py \
  --name texte-fiche-decision \
  --description "Utiliser cette competence lorsqu il faut transformer des notes de discussion non structurees en fiche de decision avec sections explicites." \
  --with-references \
  --with-evals
```

## Validation

Verifier une competence:

```bash
python3 utilities/verifier_competence.py skills/texte-synthese-structuree
```

Verifier tout le depot:

```bash
python3 utilities/verifier_toutes_competences.py
```

## Installation locale

Installer dans un repertoire de skills compatible Codex:

```bash
python3 utilities/installer_competences_codex.py --skills-root skills
```

Installer dans OpenCode:

```bash
python3 utilities/installer_competences_opencode.py --skills-root skills
```

## Regles de qualite

- une competence par responsabilite principale;
- un `SKILL.md` court, procedural et declenchable;
- une `description` qui dit explicitement quand utiliser la competence;
- des references chargees a la demande, jamais en vrac;
- des sorties observables et verifiables;
- des exemples et evaluations qui ressemblent a de vraies demandes de transformation de texte.
