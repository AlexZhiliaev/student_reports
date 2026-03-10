from tabulate import tabulate

from models import ReportTable


def format_table(table: ReportTable) -> str:
    """Форматирует отчетную таблицу для вывода в консоль."""
    return tabulate(
        tabular_data=table.rows,
        headers=table.headers,
        tablefmt="github",
    )


def print_table(table: ReportTable) -> None:
    """Печатает отчетную таблицу в stdout."""
    print(format_table(table))
