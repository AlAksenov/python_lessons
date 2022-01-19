"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import requests
import re
from decimal import Decimal

def currenct_rate(ccy_code):
    """Getting the currency exchange rate"""
    ccy_code = ccy_code.upper()
    cbr_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    pattern_code = r'<CharCode>(.+?)</CharCode>'
    pattern_value = r'<Value>(.+?)</Value>'
    result_code = re.findall(pattern_code, cbr_str)
    result_value = re.findall(pattern_value, cbr_str)
    # При работе с денежными величиными стоить использовать Decimal.
    # Float хранит приблизительное значение, а decimal-точное.
    if ccy_code in result_code:
        return Decimal(result_value[result_code.index(ccy_code)].replace(",", "."))
    else:
        return None


print('Курс USD')
print(currenct_rate('usd'))
print('---------')
print('Курс EUR')
print(currenct_rate('EUR'))
