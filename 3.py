#  Я увидел способ через Join уже после того, как написа этот.
weather = ['в', '20', 'часов', '6', 'минут', 'температура', 'воздуха', 'была',
           '+50', 'или', '-4', 'градусов']
weather_str = ''
index = 0
open_quotes = False
# расстановка кавычек и нулей. id списка не меняется.
while True:
    if weather[index].isdigit():
        weather[index] = weather[index].zfill(2)
        weather.insert(index, '"')
        weather.insert(index + 2, '"')
        index += 2
    elif '+' in weather[index] or '-' in weather[index]:
        temp = weather[index][1:].zfill(2)
        weather[index] = weather[index][:1] + temp
        weather.insert(index, '"')
        weather.insert(index + 2, '"')
        index += 2
    index += 1
    if index >= len(weather):
        break
index = 0
#  Формирование строки
for word in weather:
    weather_str += word
    if word == '"':
        open_quotes = not open_quotes
    if open_quotes:
        continue
    weather_str += ' '

print(weather_str)
