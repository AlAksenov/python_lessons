"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:

thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?

"""


def thesaurus(*args):
    """formation of a dictionary of names"""
    # формируем список ключей
    name_list = list(set(map(lambda x: x[0], args)))
    # формируем словарь
    name_dict = dict.fromkeys(name_list, [])
    for i in args:
        for key in name_dict:
            if i[0] == key:
                name_dict[key] = name_dict.setdefault(key, []) + [i]
    # сортировка словаря
    sorted_tuple = sorted(name_dict.items(), key=lambda x: x[0])
    name_dict = dict(sorted_tuple)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
