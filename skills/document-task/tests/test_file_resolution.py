import unicodedata
from pathlib import Path

import pytest

from document_task.errors import FileAmbiguousError
from document_task.file_manager import resolve_file


def test_resolves_file_with_spaces_and_accents(tmp_path: Path):
    source = tmp_path / "Reponse Red Hat DP-11584 Signé.md"
    source.write_text("# Intro\n", encoding="utf-8")

    resolved = resolve_file("Reponse Red Hat DP-11584 Signé.md", tmp_path)

    assert resolved == source.resolve()


def test_resolves_nfd_name_against_nfc_file(tmp_path: Path):
    nfc = "Café à l'essai.md"
    source = tmp_path / nfc
    source.write_text("# Test\n", encoding="utf-8")
    nfd = unicodedata.normalize("NFD", nfc)

    resolved = resolve_file(nfd, tmp_path)

    assert resolved == source.resolve()


def test_ambiguous_filename_is_reported(tmp_path: Path):
    (tmp_path / "a").mkdir()
    (tmp_path / "b").mkdir()
    (tmp_path / "a" / "doc.md").write_text("a", encoding="utf-8")
    (tmp_path / "b" / "doc.md").write_text("b", encoding="utf-8")

    with pytest.raises(FileAmbiguousError):
        resolve_file("doc.md", tmp_path)


def test_wsl_absolute_path_is_supported(tmp_path: Path):
    source = tmp_path / "doc.md"
    source.write_text("# Test\n", encoding="utf-8")

    assert resolve_file(str(source), tmp_path) == source.resolve()
