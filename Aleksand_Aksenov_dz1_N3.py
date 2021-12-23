# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

numbers = [i for i in range(1, 101)]
percent_text = 'процент'

for i in numbers:
    division_i = i % 10
    if i in (11, 12, 13, 14) or division_i in (5, 6, 7, 8, 9, 0):
        print(str(i) + ' ' + percent_text + 'ов')
    elif division_i == 1:
        print(str(i) + ' ' + percent_text)
    else:
        print(str(i) + ' ' + percent_text + 'а')
