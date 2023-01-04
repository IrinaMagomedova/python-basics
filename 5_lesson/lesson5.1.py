'''1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''

with open('lesson5.1.txt', 'w') as out_f:
    my_lst = []
    while True:
        el = str(input('Введите новую строку данных:') + '\n')
        if el == '\n':
            break
        else:
            my_lst.append(el)
    out_f.writelines(my_lst)

with open('lesson5.1.txt', 'r') as out_f:
    print(out_f.read())
