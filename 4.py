staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for employee in staff:
    name = employee[employee.rfind(' '):]
    print(f'Привет, {name}!'.title())
