def currency_rates(name):
    from requests import get, utils
    from decimal import Decimal
    from datetime import date

    #  Загружаем содержимое документа, помещаем его в строку.
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    #  Проверка входных данных
    ind = content.find(name.upper())
    if ind == -1:
        return None
    # Получение значения, номинала, названия и даты
    cur_date = content[content.find('ValCur')+14:content.find('ValCur')+24]
    current_content = content[ind:ind + 150]
    value = current_content[current_content.find('<Value>') + 7: current_content.find('</Value>')]
    nominal = current_content[current_content.find('<Nominal>')+9:current_content.find('</Nominal>')]
    rus_name = current_content[current_content.find('<Name>') + 6: current_content.find('</Name>')]
    value = value.split(',')
    value = (int(value[0]) + (Decimal(value[1])/10000)) / int(nominal)
    cur_date = cur_date.split('.')
    cur_date = date(int(cur_date[2]), int(cur_date[1]), int(cur_date[0]))
    total_info = f'Курс {rus_name}:  {value} состоянием на {cur_date}'

    #  return value # эта строка заменяет вывод функции на числовой, как требуется в задании 2.
    #  Для красоты в последующих версиях задания я использую строку.
    return total_info


if __name__ == '__main__':

    print(currency_rates(input('Введите, пожалуйста, название валюты: ')))
