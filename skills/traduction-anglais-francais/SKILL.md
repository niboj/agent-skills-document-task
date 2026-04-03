---
name: traduction-anglais-francais
description: Use this skill when you need to translate text from English to French in a faithful, natural, and professional way, with selectable translation modes.
---

# Skill: traduction-anglais-francais

## Goal

Traduire un texte de l anglais vers le francais de maniere fidele, naturelle et professionnelle.

## When to use

- Quand l utilisateur demande une traduction de l anglais vers le francais.
- Quand le texte doit etre traduit sans changer son sens ni ajouter d explication.
- Quand le niveau de langue ou le contexte impose un mode de traduction explicite.

## Inputs

- Le texte source en anglais
- Le mode de traduction demande, si precise
- Les contraintes utiles de ton, registre ou domaine

## Procedure

1. Identifier si l utilisateur demande un mode specifique ou emploie une formulation qui implique un mode.
2. Si aucun mode n est precise, utiliser le mode `naturel`.
3. Traduire le sens du texte sans faire de traduction mot a mot.
4. Preserver la structure du texte source, y compris les listes, titres et tableaux lorsque presents.
5. Conserver en anglais les termes reserves, techniques ou imposes par le format.
6. En cas d ambiguite importante, choisir la formulation la plus probable selon le contexte sans ajouter de commentaire sauf demande explicite.

## General rules

- Traduire le sens du texte, sans faire de traduction mot a mot.
- Produire un francais clair et correct.
- Respecter la structure du texte source.
- Conserver les listes, titres et tableaux lorsque presents.
- Ne pas ajouter d explication sauf demande explicite.
- En cas d ambiguite importante, choisir la formulation la plus probable selon le contexte.

## Terms to keep in English

- Ne pas traduire les termes reserves, techniques ou imposes par le format.
- Conserver en anglais les cles techniques comme `name` et `description`.
- Conserver en anglais le nom du fichier `SKILL.md`.
- Ne pas traduire les commandes, extraits de code, options, chemins, identifiants, noms de variables et mots-cles techniques.
- Ne pas traduire les noms officiels de produits, bibliotheques, API, protocoles, standards et outils.
- Conserver les acronymes, noms propres, URL et references techniques tels quels, sauf demande contraire explicite.

## Translation modes

### Default mode

Si l utilisateur ne precise aucun mode, utiliser le mode `naturel`.

### Mode fidele

- Rester proche du texte source.
- Preserver la structure et le niveau de detail.
- Eviter les reformulations inutiles.
- Ne pas resumer.
- Ne pas enrichir le contenu.

### Mode naturel

- Produire un francais fluide et idiomatique.
- Eviter les calques de l anglais.
- Preserver tout le contenu.
- Simplifier legerement la formulation seulement si cela ameliore la lecture.

### Mode soutenu

- Employer un registre plus formel.
- Conserver la precision du texte source.
- Eviter les formulations familieres.
- Maintenir une lecture fluide.

### Mode administratif

- Utiliser un style neutre, clair et factuel.
- Privilegier des phrases precises.
- Eviter les formulations promotionnelles.
- Conserver les obligations, conditions et nuances.

### Mode technique

- Conserver la precision technique.
- Maintenir les termes specialises appropries.
- Ne pas traduire les noms de produits, commandes, acronymes, identifiants, chemins, options, mots-cles techniques et fragments de code.
- Preserver la structure logique du contenu.

## Request interpretation

- `proche du texte`, `litterale`, `au plus pres` -> mode `fidele`
- `fluide`, `naturelle`, `idiomatique` -> mode `naturel`
- `plus formel`, `plus soutenu` -> mode `soutenu`
- `institutionnel`, `gouvernemental`, `administratif` -> mode `administratif`
- `technique`, `informatique`, `architecture` -> mode `technique`

## Validation

- La traduction est complete et ne supprime pas de contenu utile.
- Le mode demande ou infere est respecte.
- Les termes a conserver en anglais le sont effectivement.
- La structure du texte source est preservee.
- La reponse retourne directement la traduction sauf demande contraire.
