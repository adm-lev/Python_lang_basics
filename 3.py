class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):

        return str(self.number)

    def __add__(self, other):

        return Cell(self.number + other.number)

    def __sub__(self, other):
        calc = self.number - other.number
        if calc:
            return Cell(calc)
        else:
            print('найдите клетку побольше')

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        if self.__floordiv__(other):
            return self.__floordiv__(other)
        else:
            return 'неправильное деление'

    def __floordiv__(self, other):
        return self.number // other.number

    def make_order(self, value):
        for i in range(self.number // value):
            print('*' * value)
        print('*' * (self.number % value))


cell_0 = Cell(50)
cell_1 = Cell(60)
cell_2 = Cell(20)


print(cell_0 + cell_2 + cell_0)
print(cell_1 - cell_2)
print(cell_0 * cell_1)
print(cell_1 / cell_2)
print(cell_2 / cell_0)
cell_1.make_order(11)


