import os
import unicodedata
from pathlib import Path

from .errors import FileAmbiguousError, FileNotFoundErrorDT, WriteFailedError


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFC", value)


def normalize_path_text(value: str) -> str:
    return normalize_text(value.strip().strip("\"'"))


def _same_normalized_name(path: Path, requested: str) -> bool:
    return normalize_text(path.name) == normalize_text(requested)


def resolve_file(value: str, cwd: Path | None = None) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    raw = normalize_path_text(value)
    candidate = Path(raw).expanduser()

    if candidate.is_absolute() and candidate.exists():
        return candidate.resolve()

    direct = (cwd / candidate).resolve()
    if direct.exists():
        return direct

    matches = []
    requested = Path(raw).name
    for path in cwd.rglob("*"):
        if path.is_file() and _same_normalized_name(path, requested):
            matches.append(path.resolve())

    unique = sorted({str(path): path for path in matches}.values(), key=str)
    if len(unique) == 1:
        return unique[0]
    if len(unique) > 1:
        raise FileAmbiguousError("; ".join(str(path) for path in unique[:5]))
    raise FileNotFoundErrorDT(raw)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    try:
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, path)
    except OSError as exc:
        raise WriteFailedError(str(exc)) from exc


def append_text(path: Path, text: str, max_chunk_chars: int = 16000) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if len(text) > max_chunk_chars:
        raise WriteFailedError("append chunk too large")
    try:
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    except OSError as exc:
        raise WriteFailedError(str(exc)) from exc
