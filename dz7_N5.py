"""
(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
"""


import os


def generate_dict_file_size(pth):
    """generate file_size dict"""
    # формирование словаря
    dict_file_sizes = {}
    for root, _, files in os.walk(pth):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            key = 10 ** len(str(file_size))
            file_extension = os.path.splitext(file)[-1].replace('.', '')
            count, extension = dict_file_sizes.get(key, (0, set()))
            extension.add(file_extension)
            count += 1
            dict_file_sizes[key] = (count, extension)


    # сортировка
    sorted_tuple = sorted(dict_file_sizes.items(), key=lambda x: x[0])
    if not dict_file_sizes:
        raise Exception('Дирректория отсутствует или пуста')
    return dict(sorted_tuple)


if __name__ == '__main__':
    # формируем путь к some_data
    path_data = root_dir = os.path.dirname(os.path.abspath(__file__)) + '/some_data'
    print(generate_dict_file_size(path_data))



