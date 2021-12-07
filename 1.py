from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 6}

    def running(self):
        print("I'm running")
        for light, sec in cycle(self.__color.items()):
            print(f'Now is {light} glow...')
            time.sleep(sec)


lighter_1 = TrafficLight()
lighter_1.running()
