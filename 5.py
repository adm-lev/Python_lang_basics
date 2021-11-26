# -*- coding: cp1251 -*-
import sys

""" В качестве аргументов получил названия файлов. Открыл их одновременно, чтобы в процессе работы с файлами у других 
пользователей не было возможности вмешиваться в их содержимое. Цикл поочередно берет строки из двух файлов, форматирует
их и записывает в файл назначения, если не происходит досточное завершение с кодом 0 либо 1"""
source_one, source_two, dest = sys.argv[1:]
"""Файл назначения открываю с ключом w для удобства многократной проверки скрипта
без необхоимости очищать файл"""
with open(source_one, encoding='utf-8') as u, open(source_two, encoding='utf-8') as h,\
        open(dest, 'w', encoding='utf-8') as uh:
    while True:
        line_1, line_2 = u.readline().strip(), h.readline().strip()
        if line_2 == '':
            line_2 = 'None'
        if line_1 == '':
            if line_2 == 'None':
                break
            else:
                raise SystemExit(1)
        uh.write(f'{line_1.strip()}: {line_2.strip()}\n')
