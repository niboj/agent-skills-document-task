# Script decision matrix

Dans ce depot, la plupart des skills n ont pas besoin de scripts.

## Preferer le Markdown seul si

- la transformation repose sur des heuristiques redactionnelles;
- la validation peut se faire avec une checklist simple;
- il n y a pas de format machine a produire.

## Ajouter un script seulement si

- un format doit etre valide automatiquement;
- une conversion repetitive devient fragile sans automatisation;
- un controle structurel simple apporte une valeur nette.

## Exemples acceptables

- verifier un JSON d evaluations;
- verifier la presence de headings obligatoires;
- convertir un petit format de sortie repetitif.

## Exemples a eviter

- scripts qui reimplementent le jugement editorial;
- automatisations interactives;
- logique lourde qui transforme le depot en application.
