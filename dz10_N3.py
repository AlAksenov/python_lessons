"""Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В
его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и
выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
"""


class Cell:
    def __init__(self, count_cells: int):
        self.count_cells = count_cells

    def __add__(self, other):
        return Cell(self.count_cells + other.count_cells)

    def __sub__(self, other):
        if self.count_cells < other.count_cells:
            raise ValueError('The difference is greater than zero')
        return Cell(self.count_cells - other.count_cells)

    def __mul__(self, other):
        return Cell(self.count_cells * other.count_cells)

    def __floordiv__(self, other):
        return Cell(self.count_cells // other.count_cells)

    def make_order(self, set_of_cells):
        return ('*' * (set_of_cells) + '\n') * (self.count_cells // set_of_cells) + (
                '*' * (self.count_cells % set_of_cells))

    def __str__(self):
        return f'Клетка из {self.count_cells} ячеек'


if __name__ == '__main__':
    cell1 = Cell(15)
    cell2 = Cell(12)
    print('Сложеие')
    print(cell1 + cell2)
    print('------')
    print('Вычитание')
    print(cell1 - cell2)
    print('------')
    print('Умножение')
    print(cell1 * cell2)
    print('------')
    print('Деление')
    print(cell1 // cell2)
    print('------')
    print('make_order')
    print(cell1.make_order(5))
    print(cell2.make_order(5))
