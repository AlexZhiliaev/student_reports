from collections import defaultdict
from statistics import median

from models import ReportTable, StudentRecord


def generate_median_coffee_report(records: list[StudentRecord]) -> ReportTable:
    """Формирует таблицу отчета median-coffee."""
    spent_by_student: dict[str, list[float]] = defaultdict(list)
    for record in records:
        spent_by_student[record.student].append(record.coffee_spent)

    rows = [
        [student, median(spent_list)]
        for student, spent_list in spent_by_student.items()
    ]
    rows.sort(key=lambda row: (-float(row[1]), str(row[0])))

    return ReportTable(headers=["student", "median_coffee"], rows=rows)
