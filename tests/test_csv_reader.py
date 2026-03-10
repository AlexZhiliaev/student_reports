from pathlib import Path

from csv_reader import read_csv_files


def test_read_csv_files_parses_records(tmp_path: Path) -> None:
    csv_content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Alice,2024-06-01,100,7.5,5,ok,Math\n"
        "Bob,2024-06-02,200,6.0,6,tired,Math\n"
    )
    file_path = tmp_path / "data.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    records = read_csv_files([file_path])

    assert len(records) == 2
    assert records[0].student == "Alice"
    assert records[0].coffee_spent == 100.0
    assert records[1].student == "Bob"
    assert records[1].sleep_hours == 6.0


def test_read_csv_files_merges_multiple_files(tmp_path: Path) -> None:
    csv_content_a = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Alice,2024-06-01,100,7.5,5,ok,Math\n"
    )
    csv_content_b = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Bob,2024-06-02,200,6.0,6,tired,Math\n"
        "Cara,2024-06-03,300,6.5,7,ok,Math\n"
    )
    file_a = tmp_path / "a.csv"
    file_b = tmp_path / "b.csv"
    file_a.write_text(csv_content_a, encoding="utf-8")
    file_b.write_text(csv_content_b, encoding="utf-8")

    records = read_csv_files([file_a, file_b])

    assert len(records) == 3


def test_read_csv_files_empty_file(tmp_path: Path) -> None:
    csv_content = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
    file_path = tmp_path / "empty.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    records = read_csv_files([file_path])

    assert records == []
