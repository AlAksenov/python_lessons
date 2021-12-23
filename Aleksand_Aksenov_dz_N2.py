# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например,
# число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


numbers_cube = [i ** 3 for i in range(1, 1001, 2)]


def sum_numbers(value: object) -> object:
    res = 0
    while value != 0:
        res += value % 10
        value //= 10
    return res


len_list = len(numbers_cube) - 1


def division_7(idx):
    res = 0
    while idx != -1:
        check_number = sum_numbers(numbers_cube[idx])
        if check_number % 7 == 0:
            res += numbers_cube[idx]
        idx += -1
    return res


def division_7_plus_17(idx):
    res = 0
    while idx != -1:
        check_number = sum_numbers(numbers_cube[len_list] + 17)
        if check_number % 7 == 0:
            res += numbers_cube[len_list]
        idx += -1
    return res


print(str(division_7(len_list)) + ' Сумма цифр числа делится нацело на 7')
print(str(division_7_plus_17(len_list)) + ' Сумма цифр числа + 17 делится нацело на 7 ')
