class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__one_sm_weight = 25

    def solve_weight(self, thickness):
        return self._length * self._width * self.__one_sm_weight * thickness


school_road = Road(5000, 20)

print(f'{school_road.solve_weight(5)} kilogrammes')
