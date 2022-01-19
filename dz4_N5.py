"""
(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
 python task_4_5.py USD
75.18, 2020-09-05
"""

import utils
import sys


ccy_course = utils.currenct_rate(sys.argv[1])
if ccy_course != None:
    print('{}, {}'.format(ccy_course[1], ccy_course[0]))
else:
    print('Валюта не найдена')

#Для запуска из консоли: python dz4_N5.py USD