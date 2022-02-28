"""Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем
должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц
сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум: """

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re
from pymongo.errors import DuplicateKeyError
from pprint import pprint


def hh_search(need_vacancy, collection):
    base_url = 'https://hh.ru'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Version/15.3 Safari/605.1.15'}

    url = f'{base_url}/search/vacancy'
    params = {'area': 1, 'fromSearchLine': 'true', 'text': {need_vacancy}, 'page': 0, 'hhtmFrom': 'vacancy_search_list',
              'from': 'suggest_post', 'clusters': 'true', 'order_clusters': 'true'}
    response = requests.get(url, headers=headers, params=params)
    dom = BeautifulSoup(response.text, 'html.parser')
    pagers = dom.find('a', {'data-qa': 'pager-next'}).previousSibling
    count_page = pagers.find('a', {'data-qa': 'pager-page'}).text
    for _ in range(int(count_page)):
        response = requests.get(url, headers=headers, params=params)
        dom = BeautifulSoup(response.text, 'html.parser')
        data = dom.find('div', {'class': 'vacancy-serp'})
        data_list = data.findChildren(recursive=False)
        for vacancy in data_list:
            vacancy_info = vacancy.find('span', {'class': 'g-user-content'})
            if vacancy_info is not None:
                main_info = vacancy_info.findChild()
                vacancy_name = main_info.getText()
                vacancy_link = main_info['href']
                vacancy_id = re.findall(r'\d+', vacancy_link)
                vacancy_salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
                if vacancy_salary is not None:
                    salary = vacancy_salary.getText().split(' ')
                    salary_min = None
                    salary_max = None
                    currency = salary[-1]
                    if 'от' in salary:
                        salary_min = int(salary[1].replace('\u202f', ''))
                    if 'до' in salary:
                        salary_max = int(salary[1].replace('\u202f', ''))
                    if '–' in salary:
                        salary_min = int(salary[0].replace('\u202f', ''))
                        salary_max = int(salary[2].replace('\u202f', ''))
                else:
                    salary_min = None
                    salary_max = None
                    currency = None
                try:
                    collection.insert_one({'_id': vacancy_id[0],
                                           'currency': currency,
                                           'salary_min': salary_min,
                                           'salary_max': salary_max,
                                           'vacanyc_name': vacancy_name,
                                           'vacancy_link': vacancy_link})
                except DuplicateKeyError:
                    print(f'Vacancy {vacancy_name} is already exist')
                    print(response.url)
                    print(vacancy_link)

        params['page'] += 1


def search_vacancy(value, collection):
    for doc in collection.find({'$or': [
        {'salary_min': {'$gte': value}},
        {'salary_max': {'$gte': value}}
    ]}):
        pprint(doc)


if __name__ == '__main__':
    need_vacancy = input('Введи ключевое слово (к примеру Java): ')
    client = MongoClient('127.0.0.1', 27017)
    db = client['users2402']
    vacancy_hh = db.vacancy_hh
    # vacancy_hh.delete_many({})
    hh_search(need_vacancy, vacancy_hh)
    search_vacancy(200000, vacancy_hh)
