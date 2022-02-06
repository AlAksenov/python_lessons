"""
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed: float = 0
    is_police: bool = False

    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name

    def go(self):
        self.speed = 30
        print(f'{self.name} started moving')

    def stop(self):
        self.speed = 0
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned to {direction}')

    def add_speed(self):
        self.speed += 20

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            print('You have exceeded tht speed limit')
        return self.speed


class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 40:
            print('You have exceeded tht speed limit')
        return self.speed


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)
        self.is_police = True


if __name__ == '__main__':
    car = Car(name='Mazda', color='black')
    town_car = TownCar(name='BMW', color='white')
    work_car = WorkCar(name='Toyota', color='black')
    police_car = PoliceCar(name='Ford', color='blue')

    # на примере  workCar
    print(work_car.name)
    work_car.go()
    print(f'Начальная скорость {work_car.show_speed()}')
    # ускоряемся
    work_car.add_speed()
    print(f'Скорость {work_car.show_speed()}')
    work_car.add_speed()
    work_car.stop()
