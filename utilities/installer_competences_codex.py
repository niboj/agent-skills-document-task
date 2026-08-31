#!/usr/bin/env python3
import argparse
import json
import os
import shutil
from pathlib import Path


DEFAULT_EXCLUDES = {"_templates", "example-skill"}


def discover_skills(skills_root: Path):
    for path in sorted(skills_root.iterdir()):
        if not path.is_dir():
            continue
        if path.name in DEFAULT_EXCLUDES:
            continue
        if (path / "SKILL.md").exists():
            yield path


def copy_skill(src: Path, dst: Path, force: bool):
    if dst.exists():
        if not force:
            return {"skill": src.name, "status": "skipped", "reason": "destination exists", "target": str(dst)}
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return {"skill": src.name, "status": "installed", "target": str(dst)}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install repository skills into a Codex-compatible global skills directory."
    )
    parser.add_argument("--skills-root", default="skills", help="Source skills directory")
    parser.add_argument(
        "--target-dir",
        default=None,
        help="Destination directory. Defaults to $CODEX_HOME/skills or ~/.codex/skills",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing installed skills")
    parser.add_argument("--include-example", action="store_true", help="Also install example-skill")
    args = parser.parse_args()

    codex_home = os.environ.get("CODEX_HOME")
    target_dir = Path(args.target_dir).expanduser() if args.target_dir else Path(codex_home).expanduser() / "skills" if codex_home else Path.home() / ".codex" / "skills"
    skills_root = Path(args.skills_root)

    if not skills_root.exists():
        raise SystemExit(f"Le dossier racine des competences n existe pas: {skills_root}")

    target_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for src in discover_skills(skills_root):
        if src.name == "example-skill" and not args.include_example:
            continue
        results.append(copy_skill(src, target_dir / src.name, args.force))

    print(json.dumps({
        "platform": "codex",
        "source": str(skills_root),
        "target": str(target_dir),
        "results": results
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
