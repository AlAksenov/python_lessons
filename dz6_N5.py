"""
** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим
 исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
 когда все файлы находятся в разных папках.
"""
from dz6_N4 import *
import os

if len(sys.argv[1:]) >= 3:
    users_path = sys.argv[1]
    hobby_path = sys.argv[2]
    out_path = sys.argv[3]

try:
    do_user_dict(users_path=users_path, hobby_path=hobby_path, out_path=out_path)
except:
    print('Вы ввели недостоатнчоное кол-во атрибутов')
    print(
        'Запускайте скрипт в формате python dz6_N5.py (путь к users.csv) (путь к hobby.csv) (путь к файлу результата)')

# Для запуска из консоли: python dz6_N5.py ./users.csv ./hobby.csv ./out.txt
