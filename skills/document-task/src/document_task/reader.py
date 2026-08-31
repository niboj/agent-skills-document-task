from pathlib import Path

from .errors import ReadFailedError


def read_section(markdown: Path, section: dict, max_chars: int = 12000) -> dict:
    try:
        lines = markdown.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ReadFailedError(str(exc)) from exc

    start = section["start_line"]
    end = section["end_line"]
    content = "\n".join(lines[start - 1:end])
    truncated = len(content) > max_chars
    if truncated:
        content = content[:max_chars]
    return {
        "segment_id": section["id"].replace("SEC", "SEG"),
        "section_id": section["id"],
        "lines": f"{start}-{end}",
        "truncated": truncated,
        "content": content,
    }
