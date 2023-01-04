'''3. Создать текстовый файл (не программно).
 Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
  Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
  Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32'''

print("Сотрудники с окладом ниже 20 000:")

with open("lesson5.3.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    salary = []
    for line in content:
        staff_salary = line.split(' ')
        if float(staff_salary[1]) < 20000:
            print(f'{staff_salary[0]} {staff_salary[1]}')
        salary.append(float(staff_salary[1]))
    avg = sum(salary) / len(salary)
print(f'Средний оклад составляет: {avg}')
