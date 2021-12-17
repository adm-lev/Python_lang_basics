import sys
from random import shuffle, randint
from abc import ABC, abstractmethod
import re


class LottoGame:
    """ Сеанс игры в лото с игроками и карточками"""
    def __init__(self):
        self.players_num = 2
        self.bag1 = self.add_bag()
        self.computer = None
        self.human = None
        self.main()

    def main(self):                                            # функция выполняет весь процесс партии игры
        print(f'Здравствуйте! Вас приветствует игра ЛОТО!')

        self.human = self.add_player(self.get_name(), False)
        self.computer = self.add_player('Вассерман', True)

        while True:
            print(f'Ведущий опускает руку в мешок, перемешивает и ...')
            curr_bar = self.bag1.get_barrel()
            print(f'достает бочонок с номером {curr_bar}.'
                  f' Есть ли такой номер на карточках игроков?\n')
            self.human.mark_field(curr_bar)
            self.computer.mark_field(curr_bar)
            self.human.card.show_card()
            self.computer.card.show_card()
            self.check_win()

    @staticmethod
    def get_name():                                           # функция проверяет корректноть имени игрока
        print('Пожалуйста, введите ваше имя: ')
        while True:
            name = input()
            if re.search(r'\d+', name):
                print('Пожалуйста, введите имя без чисел!: \n')
            else:
                return name

    def check_win(self):                                      # функция проверяет, нет ли сейчас победителей
        if not re.search(r'\d+', self.human.card.card_numbers):
            return self.human.win()
        elif not re.search(r'\d+', self.computer.card.card_numbers):
            return self.computer.win()

    @staticmethod
    def add_bag():                                            # создание экземпляры сумки
        return Bag()

    @staticmethod
    def add_player(name, ai=False):                           # создание экземплра игрока

        if ai:
            return Computer(name)
        else:
            return Human(name)


class Card:
    """ Карточка ЛОТО, заполненная случайно выбранными номерами от 1 до 90"""

    def __init__(self, name):
        self.card_numbers = '-' * 10 + name + '-' * 10 + '\n' + self.__fill_card() + '\n' + '-' * 30

    def show_card(self):                                      # функция рисует карточку
        return print(self.card_numbers)

    def __str__(self):
        return self.card_numbers

    @staticmethod
    def __fill_card():                                        # функция заполняет карточку случайными числами
        numbers = [i for i in range(1, 91)]
        shuffle(numbers)
        front = [sorted(numbers[:5]), sorted(numbers[5:10]), sorted(numbers[10:15])]
        for line in front:
            i = 3
            while i:
                line.insert(randint(0, len(line)), '\t')
                i -= 1

        front = '\n'.join([' '.join(map(str, line)) for line in front])
        return front


class Bag:
    """Сумка, из которой будут браться бочонки"""
    def __init__(self):
        self.numbers = self.__fill_bag()

    @staticmethod
    def __fill_bag():                                          # сумка заполняется бочонками
        numbers = [i for i in range(1, 91)]
        shuffle(numbers)
        return numbers

    def get_barrel(self):                                      # случайный бочонок достается из сумки
        return str(self.numbers.pop())


class Player(ABC):
    """Игрок, который получает карточку и зачеркиавет на ней выпавшие числа"""

    def __init__(self, name='player'):
        self.__name = name.title()
        self.card = self.__get_card(self.__name)
        print(f'{self.__name} присоединился к игре, '
              f'и вытащил карточку:\n {self.card}')

    @abstractmethod
    def mark_field(self, value):                               # функция зачеркивает число на карточке
        pass

    @staticmethod
    def __get_card(name):                                       # функция вручает игроку новую карточку
        return Card(name)

    def win(self):                                              # игрок почеждает при вызове функции
        print(f'Мои поздравления!!!\n {self.__name} первым закрывает все числа и побеждает в игре!')
        sys.exit()

    def loose(self):                                            # игрок проигрывает при вызове функции
        print(f'К сожалению, вы проиграли, {self.__name}!')
        sys.exit()


class Human(Player):

    def mark_field(self, value):
        key = re.compile(fr'(?<=\s){value}(?=\s)')
        while True:
            choice = input(f'есть ли такой номер в вашей карточке? y/n:  ')
            if choice.lower() == 'n':
                if re.search(key, self.card.card_numbers):
                    self.loose()
                else:
                    break
            elif choice.lower() == 'y':
                if not re.search(key, self.card.card_numbers):
                    self.loose()
                else:
                    self.card.card_numbers = re.sub(key, 'X', self.card.card_numbers)
                    break
            else:
                print('недопустимый символ!')


class Computer(Player):
    def mark_field(self, value):
        key = re.compile(fr'(?<=\s){value}(?=\s)')
        if re.search(key, self.card.card_numbers):
            self.card.card_numbers = re.sub(key, 'X', self.card.card_numbers)


game_1 = LottoGame()
