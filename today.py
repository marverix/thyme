from os import environ
import calendar
from datetime import datetime

if environ.get("TODAY"):
    TODAY = datetime.fromisoformat(environ.get("TODAY"))
else:
    TODAY = datetime.today()

MONTH_RANGE = calendar.monthrange(TODAY.year, TODAY.month)

FORMAT_ISO_MONTH = "%Y-%m"
FORMAT_ISO_DATE = f"{FORMAT_ISO_MONTH}-%d"

FORMAT_POLISH_MONTH = "%m.%Y"
FORMAT_POLISH_DATE = f"%d.{FORMAT_POLISH_MONTH}"


def today_date_polish() -> str:
    return TODAY.strftime(FORMAT_POLISH_DATE)


def today_date_iso() -> str:
    return TODAY.strftime(FORMAT_ISO_DATE)


def this_month_first_day() -> int:
    return 1


def this_month_last_day() -> int:
    return MONTH_RANGE[1]


def this_month_first_date_polish() -> str:
    return TODAY.strftime(f"{this_month_first_day()}.{FORMAT_POLISH_MONTH}")


def this_month_last_date_polish() -> str:
    return TODAY.strftime(f"{this_month_last_day()}.{FORMAT_POLISH_MONTH}")


def this_month_first_date_iso() -> str:
    return TODAY.strftime(f"{FORMAT_ISO_MONTH}-{this_month_first_day()}")


def this_month_last_date_iso() -> str:
    return TODAY.strftime(f"{FORMAT_ISO_MONTH}-{this_month_last_day()}")


def to_polish_date(date: str) -> str:
    return datetime.fromisoformat(date[:-5]).strftime(FORMAT_POLISH_DATE)
