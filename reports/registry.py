from collections.abc import Callable

from models import ReportTable, StudentRecord
from reports import generate_median_coffee_report


type ReportGenerator = Callable[[list[StudentRecord]], ReportTable]


REPORTS: dict[str, ReportGenerator] = {
    "median-coffee": generate_median_coffee_report,
}


def report_names() -> list[str]:
    """Возвращает список доступных отчетов."""
    return sorted(REPORTS.keys())


def get_report(name: str) -> ReportGenerator:
    """Возвращает генератор отчета по имени."""
    try:
        return REPORTS[name]
    except KeyError as exc:
        available = ", ".join(report_names())
        raise ValueError(f"Unknown report '{name}'. Available: {available}") from exc
