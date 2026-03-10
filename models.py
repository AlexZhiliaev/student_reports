from dataclasses import dataclass

type Cell = str | int | float


type Row = list[Cell]


@dataclass(slots=True, frozen=True)
class StudentRecord:
    """Типизированное представление строки CSV."""

    student: str
    date: str
    coffee_spent: float
    sleep_hours: float
    study_hours: float
    mood: str
    exam: str


@dataclass(slots=True)
class ReportTable:
    """Табличный отчет для отображения."""

    headers: list[str]
    rows: list[Row]
