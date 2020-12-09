import json


class FileHandler:

    def file_writer(self, title, contents):
        with open(title, 'w') as f:
            for content in contents:
                f.write(f'{content}\n')

    def file_reader(self, title):
        with open(title, 'r') as f:
            print(f.read())
