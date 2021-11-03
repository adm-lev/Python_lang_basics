# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
numbers = []
for i in range(100):
    numbers.append(i+1)

for number in numbers:
    number = str(number)
    if int(number) > 10 and number[-2] == '1':
        print(f'{number} процентов')
    elif number[-1] == '1':
        print(f'{number} процент')
    elif number[-1] == '2' or number[-1] == '3' or number[-1] == '4':
        print(f'{number} процента')
    else:
        print(f'{number} процентов')
