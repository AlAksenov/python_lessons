"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
— на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

"""
import time
from enum import Enum


class Colour(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight:
    _colour: Colour

    def __init__(self, colour):
        self._colour = colour

    def running(self, red_l=7, yellow_l=2, green_l=5):
        while True:
            if self._colour == Colour.RED:
                print("\033[31m {}".format(self._colour.name))
                time.sleep(red_l)
                self._colour = Colour.YELLOW
            elif self._colour == Colour.YELLOW:
                print("\033[33m {}".format(self._colour.name))
                time.sleep(yellow_l)
                self._colour = Colour.GREEN
            elif self._colour == Colour.GREEN:
                print("\033[92m {}".format(self._colour.name))
                time.sleep(green_l)
                self._colour = Colour.RED


if __name__ == '__main__':
    traf = TrafficLight(Colour.GREEN)
    traf.running()

