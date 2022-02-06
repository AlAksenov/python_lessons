"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f'Что-то пишем...')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print(f'Что-то чертим...')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f'Что-то рисуем...')


if __name__ == '__main__':
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    for item in [pen, pencil, handle]:
        print(f'{item.title}: ', end='')
        item.draw()


