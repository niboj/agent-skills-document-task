from datetime import datetime, timezone
from pathlib import Path

from .document_manager import build_index, convert_to_markdown
from .file_manager import append_text, atomic_write, resolve_file
from .reader import read_section
from .storage import documents_registry, next_id, read_json, tasks_registry, workspace_root, write_json
from .validator import validate_output


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def prepare(source_value: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    root = workspace_root(cwd)
    source = resolve_file(source_value, cwd)
    markdown, conversion = convert_to_markdown(source)
    index = build_index(markdown)

    docs_path = documents_registry(root)
    docs = read_json(docs_path, default={}) or {}
    existing = list(docs.keys())
    document_id = next_id("DOC", existing)
    doc_dir = root / "documents" / document_id
    doc_dir.mkdir(parents=True, exist_ok=True)

    write_json(doc_dir / "source.json", {
        "document_id": document_id,
        "source": str(source),
        "working_copy": str(markdown),
        "conversion": conversion,
        "updated_at": now_iso(),
    })
    write_json(doc_dir / "index.json", index)
    docs[document_id] = str(doc_dir)
    write_json(docs_path, docs)

    return {
        "document_id": document_id,
        "source": source.name,
        "working_copy": markdown.name,
        "sections": len(index["sections"]),
        "status": "ready",
    }


def create_or_advance(document_id: str, instruction: str, output: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    root = workspace_root(cwd)
    doc_dir = _doc_dir(root, document_id)
    index = read_json(doc_dir / "index.json")
    source = read_json(doc_dir / "source.json")

    tasks_path = tasks_registry(root)
    tasks = read_json(tasks_path, default={}) or {}
    task_id = next_id("TASK", list(tasks.keys()))
    task_dir = root / task_id
    findings_dir = task_dir / "findings"
    out_dir = task_dir / "output"
    findings_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    state = {
        "task_id": task_id,
        "document_id": document_id,
        "instruction": instruction,
        "status": "in_progress",
        "progress": {
            "sections_total": len(index["sections"]),
            "sections_processed": 0,
            "next_section": index["sections"][0]["id"] if index["sections"] else None,
        },
        "output": {"path": str(out_dir / output)},
        "updated_at": now_iso(),
    }
    write_json(task_dir / "state.json", state)
    write_json(task_dir / "source.json", source)
    write_json(task_dir / "index.json", index)
    tasks[task_id] = str(task_dir)
    write_json(tasks_path, tasks)
    return advance(task_id, cwd)


def advance(task_id: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    root = workspace_root(cwd)
    task_dir = _task_dir(root, task_id)
    state = read_json(task_dir / "state.json")
    index = read_json(task_dir / "index.json")
    source = read_json(task_dir / "source.json")
    next_section = state["progress"].get("next_section")
    if not next_section:
        return status(task_id, cwd)

    section = next(item for item in index["sections"] if item["id"] == next_section)
    segment = read_section(Path(source["working_copy"]), section)
    finding_path = task_dir / "findings" / f"{section['id']}.md"
    if not finding_path.exists():
        atomic_write(finding_path, f"# {section['id']}\n\n## Constats\n\n")

    processed = state["progress"]["sections_processed"]
    all_sections = index["sections"]
    next_index = processed + 1
    state["progress"]["sections_processed"] = processed + 1
    state["progress"]["next_section"] = all_sections[next_index]["id"] if next_index < len(all_sections) else None
    state["updated_at"] = now_iso()
    if state["progress"]["next_section"] is None:
        state["status"] = "ready_to_finalize"
    write_json(task_dir / "state.json", state)

    compact = {
        "task_id": task_id,
        "status": state["status"],
        "processed": state["progress"]["sections_processed"],
        "total": state["progress"]["sections_total"],
        "section_id": section["id"],
        "next": state["progress"]["next_section"],
        "finding": str(finding_path),
        "segment_id": segment["segment_id"],
        "lines": segment["lines"],
    }
    return compact


def resume(task_id: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    task_path = _task_dir(workspace_root(cwd), task_id)
    state = read_json(task_path / "state.json")
    if state["status"] == "in_progress" and state["progress"].get("next_section"):
        advance(task_id, cwd)
        state = read_json(task_path / "state.json")
    return {
        "task": state["instruction"],
        "progress": f"{state['progress']['sections_processed']}/{state['progress']['sections_total']}",
        "next_section": state["progress"]["next_section"],
        "output": Path(state["output"]["path"]).name,
        "status": state["status"],
    }


def status(task_id: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    state = read_json(_task_dir(workspace_root(cwd), task_id) / "state.json")
    processed = state["progress"]["sections_processed"]
    total = state["progress"]["sections_total"]
    return {
        "task_id": task_id,
        "status": state["status"],
        "processed": processed,
        "total": total,
        "progress_percent": int((processed / total) * 100) if total else 100,
        "next": state["progress"]["next_section"],
        "output": Path(state["output"]["path"]).name,
    }


def finalize(task_id: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    task_dir = _task_dir(workspace_root(cwd), task_id)
    state = read_json(task_dir / "state.json")
    index = read_json(task_dir / "index.json")
    output = Path(state["output"]["path"])
    seen = set()
    parts = [f"# Resultats {task_id}\n\nInstruction: {state['instruction']}\n\n"]
    for section in index["sections"]:
        finding = task_dir / "findings" / f"{section['id']}.md"
        if not finding.exists():
            continue
        text = finding.read_text(encoding="utf-8").strip()
        if text and text not in seen:
            parts.append(text + "\n\n")
            seen.add(text)
    atomic_write(output, "".join(parts))
    validation = validate_output(output, len(index["sections"]), state["progress"]["sections_processed"])
    state["status"] = "completed"
    state["updated_at"] = now_iso()
    write_json(task_dir / "state.json", state)
    return {
        "task_id": task_id,
        "status": "completed",
        "output": str(output),
        "sections_processed": state["progress"]["sections_processed"],
        "validation": validation["validation"],
    }


def record_finding(task_id: str, section_id: str, text: str, cwd: Path | None = None) -> dict:
    cwd = cwd or Path.cwd()
    finding = _task_dir(workspace_root(cwd), task_id) / "findings" / f"{section_id}.md"
    append_text(finding, text if text.endswith("\n") else text + "\n")
    return {"status": "success", "finding": str(finding)}


def _doc_dir(root: Path, document_id: str) -> Path:
    docs = read_json(documents_registry(root), default={}) or {}
    if document_id not in docs:
        raise KeyError(document_id)
    return Path(docs[document_id])


def _task_dir(root: Path, task_id: str) -> Path:
    tasks = read_json(tasks_registry(root), default={}) or {}
    if task_id not in tasks:
        raise KeyError(task_id)
    return Path(tasks[task_id])
