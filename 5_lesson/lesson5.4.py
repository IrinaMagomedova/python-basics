'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
  Новый блок строк должен записываться в новый текстовый файл.'''

dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('lesson5.4.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    rus_content = []
    for line in content:
        my_list = line.split(' ', 1)
        my_list[0] = dict.get(my_list[0])
        rus_content.append(' '.join(my_list))

with open('lesson5.4rus.txt', 'w+', encoding='utf-8') as f_rus:
    for line in rus_content:
        print(line, file=f_rus)
    f_rus.seek(0)
    content = f_rus.read()
    print(content)

