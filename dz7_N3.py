"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""

import os
import shutil
import sys


def transferring_templates(root_dir):
    # создаем папку templates в корне проекта my_project
    try:
        path_templates = root_dir + '/my_project/templates'
        if not os.path.exists(path_templates):
            os.mkdir(path_templates)
    except FileNotFoundError:
        print('Дирректория проекта my_project не создана')
        sys.exit(105)
    # Переносим папки и файлы html в templates
    for root, dirs, files in os.walk(root_dir + '/my_project'):
        for file in files:
            if file.endswith(".html"):
                path_templates_dir = os.path.join(path_templates, os.path.basename(root))
                # создаем папку и сразу первый файл
                if not os.path.exists(path_templates_dir):
                    os.mkdir(path_templates_dir)
                    shutil.copy(os.path.join(root, file), os.path.join(path_templates_dir, file))
                # создаем остальные файлы
                elif not os.path.exists(os.path.join(path_templates_dir, file)):
                    shutil.copy(os.path.join(root, file), os.path.join(path_templates_dir, file))



if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__))
    transferring_templates(root_dir)
