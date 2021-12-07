class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):

        message = 'запуск отрисовки'

        return message


class Pen(Stationery):

    def draw(self):

        message = 'Ручка рисует...'

        return message


class Pencil(Stationery):

    def draw(self):

        message = 'Карандаш рисует'

        return message


class Handle(Stationery):

    def draw(self):

        message = 'Маркер рисует'

        return message


first = Pen('red')
second = Pencil('black')
third = Handle('cyan')

print(f'{first.title} {first.draw()}')
print(f'{second.title} {second.draw()}')
print(f'{third.title} {third.draw()}')
