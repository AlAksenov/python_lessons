"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

"""
from random import randint


def get_jokes(*kwargs):
    """
    Jokes generator
    :param kwargs:
    :return: joke_list
    """
    num_list = kwargs[0]
    jokes_list = []
    while num_list != 0:
        str_joke = kwargs[1][randint(0, len(kwargs[1]) - 1)] + " " + kwargs[2][randint(0, len(kwargs[2]) - 1)] + \
                   " " + kwargs[3][randint(0, len(kwargs[3]) - 1)]
        jokes_list.append(str_joke)
        num_list -= 1

    return jokes_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes_count = 2

print(get_jokes(jokes_count, nouns, adverbs, adjectives))
