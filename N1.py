from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from pymongo import MongoClient


s = Service(os.path.dirname(os.path.abspath(__file__)) + '/chromedriver')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=s)
driver.get('https://mail.ru/')


# Авторизация
mail = driver.find_element(By.XPATH, "//div[contains(@class, 'mailbox-services_top')]/a[1]")
driver.get(mail.get_attribute('href'))
driver.implicitly_wait(25)
elem = driver.find_element(By.XPATH, "//input[contains(@name, 'username')]")
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.ENTER)
elem = driver.find_element(By.XPATH, "//input[contains(@name, 'password')]")
elem.send_keys('NextPassword172#')
elem.send_keys(Keys.ENTER)


# Вычисляем кол-во входящих
selection_button = driver.find_element(By.CLASS_NAME, "button2__ico")
selection_button.click()
count_mails = driver.find_element(By.CLASS_NAME, "button2__txt").text
selection_button.click()


# Отбираем ссылки на письма
mail_links = set()

while len(mail_links) != int(count_mails):
    mails = driver.find_elements(By.XPATH, "//a[contains(@class, 'llc_new-selection js-letter-list-item')]")
    for i in mails:
        mail_links.add((i.get_attribute('href')))
    actions = ActionChains(driver)
    actions.move_to_element(mails[-1])
    actions.perform()


# Открываем каждое письмо и собираем инфу
client = MongoClient('127.0.0.1', 27017)
db = client['users2402']
emails_mailru = db.emails_mailru
for i in mail_links:
    driver.get(i)
    try:
        emails_mailru.insert_one({
            'link': i,
            'letter_author': driver.find_element(By.CLASS_NAME, 'letter-contact').get_attribute('title'),
            'letter_date': driver.find_element(By.CLASS_NAME, 'letter__date').text,
            'letter_title': driver.find_element(By.CLASS_NAME, 'thread-subject').text,
            'letter_body': driver.find_element(By.CLASS_NAME, 'letter__body').text
        })
    except:
        print('Mail {i} Not recorded in the database')


# Просмотр собранных данных
for doc in emails_mailru.find({}):
    print(doc)


