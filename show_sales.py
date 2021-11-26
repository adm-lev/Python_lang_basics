import sys
from itertools import islice
start, finish = None, None

if sys.argv[1].isdigit():
    start = int(sys.argv[1]) - 1
if sys.argv[2].isdigit():
    finish = int(sys.argv[2])
with open('bakery.csv', encoding='utf-8')as sales:
    lines = islice(sales, start, finish)
    for i in lines:
        print(i, end='')
