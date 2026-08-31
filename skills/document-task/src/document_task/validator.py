from pathlib import Path

from .errors import ValidationFailedError

FORBIDDEN_MARKERS = ["TODO_GENERATION", "TRUNCATED"]


def validate_output(path: Path, expected_sections: int | None = None, processed_sections: int | None = None) -> dict:
    if not path.exists():
        raise ValidationFailedError("missing output")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValidationFailedError("empty output")
    for marker in FORBIDDEN_MARKERS:
        if marker in text:
            raise ValidationFailedError(f"marker found: {marker}")
    if expected_sections is not None and processed_sections is not None and processed_sections < expected_sections:
        raise ValidationFailedError("sections incomplete")
    for temp in path.parent.glob("*.tmp"):
        raise ValidationFailedError(f"temp file remains: {temp.name}")
    return {"validation": "passed", "size": path.stat().st_size}
