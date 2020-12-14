import datetime
import pytz


class DatetimeHandler:

    def __init__(self):
        self.current_datetime = datetime.datetime.now(pytz.timezone('Asia/Seoul'))

    def get_current_time(self):
        return f'{self.current_datetime:%H:%M:%S}'

    def get_current_date(self):
        return f'{self.current_datetime:%Y-%m-%d}'

    def get_current_datetime(self):
        return f'{self.current_datetime:%Y-%m-%d %H:%M:%S}'

