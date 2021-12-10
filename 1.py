class Check:
    def __str__(self):
        return 'Это не матрица'


class Matrix:
    def __init__(self, sample):
        self.sample = sample

    def draw(self, matrix):
        out_string = '\n'.join([' '.join(map(str, line)) for line in matrix])

        return out_string

    def __str__(self):
        return self.draw(self.sample)

    def __add__(self, other_matrix):
        if type(other_matrix) == type(self):
            if len(other_matrix.sample) == len(self.sample):
                summary = []
                temp = []
                for a_1, b_1 in (zip(self.sample, other_matrix.sample)):
                    if len(a_1) == len(b_1):
                        for a_2, b_2 in (zip(a_1, b_1)):
                            temp.append(a_2 + b_2)
                        summary.append(temp.copy())
                        temp.clear()
                    else:
                        print('недопустимый объект')

                return Matrix(summary)
        else:
            print('недопустимый объект')


value = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
value1 = [
    [9, 8, 7], [6, 5, 4], [3, 2, 1]
]
square = Matrix(value)

square_1 = Matrix(value1)


print(square + square_1 + square_1)

square_2 = Check()

print(square_2)


