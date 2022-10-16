import datetime
import re
import os
import time
from pathlib import Path
import math

route = '/Users/hugoroca/personalProjects/python-total-course/Day 09/project_day_09/Mi_Gran_Directorio'
pattern = r'N\D{3}-\d{5}'
today = datetime.date.today()
numbers_found = []
files_found = []
start = time.time()


def search_number(file, regex_pattern):
    this_file = open(file, 'r')
    text = this_file.read()

    if re.search(regex_pattern, text):
        return re.search(pattern, text)
    else:
        return ''


def create_list():
    for folders, sub_folders, file in os.walk(route):
        for a in file:
            result = search_number(Path(folders, a), pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(a.title())


def show_all():
    index = 0
    print('-' * 50)
    print(f'Date: {today.day}/{today.month}/{today.year}')
    print('\n')
    print('FILE\t\t\t\tNRO. SERIAL')
    print('----\t\t\t\t-----------')

    for i in files_found:
        print(f'{i}\t{numbers_found[index]}')
        index += 1

    print('\n')
    print(f'Found numbers: {len(numbers_found)}')
    end = time.time()
    duration = end - start
    print(f'Found Duration: {math.ceil(duration)} seconds')
    print('-' * 50)


create_list()
show_all()
