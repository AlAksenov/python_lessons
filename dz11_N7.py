"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата. """


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%si)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumber(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return ComplexNumber(new_a, new_b)


z1 = ComplexNumber(5, 3)
z2 = ComplexNumber(1, 4)
print(z1 + z2)
print(z1 * z2)
