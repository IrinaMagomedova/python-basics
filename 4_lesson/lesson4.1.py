'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, production_in_hours, hourly_rate, premium, name = argv


def salary(arg_1, arg_2, arg_3, arg_4):
    salary = float(arg_1) * float(arg_2) + float(arg_3)
    print(f'Зарплата сотрудника {arg_4} составляет {salary}')


salary(production_in_hours, hourly_rate, premium, name)