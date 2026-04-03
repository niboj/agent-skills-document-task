# Note de compatibilite des plateformes

Ce gabarit sert a documenter les ecarts si un skill de transformation de texte doit etre adapte a une plateforme particuliere.

## Noyau portable

- frontmatter `name` et `description`
- `SKILL.md`
- `references/` en Markdown
- scripts non interactifs optionnels

## Notes specifiques par plateforme

- Codex: privilegier des descriptions tres explicites pour le declenchement.
- Claude Code: conserver un noyau procedural court.
- OpenCode: limiter les dependances externes et les chemins complexes.
