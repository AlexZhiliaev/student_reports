import argparse
from pathlib import Path

from csv_reader import read_csv_files
from render import print_table
from reports import registry


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Парсит аргументы CLI."""
    parser = argparse.ArgumentParser(description="Student reports")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name",
    )
    return parser.parse_args(argv)


def ensure_files_exist(file_paths: list[Path]) -> None:
    """Быстро падает, если входной файл отсутствует."""
    for file_path in file_paths:
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")


def run(argv: list[str] | None = None) -> None:
    """Запускает пайплайн формирования отчета."""
    args = parse_args(argv)
    file_paths = [Path(path) for path in args.files]
    ensure_files_exist(file_paths)

    report = registry.get_report(args.report)
    records = read_csv_files(file_paths)
    table = report(records)
    print_table(table)


if __name__ == "__main__":
    try:
        run()
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc))
