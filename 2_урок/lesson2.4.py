'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки нужно пронумеровать.
 Если слово длинное, выводить только первые 10 букв в слове.
'''

my_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
my_list = my_str.split(' ')
num = 1
while num <= len(my_list):
    if len(my_list[num - 1]) <= 10:
        print(f'{num} {my_list[num - 1]}')
        num += 1
    else:
        print(f'{num} {my_list[num - 1]:.10}')
        num += 1
