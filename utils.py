import requests
import re
from decimal import Decimal
import datetime as dt

def currenct_rate(ccy_code):
    """Getting the currency exchange rate"""
    if type(ccy_code) == list:
        ccy_code = ccy_code[0].upper()
    else:
        ccy_code = ccy_code.upper()
    cbr_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    pattern_code = r'<CharCode>(.+?)</CharCode>'
    pattern_value = r'<Value>(.+?)</Value>'
    pattern_date = r'\d{2}.\d{2}.\d{4}'
    result_code = re.findall(pattern_code, cbr_str)
    result_value = re.findall(pattern_value, cbr_str)
    if ccy_code in result_code:
        result_date = re.findall(pattern_date, cbr_str)
        list_response = [dt.datetime.strptime(result_date[0], '%d.%m.%Y').date(),
                         Decimal(result_value[result_code.index(ccy_code)].replace(",", "."))]
        return list_response
    else:
        return None


if __name__ == '__main__':
    ccy = 'USD'
    ccy_course = currenct_rate(ccy)

    if ccy_course != None:
        print('Курс валюты {} к рублю {} на {}'.format(ccy, ccy_course[1], ccy_course[0]))
    else:
        print('Валюта не найдена')