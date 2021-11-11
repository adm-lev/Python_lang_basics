from random import randint

#  Создание списка цен
prices = [randint(100, 1000) / 10 for i in range(10)]
print(prices) # Для наглядности
print(f'ID списка до: {id(prices)}')

#  А - Красисый вывод цен
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.', end=', ')
print('\n')
#  B - Вывод по возрастанию
prices.sort()
print(f'ID списка после сортировки: {id(prices)}')
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.', end=', ')
print('\n')
#  C,D - Сортировка по убыванию + пять наибольших
# for price in sorted(prices)[::-1]:
for price in sorted(prices)[::-1][:5]:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.', end=', ')
print('\n')
print([f'{int(price)} руб. {(price - int(price)) * 100:02.0f} коп.' for price in sorted(prices)[::-1][:5]])


