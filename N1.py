"""Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json. """

import requests
import json


class MyOwnErr(Exception):
    def __init__(self, message='Incorrect response from GitHub API'):
        self.message = message
        super().__init__(self.message)


def get_repos(user):
    """Получение списка репозиториев с github"""
    response = requests.get('https://api.github.com/users/' + user + '/repos')
    repos = []
    if response.ok:
        j_data = response.json()
        for repo in j_data:
            repos.append(repo.get('name'))
        with open('j_repo.json', 'w') as f:
            json.dump(repos, f)
    else:
        raise MyOwnErr


if __name__ == '__main__':
    user = 'AlAksenov'
    get_repos(user)
