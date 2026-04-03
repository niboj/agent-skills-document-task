#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter terminator not found")
    raw = text[4:end]
    data = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    body = text[end + 5:]
    return data, body


def check_skill_dir(skill_dir: Path):
    issues = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"Missing SKILL.md in {skill_dir}"]

    data, body = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    name = data.get("name", "")
    description = data.get("description", "")

    if not name:
        issues.append("Missing frontmatter field: name")
    else:
        if len(name) > MAX_NAME_LENGTH:
            issues.append(f"Skill name exceeds {MAX_NAME_LENGTH} characters: {name}")
        if not NAME_RE.match(name):
            issues.append(f"Invalid name format: {name}")

    if name and skill_dir.name != name:
        issues.append(f"Folder name does not match skill name: {skill_dir.name} != {name}")

    if not description:
        issues.append("Missing frontmatter field: description")
    elif "use this skill when" not in description.lower():
        issues.append("Description should explicitly say when to use the skill")
    elif len(description) > 1024:
        issues.append("Description exceeds 1024 characters")

    if "--" in name:
        issues.append("Skill name must not contain consecutive hyphens")

    if len(body.splitlines()) > 500:
        issues.append("SKILL.md body exceeds 500 lines")

    for required_heading in ["## Goal", "## When to use", "## Procedure"]:
        if required_heading not in body:
            issues.append(f"Missing recommended heading: {required_heading}")

    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        if not refs_dir.is_dir():
            issues.append("references exists but is not a directory")
        for path in refs_dir.rglob("*"):
            if path.is_file() and len(path.relative_to(refs_dir).parts) > 2:
                issues.append(f"references tree is too deep: {path}")

    evals_file = skill_dir / "evals" / "evals.json"
    if evals_file.exists():
        try:
            evals = json.loads(evals_file.read_text(encoding="utf-8"))
            cases = evals.get("cases", [])
            if not isinstance(cases, list) or len(cases) < 3:
                issues.append("evals/evals.json should contain at least 3 cases")
        except json.JSONDecodeError:
            issues.append("evals/evals.json is not valid JSON")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Run lightweight checks on one or more skill folders.")
    parser.add_argument("paths", nargs="+", help="Skill directories to validate")
    args = parser.parse_args()

    report = {}
    failed = False
    for path in args.paths:
        issues = check_skill_dir(Path(path))
        report[path] = issues
        if issues:
            failed = True

    print(json.dumps(report, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
