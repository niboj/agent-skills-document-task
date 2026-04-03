# Platform compatibility matrix

This repository targets a portable core for Agent Skills, with platform-specific behavior documented explicitly.

## Shared portable core

- One folder per skill
- `SKILL.md` entrypoint
- YAML frontmatter
- `name` and `description`
- Markdown body
- Optional `references/`, `scripts/`, `assets/`, `evals/`

## Discovery paths

### Codex / generic agent-compatible layout

- `.agents/skills/<name>/SKILL.md`
- `~/.agents/skills/<name>/SKILL.md`

### Claude Code

- `.claude/skills/<name>/SKILL.md`
- `~/.claude/skills/<name>/SKILL.md`

### OpenCode

- `.opencode/skills/<name>/SKILL.md`
- `~/.config/opencode/skills/<name>/SKILL.md`
- also reads `.claude/skills/` and `.agents/skills/` layouts

## Frontmatter portability

### Portable across all targeted environments

- `name`
- `description`

### OpenCode-documented optional fields

- `license`
- `compatibility`
- `metadata`

### Claude-specific optional fields

- `disable-model-invocation`
- `allowed-tools`
- `model`
- `effort`
- `context`
- `agent`

## Notable behavior differences

### Claude Code

- `description` is recommended and is used for automatic loading.
- Descriptions longer than about 250 characters are truncated in the skill listing, so front-load the key use case.
- `name` is optional in Claude, but keep it for cross-tool portability.

### OpenCode

- Only `name`, `description`, `license`, `compatibility`, and `metadata` are recognized in frontmatter.
- Unknown frontmatter fields are ignored.
- `description` must stay within 1 to 1024 characters.

### Portable repository default

- Use only `name` and `description` in shipped templates.
- Add platform-specific metadata only in consciously tool-specific variants.

## Guidance

- Keep the default repository templates on the portable core only.
- Put platform-specific guidance in references, not in every skill frontmatter.
- If using Claude-specific fields, isolate the decision in a compatibility note.
- Treat any non-portable frontmatter as opt-in, not default.
