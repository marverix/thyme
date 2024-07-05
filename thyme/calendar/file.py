from pathlib import Path


def does_calendar_file_exist(calendar_file_path: Path) -> bool:
    return calendar_file_path.exists()
