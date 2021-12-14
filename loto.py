import sys
from random import shuffle
from abc import ABC, abstractmethod
import re


class LottoGame:
    """ Сеанс игры в лото с игроками и карточками"""
    def __init__(self):
        self.players_num = 2
        self.names = []                         # список с экзеплярами игроков
        self.bag1 = self.add_bag()
        self.computer = None
        self.human = None
        self.main()

    def main(self):
        print(f'Здравствуйте! Вас приветствует игра ЛОТО!')

        human_name = input('Введите ваше имя: ')
        self.human = self.add_player(human_name, False)
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

    def check_win(self):
        if not re.search(r'\d+', self.human.card.card_numbers):
            return self.human.win()
        elif not re.search(r'\d+', self.computer.card.card_numbers):
            return self.computer.win()

    @staticmethod
    def add_bag():
        return Bag()

    @staticmethod
    def add_player(name, ai=False):

        if ai:
            return Computer(name)
        else:
            return Human(name)


class Card:
    """ Карточка ЛОТО, заполненная случайно выбранными номерами от 1 до 90"""

    def __init__(self, name):
        self.card_numbers = '-' * 10 + name + '-' * 10 + '\n' + self.__fill_card() + '\n' + '-' * 30

    def show_card(self):
        return print(self.card_numbers)

    def __str__(self):
        return self.card_numbers

    @staticmethod
    def __fill_card():
        numbers = [i for i in range(1, 91)]
        shuffle(numbers)
        front = [numbers[:5], numbers[5:10], numbers[10:15]]
        list(map(lambda x: x.extend([0, 0, 0]), front))
        list(map(shuffle, front))
        front = '\n'.join([' '.join(map(str, line)) for line in front]).replace('0', '\t')
        return front


class Bag:
    """Сумка, из которой будут браться бочонки"""
    def __init__(self):
        self.numbers = self.__fill_bag()

    @staticmethod
    def __fill_bag():
        numbers = [i for i in range(1, 91)]
        shuffle(numbers)
        return numbers

    def get_barrel(self):
        return str(self.numbers.pop())


class Player(ABC):
    """Игрок, который получает карточку и зачеркиавет на ней выпавшие числа"""

    def __init__(self, name='player'):
        self.__name = name.title()
        self.card = self.__get_card(self.__name)
        print(f'{self.__name} присоединился к игре, '
              f'и вытащил карточку:\n {self.card}')

    @abstractmethod
    def mark_field(self, value):
        pass

    @staticmethod
    def __get_card(name):
        return Card(name)

    def win(self):
        print(f'Мои поздравления!!!\n {self.__name} первым закрывает все числа и побеждает в игре!')
        sys.exit()

    def loose(self):
        print(f'К сожалению, вы проиграли, {self.__name}!')
        sys.exit()


class Human(Player):

    def mark_field(self, value):
        key = re.compile(fr'(?<=\s){value}(?=\s)')
        choice = input(f'есть ли такой номер в вашей карточке? y/n:  ')
        if choice == 'n':
            if re.search(key, self.card.card_numbers):
                self.loose()
        elif choice == 'y':
            if not re.search(key, self.card.card_numbers):
                self.loose()
            else:
                self.card.card_numbers = re.sub(key, 'X', self.card.card_numbers)


class Computer(Player):
    def mark_field(self, value):
        key = re.compile(fr'(?<=\s){value}(?=\s)')
        if re.search(key, self.card.card_numbers):
            self.card.card_numbers = re.sub(key, 'X', self.card.card_numbers)


game_1 = LottoGame()
