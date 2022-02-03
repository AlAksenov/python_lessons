"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3
a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
"""

from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            for i in args:
                if not callback(i):
                    msg = f'wrong val {i}'
                    raise ValueError(msg)
                else:
                    return func(*args)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x, *args):
    """calc area"""
    return x ** 3


help(calc_cube)
