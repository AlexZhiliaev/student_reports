import csv
from pathlib import Path

from models import StudentRecord


def read_csv_files(file_paths: list[Path]) -> list[StudentRecord]:
    """Читает и парсит несколько CSV-файлов в общий список записей."""
    records: list[StudentRecord] = []
    for file_path in file_paths:
        records.extend(_read_csv_file(file_path))
    return records


def _read_csv_file(file_path: Path) -> list[StudentRecord]:
    """Читает один CSV-файл и парсит строки."""
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return [
            StudentRecord(
                student=row["student"],
                date=row["date"],
                coffee_spent=float(row["coffee_spent"]),
                sleep_hours=float(row["sleep_hours"]),
                study_hours=float(row["study_hours"]),
                mood=row["mood"],
                exam=row["exam"],
            )
            for row in reader
        ]
