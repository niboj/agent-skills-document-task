# document-task

Skill documentaire pour preparer, segmenter, traiter, reprendre et finaliser une analyse de document avec un contexte modele limite.

## Utilisation

```bash
skills/document-task/bin/document-task prepare "document.pdf"
skills/document-task/bin/document-task process DOC-001 "Identifier les besoins" --output besoins.md
skills/document-task/bin/document-task resume TASK-001
skills/document-task/bin/document-task status TASK-001
skills/document-task/bin/document-task finalize TASK-001
```

Les donnees persistantes sont stockees dans `.opencode/document-tasks/` par defaut. Les documents prepares sont references dans `.opencode/document-tasks/documents.json`.

## Principes

- Un seul skill expose aux agents.
- Des actions compactes: `prepare`, `process`, `resume`, `status`, `finalize`.
- Pas de lecture complete retournee au modele.
- Etat sur disque, lisible et recuperable.
- Ecriture atomique pour les etats et les sorties finales.

## Formats supportes

- Markdown et texte brut.
- PDF textuel avec PyMuPDF lorsque la dependance `fitz` est disponible.
