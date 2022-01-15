"""
 (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
 и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
 предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:

 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""

def thesaurus_adv(*args):
    """formation of a dictionary of names"""
    res_dict = {}
    for i in args:
        first_name, last_name = i.split()
        if not res_dict.get(last_name[0]):
            res_dict[last_name[0]] = {first_name[0]: [i]}
        elif not res_dict[last_name[0]].get(first_name[0]):
            (res_dict[last_name[0]])[first_name[0]] = [i]
        else:
            (res_dict[last_name[0]])[first_name[0]].append(i)

    # сортировка списка
    sorted_tuple = sorted(res_dict.items(), key=lambda x: x[0])
    res_dict = dict(sorted_tuple)
    return res_dict

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))