"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:

email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

"""

import re


def email_parse(email):
    """validate email"""
    pattern = re.compile(
        r'(?P<username>([A-Za-z0-9]+[.-_-])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,3})+)')
    result_iter = pattern.finditer(email)
    for i in result_iter:
        res = i.groupdict()
        return res


email = 'someone@geekbrains.ru'
valid_email = email_parse(email)

if valid_email:
    print(valid_email)
else:
    msg = 'wrong email: ' + email
    raise ValueError(msg)
