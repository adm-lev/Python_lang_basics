class Worker:
    def __init__(self, worker_name, worker_surname, worker_position='стажер', income=(100, 50)):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income = {'wage': income[0], 'bonus': income[1]}
        self.get_position()

    def set_income(self, wag, bon):
        self._income['wage'] = wag
        self._income['bonus'] = bon

    def get_income(self):
        return print(f'зарплата:{self._income["wage"]}, премия: {self._income["bonus"]}')

    def get_position(self):

        return print(f'Создан {self.position}')


class Position(Worker):

    def get_full_name(self):

        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):

        return f'Полный доход составлет {self._income["wage"] + self._income["bonus"]} рублей'


worker_1 = Worker('Vladimir', 'Sharapov')
worker_2 = Position('Глеб', 'Жиглов', 'начальник', (1000, 500))

print('зарбрата первого работника до инфляции')
worker_1.get_income()
worker_1.set_income(1000, 500)
print('зарбрата первого работника после инфляции')
worker_1.get_income()
worker_2.set_income(1200, 600)
print('второй работник')
print(worker_2.get_full_name())
print(worker_2.get_total_income())
