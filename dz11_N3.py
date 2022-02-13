"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
только числами. Класс-исключение должен контролировать типы данных элементов списка. """


class MyOwnErr(Exception):
    def __init__(self, message='The element cannot be a string'):
        self.message = message
        super().__init__(self.message)


my_list = []

while True:
    try:
        element = input('Enter the item to add to the list :')
        if element == 'stop':
            break
        if not element.isdigit():
            raise MyOwnErr()
    except MyOwnErr as err:
        print(err)
    else:
        my_list.append(element)
        continue

print(my_list)