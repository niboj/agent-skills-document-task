import re
from pathlib import Path

from .errors import IndexFailedError, PdfExtractionFailedError, UnsupportedFormatError
from .file_manager import atomic_write

PAGE_RE = re.compile(r"^<!-- page: (\d+) -->$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUMBERED_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)[.)]\s+(.+?)\s*$")


def convert_to_markdown(source: Path) -> tuple[Path, dict]:
    suffix = source.suffix.lower()
    if suffix in {".md", ".markdown"}:
        return source, {"format": "markdown", "converted": False}
    if suffix in {".txt", ".text"}:
        target = source.with_suffix(".md")
        atomic_write(target, source.read_text(encoding="utf-8"))
        return target, {"format": "text", "converted": True}
    if suffix == ".pdf":
        return _convert_pdf(source)
    raise UnsupportedFormatError(suffix or "unknown")


def _convert_pdf(source: Path) -> tuple[Path, dict]:
    try:
        import fitz
    except ImportError as exc:
        raise PdfExtractionFailedError("PyMuPDF unavailable") from exc

    pages = []
    empty_pages = []
    try:
        with fitz.open(source) as doc:
            for index, page in enumerate(doc, start=1):
                text = page.get_text("text").strip()
                if len(text) < 10:
                    empty_pages.append(index)
                pages.append(f"<!-- page: {index} -->\n\n{text}\n")
    except Exception as exc:
        raise PdfExtractionFailedError(str(exc)) from exc

    target = source.with_suffix(".md")
    atomic_write(target, "\n".join(pages))
    return target, {"format": "pdf", "converted": True, "pages": len(pages), "empty_pages": empty_pages}


def build_index(markdown: Path, max_section_chars: int = 12000) -> dict:
    try:
        lines = markdown.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise IndexFailedError(str(exc)) from exc

    starts = []
    for idx, line in enumerate(lines, start=1):
        heading = HEADING_RE.match(line)
        numbered = NUMBERED_RE.match(line)
        page = PAGE_RE.match(line)
        if heading:
            starts.append((idx, heading.group(2)))
        elif numbered:
            starts.append((idx, numbered.group(0).strip()))
        elif page:
            starts.append((idx, f"Page {page.group(1)}"))

    if not starts:
        starts = [(1, markdown.stem)]

    sections = []
    for pos, (start, title) in enumerate(starts):
        end = starts[pos + 1][0] - 1 if pos + 1 < len(starts) else len(lines)
        sections.extend(_split_section(lines, start, end, title, len(sections), max_section_chars))

    return {
        "document": str(markdown),
        "line_count": len(lines),
        "sections": sections,
    }


def _split_section(lines: list[str], start: int, end: int, title: str, offset: int, max_chars: int) -> list[dict]:
    result = []
    chunk_start = start
    chars = 0
    for line_no in range(start, end + 1):
        line_len = len(lines[line_no - 1]) + 1
        chars += line_len
        if chars >= max_chars and (line_no < end or line_len >= max_chars):
            result.append(_section(offset + len(result) + 1, title, chunk_start, line_no, split=True))
            chunk_start = line_no + 1
            chars = 0
            if chunk_start > end:
                break
    if chunk_start <= end:
        result.append(_section(offset + len(result) + 1, title, chunk_start, end, split=len(result) > 0))
    return result


def _section(number: int, title: str, start: int, end: int, split: bool = False) -> dict:
    return {
        "id": f"SEC-{number:03d}",
        "title": title[:120],
        "start_line": start,
        "end_line": end,
        "split": split,
    }
