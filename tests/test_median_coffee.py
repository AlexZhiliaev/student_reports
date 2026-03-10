from models import StudentRecord
from reports.median_coffee import generate_median_coffee_report


def test_median_coffee_report_sorts_and_computes() -> None:
    records = [
        StudentRecord(
            student="Alice",
            date="2024-06-01",
            coffee_spent=10.0,
            sleep_hours=7.0,
            study_hours=5.0,
            mood="ok",
            exam="Math",
        ),
        StudentRecord(
            student="Alice",
            date="2024-06-02",
            coffee_spent=20.0,
            sleep_hours=6.0,
            study_hours=6.0,
            mood="ok",
            exam="Math",
        ),
        StudentRecord(
            student="Bob",
            date="2024-06-01",
            coffee_spent=30.0,
            sleep_hours=5.0,
            study_hours=7.0,
            mood="tired",
            exam="Math",
        ),
        StudentRecord(
            student="Bob",
            date="2024-06-02",
            coffee_spent=40.0,
            sleep_hours=5.5,
            study_hours=8.0,
            mood="tired",
            exam="Math",
        ),
        StudentRecord(
            student="Bob",
            date="2024-06-03",
            coffee_spent=50.0,
            sleep_hours=5.0,
            study_hours=9.0,
            mood="tired",
            exam="Math",
        ),
    ]

    table = generate_median_coffee_report(records)

    assert table.headers == ["student", "median_coffee"]
    assert table.rows == [["Bob", 40.0], ["Alice", 15.0]]


def test_median_coffee_report_sorts_by_name_on_tie() -> None:
    records = [
        StudentRecord(
            student="Bob",
            date="2024-06-01",
            coffee_spent=10.0,
            sleep_hours=7.0,
            study_hours=5.0,
            mood="ok",
            exam="Math",
        ),
        StudentRecord(
            student="Bob",
            date="2024-06-02",
            coffee_spent=30.0,
            sleep_hours=6.0,
            study_hours=6.0,
            mood="ok",
            exam="Math",
        ),
        StudentRecord(
            student="Alice",
            date="2024-06-01",
            coffee_spent=20.0,
            sleep_hours=7.0,
            study_hours=5.0,
            mood="ok",
            exam="Math",
        ),
        StudentRecord(
            student="Alice",
            date="2024-06-02",
            coffee_spent=20.0,
            sleep_hours=6.0,
            study_hours=6.0,
            mood="ok",
            exam="Math",
        ),
    ]

    table = generate_median_coffee_report(records)

    assert table.rows == [["Alice", 20.0], ["Bob", 20.0]]
