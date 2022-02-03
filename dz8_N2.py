"""
(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt

получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
<response_code>, <response_size>), например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'

parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""
import re

pattern = re.compile(r"(?P<remote_addr>^\S+)[\s-]*\[(?P<request_datetime>.*)\]\s*\"(?P<request_type>\w*)\s*(?P<requested_resource>[/\w]+)[^\"]+\"\s+("
                     r"?P<response_code>\d+)\s+(?P<response_size>\d+)")


with open("nginx_logs.txt", "r", encoding= "utf-8") as logs_file:
    for line in logs_file:
        result = pattern.findall(line)
        print(result[0])

