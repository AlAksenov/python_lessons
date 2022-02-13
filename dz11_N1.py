"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных. """


class Date:
    date_string = None

    def __init__(self, date_string: str):
        self.data_string = date_string

    @classmethod
    def split_date(cls, date_string: str):
        date_list = list(map(int, date_string.split('-')))
        if date_list is None:
            raise ValueError('Cant split this')
        return date_list

    @staticmethod
    def validate_date(date_string: str):

        day, month, year = Date.split_date(date_string)

        if not 1 <= month <= 12:
            raise ValueError('Incorrect month, 1 <= month <= 12')

        if month in [4, 6, 9, 11] and day == 31:
            raise ValueError('Incorrect month, there cannot be 31 days in months 4, 6, 9, 11')

        if not year > 0:
            raise ValueError('Incorrect year, year > 0')


        if not 1 <= day <= 31:
            raise ValueError('Incorrect day, 1 <= day <= 31')

        if (
                month == 2 and
                day == 29 and
                year % 4 != 0 and
                year % 100 != 0 and
                year % 400 != 0
        ):
            raise ValueError('Incorrect data for leap year')

        return day, month, year


data = Date.validate_date('02-12-2021')

print(data)
