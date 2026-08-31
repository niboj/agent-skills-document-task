from pathlib import Path

import pytest

from document_task.errors import ValidationFailedError
from document_task.validator import validate_output


def test_validation_passes_for_non_empty_utf8(tmp_path: Path):
    target = tmp_path / "out.md"
    target.write_text("# Resultat\n", encoding="utf-8")

    assert validate_output(target)["validation"] == "passed"


def test_validation_rejects_forbidden_marker(tmp_path: Path):
    target = tmp_path / "out.md"
    target.write_text("TRUNCATED", encoding="utf-8")

    with pytest.raises(ValidationFailedError):
        validate_output(target)
