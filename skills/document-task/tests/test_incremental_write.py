from pathlib import Path

import pytest

from document_task.errors import WriteFailedError
from document_task.file_manager import append_text


def test_append_writes_small_chunks(tmp_path: Path):
    target = tmp_path / "out.md"

    append_text(target, "one\n", max_chunk_chars=10)
    append_text(target, "two\n", max_chunk_chars=10)

    assert target.read_text(encoding="utf-8") == "one\ntwo\n"


def test_append_rejects_large_chunk(tmp_path: Path):
    with pytest.raises(WriteFailedError):
        append_text(tmp_path / "out.md", "x" * 20, max_chunk_chars=10)
