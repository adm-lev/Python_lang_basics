from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def calculate_cons(self):
        pass


class Coat(Clothes):

    @property
    def calculate_cons(self):
        consumption = self.param / 6.5 + 0.5
        return consumption


class Suit(Clothes):

    @property
    def calculate_cons(self):
        consumption = 2 * self.param + 0.3
        return consumption


smoking = Suit('smoking', 50)
french = Coat('french', 100)

print(smoking.calculate_cons)
print(french.calculate_cons)

