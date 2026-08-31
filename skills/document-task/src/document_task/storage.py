import json
from pathlib import Path

from .errors import StateCorruptedError
from .file_manager import atomic_write


def workspace_root(cwd: Path | None = None) -> Path:
    return (cwd or Path.cwd()) / ".opencode" / "document-tasks"


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise StateCorruptedError(str(path)) from exc


def write_json(path: Path, data) -> None:
    atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def next_id(prefix: str, existing: list[str]) -> str:
    max_seen = 0
    for value in existing:
        if value.startswith(prefix + "-"):
            try:
                max_seen = max(max_seen, int(value.split("-", 1)[1]))
            except ValueError:
                pass
    return f"{prefix}-{max_seen + 1:03d}"


def documents_registry(root: Path) -> Path:
    return root / "documents.json"


def tasks_registry(root: Path) -> Path:
    return root / "tasks.json"
