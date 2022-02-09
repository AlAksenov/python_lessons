"""еализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 | | 37 43 | | 51 86 | | 3 5 32 | | 2 4 6 | | -1 64 -8 | | 3 5 8 3 | | 8 3 7 1 | Следующий шаг — реализовать
перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка:
сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым
элементом первой строки второй матрицы и пр. """
import collections


class Matrix:
    def __init__(self, matrix_list: list):
        self._matrix = matrix_list

    def __str__(self):
        matrix_col = self.get_matrix_size()[0]
        matrix_str = ''
        while matrix_col > 0:
            matrix_str += f'{self._matrix[-matrix_col]}\n'
            matrix_col -= 1
        return matrix_str.replace(',', '').replace('[', '|').replace(']', '|')

    @property
    def matrix(self):
        return self._matrix

    def __add__(self, other):
        self.check_size(other)
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def get_matrix_size(self):
        matrix_col = len(self.matrix)
        matrix_row_len = []
        for matrix_row in self.matrix:
            matrix_row_len.append(len(matrix_row))
        return [matrix_col, matrix_row_len]

    def check_size(self, other):
        if self.get_matrix_size() != other.get_matrix_size():
            raise ValueError("Matrix's sizes must be equal")


if __name__ == '__main__':
    data_x = [3, 2, 1]
    data_y = [1, 2, 3]

    data_1 = [[31, 22], [37, 43], [51, 86]]
    data_2 = [[31, 22], [37, 43], [51, 86]]
    data_3 = [[1, 1], [1, 1], [1, 1]]

    matrix = Matrix(data_1)
    print(matrix)
    matrix2 = Matrix(data_2)
    print(matrix2)
    matrix3 = Matrix(data_3)
    print(matrix3)
    print('Складываем 3 матрицы')
    matrix23 = matrix + matrix2 + matrix3
    print(matrix23)
