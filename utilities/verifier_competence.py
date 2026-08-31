#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md doit commencer par un frontmatter YAML")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Fin du frontmatter de SKILL.md introuvable")
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
        return [f"SKILL.md manquant dans {skill_dir}"]

    data, body = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    name = data.get("name", "")
    description = data.get("description", "")

    if not name:
        issues.append("Champ frontmatter manquant: name")
    else:
        if len(name) > MAX_NAME_LENGTH:
            issues.append(f"Le nom de la competence depasse {MAX_NAME_LENGTH} caracteres: {name}")
        if not NAME_RE.match(name):
            issues.append(f"Format de nom invalide: {name}")

    if name and skill_dir.name != name:
        issues.append(f"Le nom du dossier ne correspond pas au nom de la competence: {skill_dir.name} != {name}")

    if not description:
        issues.append("Champ frontmatter manquant: description")
    elif "utiliser cette competence" not in description.lower():
        issues.append("La description doit indiquer explicitement quand utiliser la competence")
    elif len(description) > 1024:
        issues.append("La description depasse 1024 caracteres")

    if "--" in name:
        issues.append("Le nom de la competence ne doit pas contenir de traits d union consecutifs")

    if len(body.splitlines()) > 500:
        issues.append("Le corps de SKILL.md depasse 500 lignes")

    for required_heading in ["## Objectif", "## Quand utiliser cette competence", "## Procedure"]:
        if required_heading not in body:
            issues.append(f"Section recommandee manquante: {required_heading}")

    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        if not refs_dir.is_dir():
            issues.append("references existe mais n est pas un dossier")
        for path in refs_dir.rglob("*"):
            if path.is_file() and len(path.relative_to(refs_dir).parts) > 2:
                issues.append(f"L arborescence references est trop profonde: {path}")

    evals_file = skill_dir / "evals" / "evaluations.json"
    if evals_file.exists():
        try:
            evals = json.loads(evals_file.read_text(encoding="utf-8"))
            cases = evals.get("cases", [])
            if not isinstance(cases, list) or len(cases) < 3:
                issues.append("evals/evaluations.json devrait contenir au moins 3 cas")
        except json.JSONDecodeError:
            issues.append("evals/evaluations.json n est pas un JSON valide")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute des verifications legeres sur un ou plusieurs dossiers de competences.")
    parser.add_argument("paths", nargs="+", help="Dossiers de competences a valider")
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
