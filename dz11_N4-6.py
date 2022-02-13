"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники. """
from abc import ABC
from enum import Enum


class PrintType(Enum):
    COLOR = 1
    BLACK = 2


class PrintFormat(Enum):
    A4 = 1
    A3 = 2
    A5 = 3
    A1 = 4


class Interfaces(Enum):
    USB = 1
    TYPE_C = 2
    WiFi = 3
    ETHERNET = 4
    AIRPRINT = 5


class Compatibility(Enum):
    PC = 1
    PS5 = 2
    SMARTPHONE = 3


class IdIntErr(Exception):
    def __init__(self, message='The ID in list must be numeric'):
        self.message = message
        super().__init__(self.message)


class EmptyStore(Exception):
    def __init__(self, message='There is no equipment in stock'):
        self.message = message
        super().__init__(self.message)


class OfficeEquipmentWarehouse:
    _store_list = []

    @classmethod
    def add_equip(cls, *args):
        for equip in args:
            cls._store_list.append(equip)
            print(f"Добавляем {equip.__class__.__name__} с id {equip.get_id} на склад")

    @property
    def get_store_list(self):
        return self._store_list

    def transfer_equipment(self, id_list: list, department):

        if len(self._store_list) == 0:
            raise EmptyStore()

        # проверяем переданные ид на инт
        for i in id_list:
            if not isinstance(i, int):
                raise IdIntErr()

        for equip in self._store_list:
            if equip.get_id in id_list:
                # удаляем технику со склада
                self._store_list.remove(equip)
                print(f"Убираем {equip.__class__.__name__} с id {equip.get_id} со склада")
                # Передаем технику в отдел
                department.add_equip(equip)


class Department:
    dep_eq_list = []

    def __init__(self, name: str):
        self.name = name

    def add_equip(self, equip):
        self.dep_eq_list.append(equip)
        print(f"Добавляем {equip.__class__.__name__} с id {equip.get_id} в отдел {self.name}")

    @property
    def get_depeq_list(self):
        return self.dep_eq_list


class OfficeEquipment(ABC):
    def __init__(self, __id: int, producer: str, model: str, interfaces: list):
        self.__id = __id
        self.producer = producer
        self.model = model
        self.interfaces = interfaces

    @property
    def get_id(self):
        return self.__id


class Printer(OfficeEquipment):
    print_type: PrintType
    print_format: PrintFormat

    def __init__(self, __id: int, producer: str, model: str, interfaces: list, print_type, print_format):
        self.print_type = print_type
        self.print_format = print_format
        super().__init__(__id, producer, model, interfaces)


class Scanner(OfficeEquipment):
    compatibility: Compatibility

    def __init__(self, __id: int, producer: str, model: str, interfaces: list, compatibility, permission: str):
        self.compatibility = compatibility
        self.permission = permission
        super().__init__(__id, producer, model, interfaces)


class Copier(OfficeEquipment):
    def __init__(self, __id: int, producer: str, model: str, interfaces: list, max_papers: int):
        self.max_papers = max_papers
        super().__init__(__id, producer, model, interfaces)


if __name__ == '__main__':
    # формируем принтер
    printer = Printer(1, 'Xerox', 'XV11', [Interfaces.USB, Interfaces.TYPE_C], PrintType.COLOR, PrintFormat.A4)
    printer2 = Printer(2, 'Xerox', 'XV11', [Interfaces.USB, Interfaces.TYPE_C], PrintType.BLACK, PrintFormat.A4)
    printer3 = Printer(3, 'Xerox', 'GWH', [Interfaces.USB, Interfaces.TYPE_C], PrintType.COLOR, PrintFormat.A1)

    # формируем сканеры
    scanner = Scanner(4, 'HP', 'CC11', [Interfaces.USB, Interfaces.TYPE_C], Compatibility.PC, '600x600 dpi')
    scanner2 = Scanner(5, 'HP', 'RR12', [Interfaces.USB, Interfaces.TYPE_C], Compatibility.PC, '600x600 dpi')
    scanner3 = Scanner(6, 'HP', 'VVZ', [Interfaces.USB, Interfaces.TYPE_C], Compatibility.PC, '600x600 dpi')

    # формируем ксероксы
    copier = Copier(7, 'Xerox', 'CC11', [Interfaces.USB, Interfaces.TYPE_C], 500)
    copier2 = Copier(8, 'Xerox', 'CV3', [Interfaces.USB, Interfaces.TYPE_C], 400)
    copier3 = Copier(9, 'Xerox', 'CC12', [Interfaces.USB, Interfaces.TYPE_C], 300)
    # формируем склад
    store = OfficeEquipmentWarehouse()
    # Передаем всю технику на склад
    store.add_equip(printer, printer2, printer3, scanner, scanner2, scanner3, copier, copier2, copier3)

    # формируем отделы
    department1 = Department('Отдел продаж')

    # Передаем в отдел продаж принтер
    store.transfer_equipment([1, 4, 6, 9], department1)
