"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
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
            if key not in dict_file_sizes:
                dict_file_sizes[key] = 0
            dict_file_sizes[key] += 1
    # сортировка
    sorted_tuple = sorted(dict_file_sizes.items(), key=lambda x: x[0])
    if not dict_file_sizes:
        raise Exception('Дирректория отсутствует или пуста')
    return dict(sorted_tuple)


if __name__ == '__main__':
    # формируем путь к some_data
    path_data = root_dir = os.path.dirname(os.path.abspath(__file__)) + '/some_data'
    print(generate_dict_file_size(path_data))


