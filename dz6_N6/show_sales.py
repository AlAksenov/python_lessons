
import sys


def search_price(start, end, file_path):
    """ search price in file with start end arg"""
    with open(file_path, "r", encoding="utf-8") as prices:
        if start > 0:
            for line in range(start-1):
                prices.readline()
        if end > 0:
            for line in range(end-start+1):
                yield prices.readline().replace('\n', '').replace('.', ',')
        else:
            for line in prices:
                yield line.replace('\n', '').replace('.', ',')


start = 0
end = 0
file_path = "./bakery.csv"

if len(sys.argv) >= 2:
    start = int(sys.argv[1])
if len(sys.argv) == 3:
    end = int(sys.argv[2])
for i in search_price(start, end, file_path):
    print(i)

# python show_sales.py
# python show_sales.py 3
# python show_sales.py 1 3