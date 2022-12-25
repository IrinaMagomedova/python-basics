'''6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.'''


def int_func_1():
    '''Вариант 1. Принимает слова из строчных латинских букв, возвращает их с прописной первой буквы'''
    my_input = input("Enter words in lowercase latin letters: ")
    for el in my_input:
        if el not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
            print('Invalid value.')
            return
    return my_input.title()


print(int_func_1())


def int_func(var_1):
    '''Вариант 2. Принимает слова из строчных латинских букв, возвращает их с прописной первой буквы'''
    return var_1.title()


print(int_func('text'))
