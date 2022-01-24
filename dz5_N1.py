"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...

"""


def odd_nums(max_number):
    for num in range(1, max_number + 1):
        if num % 2 != 0:
            yield num

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))