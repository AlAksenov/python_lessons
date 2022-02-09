"""Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H
+ 0.3). Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property. """

from abc import ABC, abstractmethod


class Closes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Closes):
    def __init__(self, name: str, v: float):
        self.name = name
        self._v = v

    @property
    def a_coat(self):
        return self._v

    def fabric_consumption(self):
        return self.a_coat / 6.5 + 0.5


class Suit(Closes):
    def __init__(self, name, h):
        self.name = name
        self._h = h

    @property
    def a_suit(self):
        return self._h

    def fabric_consumption(self):
        return self.a_suit / 6.5 + 0.5


class MaterialLength:
    _length: float = 0

    @property
    def length(self):
        return self._length

    def __iadd__(self, other):
        self._length = self.length + other.fabric_consumption()
        return self


if __name__ == '__main__':
    res = MaterialLength()
    res += Coat("Joli", 45)
    res += Suit("Norda", 121)
    res += Suit("Varda", 15)
    res += Coat("Volli", 125)
    res += Coat("Gurda", 1111)
    print(res.length)
