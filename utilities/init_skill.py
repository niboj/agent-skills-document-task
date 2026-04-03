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

## Objectif

Produire une transformation de texte fiable pour un cas d usage cible et repetable.

## Quand utiliser cette competence

- Remplacer ces puces par le moment exact ou la competence doit se declencher.
- Garder un perimetre limite a une transformation textuelle principale.

## Entrees

- Texte source
- Contraintes pertinentes
- References locales utiles, si necessaire

## Procedure

1. Identifier le texte source, la sortie cible et les contraintes requises.
2. Lire uniquement les references necessaires pour le cas traite.
3. Executer d abord le chemin de transformation par defaut.
4. Valider la sortie avant finalisation.

## Validation

- Remplacer cette checklist par des verifications concretes sur le texte transforme.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialiser un nouveau dossier de competence Agent Skills.")
    parser.add_argument("--root", default="skills", help="Dossier racine des competences")
    parser.add_argument("--name", required=True, help="Nom du dossier et du frontmatter")
    parser.add_argument("--description", required=True, help="Description orientee declenchement")
    parser.add_argument("--with-references", action="store_true", help="Creer references/context.md")
    parser.add_argument("--with-scripts", action="store_true", help="Creer le dossier scripts/")
    parser.add_argument("--with-assets", action="store_true", help="Creer le dossier assets/")
    parser.add_argument("--with-evals", action="store_true", help="Creer evals/evals.json")
    args = parser.parse_args()

    name = slugify(args.name)
    if len(name) > MAX_NAME_LENGTH:
        raise SystemExit(f"Le nom de la competence depasse {MAX_NAME_LENGTH} caracteres apres normalisation: {name}")
    if not NAME_RE.match(name):
        raise SystemExit(f"Nom de competence invalide apres normalisation: {name}")

    root = Path(args.root)
    skill_dir = root / name
    if skill_dir.exists():
        raise SystemExit(f"Le dossier de competence existe deja: {skill_dir}")

    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(build_skill_md(name, args.description), encoding="utf-8")

    created = [str(skill_dir / "SKILL.md")]

    if args.with_references:
        ref_dir = skill_dir / "references"
        ref_dir.mkdir()
        ref_file = ref_dir / "context.md"
        ref_file.write_text("# Reference locale\n\nAjouter seulement le contenu qui change reellement l execution.\n", encoding="utf-8")
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
