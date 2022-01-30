"""
вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
"""

import os
import yaml


# Задача оч классная :)

def create_structure(conf_file, path):
    """Generate project folder structure"""
    for k, v in conf_file.items():
        folder_path = os.path.join(path, k)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for i in v:
            if isinstance(i, dict):
                create_structure(i, folder_path)
            else:
                file_path = os.path.join(path, k, i)
                if not os.path.exists(file_path):
                    open(file_path, "a")


if __name__ == '__main__':
    try:
        with open("./config.yaml", "r", encoding="utf-8") as conf_yaml:
            conf = yaml.load(conf_yaml, Loader=yaml.FullLoader)
        path = os.getcwd()
        create_structure(conf, path)
    except:
        print('файл .yaml не валиден')
