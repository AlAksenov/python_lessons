import requests
from lxml import html
import datetime
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import re
from pprint import pprint
import unicodedata


def search_news_yandex(block, collection, headers):
    response = requests.get('https://yandex.ru/news/', headers=headers)

    dom = html.fromstring(response.text)
    # сбор новостей с секции Интересное
    blocks = dom.xpath(f'//section[{block}]//div[contains(@class,"mg-grid__item")]')

    for block in blocks:
        news_name = block.xpath('.//h2[@class="mg-card__title"]/a/text()')
        news_link = block.xpath('.//h2[@class="mg-card__title"]/a/@href')
        news_time = block.xpath('.//span[contains(@class,"__time")]/text()')
        cur_date = datetime.datetime.now()
        news_id = re.findall(r'id=\d{9}', news_link[0])
        try:
            news_date = cur_date.replace(hour=int(news_time[0][:1])).replace(minute=int(news_time[0][3:]))
        except:
            news_date = None
        try:
            collection.insert_one({'_id': news_id[0][3:],
                                   'info_source': response.url,
                                   'news_name': unicodedata.normalize("NFKD", news_name[0]),
                                   'news_link': news_link[0],
                                   'news_time': news_date})
        except DuplicateKeyError:
            print(f'Vacancy {news_name} is already exist')
            print(news_link)


if __name__ == '__main__':
    client = MongoClient('127.0.0.1', 27017)
    db = client['users2402']
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}

    news_yandex = db.news_yandex
    news_yandex.delete_many({})
    search_news_yandex(3, news_yandex, headers)
    for doc in news_yandex.find({}):
        pprint(doc)
