"""
 Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

"""
import os


def create_structure(path, structure_folder):
    """Generate project folder structure"""
    for root_folder, child_folders in structure_folder.items():
        c_path = os.path.join(path, root_folder)
        if not os.path.exists(c_path):
            os.mkdir(c_path)
        for folder in child_folders:
            print(folder)
            create_structure(c_path, folder)

if __name__ == '__main__':

    path = os.getcwd()
    structure_folder = {
        "my_project": [
            {
                "setting": [],
                "mainapp": [],
                "adminapp": [],
                "authapp": []

            }
        ]
    }

    create_structure(path, structure_folder)


