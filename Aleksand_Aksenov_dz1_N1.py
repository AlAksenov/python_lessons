
# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты:
# <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input())

seconds = duration % 60
minutes = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 3600 // 24
data_list = [day, hour, minutes, seconds]
desc_list = ['дн', 'час', 'мин', 'сек']
print_list = []

for i, val in enumerate(data_list):
    if val != 0:
        print_list.append(str(val) + ' ' + desc_list[i])

print(" ".join(print_list))




