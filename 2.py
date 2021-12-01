import re


#  Функция получает строку и разбивает ее на слова согласно шаблону
def gather_2(line):
    result = []
    group_line = SEARCH_KEY.finditer(line)
    tuple((map(lambda i: result.append(i.group()), group_line)))
    return tuple(result)


#  Шаблон поиска содержит 6 групп, включая ipv6 адрес.
SEARCH_KEY = re.compile('(^(?:\d{1,3}\.){3}\d+)|(^(?:[\da-f]{3,4}:){7}[\da-f]{3,4}(?=\s))|'
                        '((?:\/\w+){2}(?=\s))|((?<=")[A-Z]+(?=\s))|(\d{1,2}\/\w+\/\d{4}(?::\d{2}){3}\s\+\d{4})|'
                        '((?<="\s)\d+(?=\s))|((?<=\s)\d+(?=\s"))')
#  Весь файл считвывается в список из строк
with open('nginx_logs.txt', encoding='utf-8') as log:
    lines = log.readlines()
#  К каждой строке применяется функция gather_2
mapped_lines = list(map(gather_2, lines))
# Запись в файл облегчает проверку результата и тестирование кода
with open('filtered_log.txt', 'a', encoding='utf-8') as saved:
    saved.truncate(0)
    for num, line in enumerate(mapped_lines):
        saved.write(f'{line}\n')

