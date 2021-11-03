# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
cubes = []

for number in range(1, 1000, 2):    # Заполнение списка
    cubes.append(number ** 3)
a_total_sum = 0                     # Переменная для хранения результата задания а)
b_total_sum = 0                     # Переменная для хранения результата задания б)

for number in cubes:                # Разбиение числа на цифры и их сложение
    a_temp_str = str(number)        # Расчеты для задания a)
    a_digit_count = (len(a_temp_str))
    a_digit_sum = 0
    a_counter = 0
    # print(f'получили длину числа {number} равную {a_digit_count}')
    #  Расчеты для задания б)
    b_temp_str = str(number + 17)
    b_digit_count = (len(b_temp_str))
    b_digit_sum = 0
    b_counter = 0
    # print(f'получили длину числа {b_temp_str} равную {b_digit_count}')
    while a_digit_count:             # нахождение суммы чисел и сложение
        a_digit_sum += int(a_temp_str[a_counter])
        a_counter += 1
        a_digit_count -= 1
    if a_digit_sum % 7 == 0:
        a_total_sum += number

    while b_digit_count:              # нахождение суммы чисел задания б) и сложение
        b_digit_sum += int(b_temp_str[b_counter])
        b_counter += 1
        b_digit_count -= 1
    if b_digit_sum % 7 == 0:
        b_total_sum += number + 17
    # print(f'сумма цифр равна {b_digit_sum}')
    # print(f'сумма правильных чисел равна {b_total_sum}------------')
print(a_total_sum)
print(b_total_sum)
