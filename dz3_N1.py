"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
 num_translate("eight")
 "восемь"
"""

def num_translate(num, translate):
    """num translate ru -> en"""
    try:
        return translate[num]
    except KeyError:
        return None


translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

# Делаем проверкку
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

for i in nums:
    print(num_translate(i, translate_dict))

