"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""


def log_parser(file_path):
    """ parser for log file"""
    with open(file_path, "r", encoding="utf-8") as logs_file:
        for line in logs_file:
            ip = line.split(" - - ")[0]
            method_url = line.split('"')[1]
            method = method_url.split()[0]
            url = method_url.split()[1]
            yield ip, method, url


if __name__ == '__main__':
    result_logs = log_parser(file_path="./nginx_logs.txt")
    print(next(result_logs))
    print(next(result_logs))
    print(next(result_logs))
