"""
* (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""

import sys
import fileinput


def edit_price(idx_price, new_price, file_path):
    """ search price in file with start end arg"""
    new_price = new_price.replace(',', '.')
    for idx, line in enumerate(fileinput.input(file_path, inplace=True)):
        if idx == idx_price - 1:
            line = line.replace(line, f'{new_price}\n')
        sys.stdout.write(line)


file_path = "./bakery.csv"

if len(sys.argv) == 3:
    idx_price = int(sys.argv[1])
    new_price = str(sys.argv[2])
    edit_price(idx_price, new_price, file_path)
    print('Строк {} заменила значение на {}'.format(idx_price, new_price))
else:
    print("Необходимо ввести 2 параметра номер строки и новую цену")

# Для замены первой записи
# Скрипт для запуска python edit_sales.py 1 5555,3
#Для замены второй записи
# Скрипт для запуска python edit_sales.py 2 7777,3