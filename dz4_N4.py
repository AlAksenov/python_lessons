"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

import utils

ccy_course = utils.currenct_rate('usd')
if ccy_course != None:
    print('{}, {}'.format(ccy_course[1], ccy_course[0]))
else:
    print('Валюта не найдена')

