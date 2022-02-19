"""Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""

import requests
import json
from PIL import Image
from urllib.request import urlopen


class MyOwnErr(Exception):
    def __init__(self, message='Incorrect response from Nasa API'):
        self.message = message
        super().__init__(self.message)


def get_nasa_apod(key):
    """Получение картинки дня из API nasa"""
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + key)
    if response.ok:
        j_data = response.json()
        with open('j_nasa.json', 'w') as f:
            json.dump(j_data, f)
        url_picture = j_data.get("url")
        open_img = input('Открыть картинку ? (Y/N): ')
        if open_img == 'Y':
            image = Image.open(urlopen(url_picture))
            image.show()
        return f'Astronomy Picture of the Day at {j_data.get("date")}\nExplanation : {j_data.get("explanation")}' \
               f'\nPicture : {url_picture} '
    else:
        raise MyOwnErr


if __name__ == '__main__':
    key = '1mUieeiy2HzOyMCISIscIUj9v3lbG7FTcaYIXXnw'
    print(get_nasa_apod(key))
