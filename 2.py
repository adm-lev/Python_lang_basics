addresses = []
spammer = (None, 0)
"""  Берется по очереди каждая строка, разделяется по символам пробела.
Первый элемент помещается в список.   """
with open('nginx_logs.txt', encoding='utf-8') as file_1:
    for line in file_1:
        temp = line.split()
        addresses.append(temp[0])

#  Затем находится элемент, который встречается чаще других
for address in addresses:
    if spammer[0] == address:
        continue
    elif spammer[1] < addresses.count(address):
        spammer = (address, addresses.count(address))


print(f'Внимание! Пойман спамер под IP адресом {spammer[0]}, отправивший {spammer[1]} запросов.')
