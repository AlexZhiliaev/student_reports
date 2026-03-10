from pathlib import Path

import pytest

from main import run


def test_run_outputs_table(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    csv_content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Alice,2024-06-01,100,7.5,5,ok,Math\n"
        "Bob,2024-06-02,200,6.0,6,tired,Math\n"
        "Bob,2024-06-03,300,6.0,6,tired,Math\n"
    )
    file_path = tmp_path / "data.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    run(["--files", str(file_path), "--report", "median-coffee"])
    output = capsys.readouterr().out

    assert "median_coffee" in output
    assert "Alice" in output
    assert "Bob" in output


def test_run_missing_file_raises() -> None:
    with pytest.raises(FileNotFoundError) as exc_info:
        run(["--files", "missing.csv", "--report", "median-coffee"])
    assert "File not found" in str(exc_info.value)


def test_run_invalid_report_raises(tmp_path: Path) -> None:
    csv_content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Alice,2024-06-01,100,7.5,5,ok,Math\n"
    )
    file_path = tmp_path / "data.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        run(["--files", str(file_path), "--report", "unknown-report"])
    assert "Unknown report" in str(exc_info.value)
