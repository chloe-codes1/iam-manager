import csv

from utils.datetime_handler import DatetimeHandler
from configs.configs import FILE_PATH


class FileHandler:

    def write_file(self, title, contents):
        with open(title + '.txt', 'w') as f:
            for content in contents:
                f.write(f'{content}\n')

    def read_file(self, title):
        with open(title, 'r') as f:
            print(f.read())

    def write_csv_file(self, title, contents):
        datetime = DatetimeHandler()
        current = datetime.get_current_date()
        dict_contents = [{'username': content} for content in contents]
        csv_file_name = FILE_PATH + title + '_' + current + '.csv'
        with open(csv_file_name, 'w', newline='') as f:
            field_names = ['username', 'mfa enabled']
            csv_file = csv.DictWriter(f, fieldnames=field_names)
            csv_file.writeheader()
            for row in dict_contents:
                 csv_file.writerow(row)