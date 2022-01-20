"""
* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

max_num = 15
odd_nums = (num for num in range(1, max_num + 1) if num % 2 != 0)

print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))