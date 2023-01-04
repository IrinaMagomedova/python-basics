'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран'''
try:
    with open('lesson5.5.txt', 'w+', encoding='utf-8') as f_obj:
        print(input('Введите набор чисел, разделённых пробелами: '), file=f_obj)
        f_obj.seek(0)
        content = f_obj.read()
        my_list = content.split(' ')
        num_list = [float(el) for el in my_list]
        print(sum(num_list))
except IOError:
    print('Произошла ошибка ввода-вывода!')
except ValueError:
    print('Введено недопустимое значение')

