import sys

with open('bakery.csv', 'a', encoding='utf-8') as file:
    file.write(f'{sys.argv[1]}\n')
