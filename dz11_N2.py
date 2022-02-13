"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyOwnErr(Exception):

    def __init__(self, message='The divisor cannot be zero'):
        self.message = message
        super().__init__(self.message)


in_data = float(input("Enter a number: "))
divider = float(input("Enter a divisor of a number"))
try:
    if divider == 0:
        raise MyOwnErr()

except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(in_data/divider)
finally:
    print("The end")

