#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return re.sub(r"-{2,}", "-", slug)


def build_skill_md(name: str, description: str) -> str:
    return f"""---
name: {name}
description: {description}
---

# Skill: {name}

## Goal

Produce a reliable text transformation for one focused, repeatable use case.

## When to use

- Replace these bullets with the exact moment the skill should trigger.
- Keep the scope limited to one main text transformation.

## Inputs

- Source text
- Constraints that matter
- Relevant local references, if any

## Procedure

1. Identify the source text, target output, and required constraints.
2. Read only the references needed for the current case.
3. Execute the default transformation path first.
4. Validate the output before finalizing.

## Validation

- Replace this checklist with concrete checks on the transformed text.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a new Agent Skill folder.")
    parser.add_argument("--root", default="skills", help="Skills root directory")
    parser.add_argument("--name", required=True, help="Skill folder and frontmatter name")
    parser.add_argument("--description", required=True, help="Trigger-oriented skill description")
    parser.add_argument("--with-references", action="store_true", help="Create references/context.md")
    parser.add_argument("--with-scripts", action="store_true", help="Create scripts/ directory")
    parser.add_argument("--with-assets", action="store_true", help="Create assets/ directory")
    parser.add_argument("--with-evals", action="store_true", help="Create evals/evals.json")
    args = parser.parse_args()

    name = slugify(args.name)
    if len(name) > MAX_NAME_LENGTH:
        raise SystemExit(f"Skill name exceeds {MAX_NAME_LENGTH} characters after normalization: {name}")
    if not NAME_RE.match(name):
        raise SystemExit(f"Invalid skill name after normalization: {name}")

    root = Path(args.root)
    skill_dir = root / name
    if skill_dir.exists():
        raise SystemExit(f"Skill directory already exists: {skill_dir}")

    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(build_skill_md(name, args.description), encoding="utf-8")

    created = [str(skill_dir / "SKILL.md")]

    if args.with_references:
        ref_dir = skill_dir / "references"
        ref_dir.mkdir()
        ref_file = ref_dir / "context.md"
        ref_file.write_text("# Local reference\n\nAdd only material that changes execution.\n", encoding="utf-8")
        created.append(str(ref_file))

    if args.with_scripts:
        scripts_dir = skill_dir / "scripts"
        scripts_dir.mkdir()
        created.append(str(scripts_dir))

    if args.with_assets:
        assets_dir = skill_dir / "assets"
        assets_dir.mkdir()
        created.append(str(assets_dir))

    if args.with_evals:
        evals_dir = skill_dir / "evals"
        evals_dir.mkdir()
        evals_file = evals_dir / "evals.json"
        evals_file.write_text(json.dumps({
            "version": "1",
            "skill": name,
            "cases": []
        }, indent=2) + "\n", encoding="utf-8")
        created.append(str(evals_file))

    print(json.dumps({"created": created}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
