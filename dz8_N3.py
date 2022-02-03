"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

Сможете ли вы вывести с названием функции
a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        all_args_type = [f' {str(x)}: {type(x)}' for x in all_args]
        all_args_type_func_name = [f' {func.__name__} ({str(x)}: {type(x)})' for x in all_args]
        print('Типы аргументов')
        print(all_args_type)
        print('Типы аргументов c названиями функции')
        print(all_args_type_func_name)
        return func(*args)

    return wrapper


@type_logger
def calc_cuve(x, *args, **kwargs):
    """calc area"""
    return x ** 3


calc_cuve(3, 2, 1, val=5)
