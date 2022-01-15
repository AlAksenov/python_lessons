"""
(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
"""


def num_translate_adv(num, translate):
    """num translate ru -> en"""
    try:
        if num[0].isupper():
            return translate[num.lower()].capitalize()
        return translate[num]
    except KeyError:
        return None


translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

# Делаем проверкку
nums = ['Zero', 'one', 'two', 'three', 'Four', 'five', 'six', 'Seven', 'eight', 'nine', 'ten']

for i in nums:
    print(num_translate_adv(i, translate_dict))
