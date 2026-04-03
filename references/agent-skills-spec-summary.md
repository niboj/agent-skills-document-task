# Agent Skills specification summary

This repository follows the public Agent Skills format and authoring guidance.

## Baseline rules

- A skill is a folder that contains at least `SKILL.md`.
- `SKILL.md` must contain YAML frontmatter followed by Markdown instructions.
- Required frontmatter fields: `name`, `description`.
- `name` should use lowercase letters, digits, and hyphens only.
- Keep `SKILL.md` lean; move detail into `references/`, `assets/`, or `scripts/` when needed.
- Write `description` for triggering, not for documentation alone.
- Use scripts only when determinism or repeatability matters.
- Prefer realistic evaluations over contrived prompts.

## Repository policy

- Author-facing repository documentation may be in French.
- Portable skills should be written in English unless there is a strong reason not to.
- Optional frontmatter beyond `name` and `description` should stay minimal.
- If `allowed-tools` is used, treat it as experimental and document that explicitly.
