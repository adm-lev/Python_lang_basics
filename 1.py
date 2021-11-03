# 1 день = 86400с
# 1 час = 3600с
# 1 минута = 60с
# Нахождение числа каждой единицы времени
while True:
    duration = int(input('Введите, пожалуйста число секунд или "0" для выхода:\n'))
    if duration == 0:
        break
    days = duration // 86400
    hours = (duration - (days * 86400)) // 3600
    minutes = (duration - (hours * 3600) - (days * 86400)) // 60
    seconds = (duration - (minutes * 60)) - (days * 86400) - (hours * 3600)

# Выбор формата выводимого результата
    if days:
        print(f"{days} дн {hours} час {minutes} мин {seconds} сек")
    elif hours:
        print(f"{hours} час {minutes} мин {seconds} сек")
    elif minutes:
        print(f"{minutes} мин {seconds} сек")
    else:
        print(f"мин {seconds} сек")
