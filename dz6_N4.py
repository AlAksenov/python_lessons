"""
(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и
название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""

import sys
import json
from itertools import zip_longest
import sys


def read_users_files(users_path, hobby_path):
    """create dict user:hobby for big files"""
    with open(users_path, 'r', encoding="utf-8") as users_file, open(hobby_path, 'r', encoding="utf-8") as hobby_file:
        for user, hobby in zip_longest(users_file, hobby_file):
            yield user.replace('\n', '') if user else sys.exit(1), hobby.replace('\n', '') if hobby else None


def do_user_dict(users_path, hobby_path, out_path):
    """damp dict user:hobby into file"""
    with open(out_path, "w", encoding="utf-8") as out_file:
        for line in read_users_files(users_path, hobby_path):
            print(f"{line[0]}: {line[1]}", file=out_file)
    print('Запись в файл закончена')


def parse_files(file_path):
    """parse users and hobby files"""
    with open(file_path, 'r', encoding="utf-8") as file:
        for i in file:
            i = i.replace('\n', '').split(sep=',')
            yield i


if __name__ == '__main__':
    users_path = "./users.csv"
    hobby_path = "./hobby.csv"
    out_path = "./out_2.txt"

    # Формируем словари
    do_user_dict(users_path, hobby_path, out_path)
    print('----------------')
    # парсим файл с юзерами
    print(*parse_files(users_path))
    print('----------------')
    # парсим файл с хобби
    hobby_list = []
    for i in parse_files(hobby_path):
        hobby_list.extend(i)
    print(hobby_list)
