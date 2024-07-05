import datetime

from .common import get_current_month, get_current_year
from .workday import CalendarWorkday
from .file import does_calendar_file_exist


class CalendarMonth:

    def __init__(self, year=None, month=None):
        if year is None:
            year = get_current_year()
        self.__year = year

        if month is None:
            month = get_current_month()
        self.__month = month

        self.__days_in_month = datetime.datetime(year, month, 1).days_in_month

    def init(self):
        # Loop over each day in current month
        for day in range(1, 32):
            # Create a new day object
            day = CalendarDay(day, self.__month, self.__year)
            # Initialize the day
            day.init()

    def reset(self):
        print("Ending the month")
