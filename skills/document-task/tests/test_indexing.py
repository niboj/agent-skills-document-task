from pathlib import Path

from document_task.document_manager import build_index


def test_index_detects_markdown_headings(tmp_path: Path):
    source = tmp_path / "doc.md"
    source.write_text("# Intro\nA\n\n## Besoins\nB\n", encoding="utf-8")

    index = build_index(source)

    assert [section["id"] for section in index["sections"]] == ["SEC-001", "SEC-002"]
    assert index["sections"][1]["title"] == "Besoins"


def test_long_markdown_is_split_into_segments(tmp_path: Path):
    source = tmp_path / "long.md"
    source.write_text("# Long\n" + "\n".join("ligne " * 40 for _ in range(80)), encoding="utf-8")

    index = build_index(source, max_section_chars=1000)

    assert len(index["sections"]) > 1
    assert index["sections"][0]["split"] is True
