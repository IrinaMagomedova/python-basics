'''2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

with open("lesson5.2.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print('Количество строк: ', len(content))
    i= 1
    for string in content:
        words_list = string.split(' ' or ',' or '.'or'-'or ':'or '\n')
        words_quantity = len(words_list)
        print(f'Количество слов в строке {i}: {words_quantity}')
        i += 1
