class Car:
    def __init__(self, name, speed=20, color='black'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):

        return print(f'Машина поехала...')

    def stop(self):

        return print(f'Машина остановилась...')

    def turn(self, direction):

        return print(f'Машина повернула {direction}')

    def show_speed(self):

        return print(f'Текущая скорость равна {self.speed}')


class TownCar(Car):

    def show_speed(self):

        message = f'Текущая скорость равна {self.speed}\n'
        if int(self.speed) > 60:
            message += 'Внимание! Превышение скорости!'

        return print(message)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):

        message = f'Текущая скорость равна {self.speed}\n'
        if int(self.speed) > 40:
            message += 'Внимание! Превышение скорости!'

        return print(message)


class PoliceCar(Car):

    def turn_lights(self):
        message = f'сирена включена'
        return print(message)


mercedes = WorkCar(name='Mercedes', speed=160, color='silver')
shelby = PoliceCar(name='Shelby')
lincoln = TownCar('Lincoln', 60, 'white')

(shelby.turn_lights())


mercedes.show_speed()
print(mercedes.color)
mercedes.turn('влево')
mercedes.go()
lincoln.show_speed()
