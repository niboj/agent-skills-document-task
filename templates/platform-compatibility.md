# Platform compatibility note

Ce gabarit sert a documenter les ecarts si un skill de transformation de texte doit etre adapte a une plateforme particuliere.

## Portable core

- frontmatter `name` et `description`
- `SKILL.md`
- `references/` en Markdown
- scripts non interactifs optionnels

## Platform-specific notes

- Codex: privilegier des descriptions tres explicites pour le declenchement.
- Claude Code: conserver un noyau procedural court.
- OpenCode: limiter les dependances externes et les chemins complexes.
