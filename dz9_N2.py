"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
 """


class Road:
    def __init__(self, length: float = 0, width: float = 0):
        self._length = length
        self._width = width

    def mass_calc(self, asp_mass_m2: float, thickness: float):
        return self._length * self._width * asp_mass_m2 * thickness


if __name__ == '__main__':
    road = Road(length=20, width=5000)
    print('{} т.'.format(int(road.mass_calc(asp_mass_m2=25, thickness=5) / 1000)))

