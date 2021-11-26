import sys
"""У меня не была решена 7-я задача, сначала выполнил с ошибкой, затем не хватило времени исправить.
Я разобрал Ваш вариант и понял как он работает"""
pos, data = sys.argv[1:]
with open('bakery.csv', 'r+') as f:
    tmp_file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):
        if i == int(pos):
            tmp_file.write(f'{data}\n')
            change = True
        else:
            tmp_file.write(line)
    if not change:
        exit('error')

    tmp_file.seek(0)

    f.truncate(0)
    for line in tmp_file:
        f.write(line)
    tmp_file.close()
