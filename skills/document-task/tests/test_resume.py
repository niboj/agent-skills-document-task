from pathlib import Path

from document_task import task


def test_prepare_process_resume_and_finalize(tmp_path: Path):
    source = tmp_path / "source.md"
    source.write_text("# A\ncontenu A\n# B\ncontenu B\n", encoding="utf-8")

    prepared = task.prepare("source.md", tmp_path)
    first = task.create_or_advance(prepared["document_id"], "Extraire les besoins", "besoins.md", tmp_path)
    task_id = first["task_id"]

    resumed = task.resume(task_id, tmp_path)
    status = task.status(task_id, tmp_path)

    assert resumed["progress"] == "2/2"
    assert resumed["next_section"] is None
    assert status["processed"] == 2

    final = task.finalize(task_id, tmp_path)
    assert final["status"] == "completed"
    assert final["validation"] == "passed"
    assert Path(final["output"]).exists()
