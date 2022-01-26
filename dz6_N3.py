"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
"""
import sys
import json


def do_user_dict(users_path, hobby_path, out_path):
    """create dict user:hobby and dump into out file"""
    with open(users_path, 'r', encoding="utf-8") as users_file:
        users = users_file.read().splitlines()
    with open(hobby_path, 'r', encoding="utf-8") as hobby_file:
        hobby = hobby_file.read().splitlines()
    if len(hobby) < len(users):
        hobby.extend([None for dif in range(len(users) - len(hobby))])
    elif len(hobby) > len(users):
        sys.exit(1)
    out_dict = zip(users, hobby)
    with open(out_path, "w", encoding="utf-8") as out_file:
        json.dump(dict(out_dict), out_file)

users_path = "./users.csv"
hobby_path = "./hobby.csv"
out_file = "./out.txt"
do_user_dict(users_path, hobby_path, out_file)

