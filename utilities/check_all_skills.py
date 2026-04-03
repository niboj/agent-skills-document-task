#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run check_skill.py against every skill folder that contains SKILL.md."
    )
    parser.add_argument(
        "--skills-root",
        default="skills",
        help="Root directory containing skill folders",
    )
    args = parser.parse_args()

    skills_root = Path(args.skills_root)
    if not skills_root.exists():
        raise SystemExit(f"Skills root does not exist: {skills_root}")

    skill_dirs = sorted(
        path.parent
        for path in skills_root.glob("*/SKILL.md")
        if path.parent.is_dir()
    )
    if not skill_dirs:
        raise SystemExit(f"No skills found under: {skills_root}")

    cmd = [sys.executable, "utilities/check_skill.py", *[str(path) for path in skill_dirs]]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
