"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
"""

from dz6_N1 import log_parser
from collections import Counter


def find_spam(data):
    """find spammer user in log file"""
    counter_dict = Counter([x[0] for x in data])
    return counter_dict.most_common(1)[0]


result_logs = log_parser(file_path="./nginx_logs.txt")
result_spam = find_spam(result_logs)
print('IP спамера {}, было {} обращений'.format(result_spam[0], result_spam[1]))
