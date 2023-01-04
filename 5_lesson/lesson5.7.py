'''7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
 о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.'''
import json

with open('lesson5.7.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    profit_total = 0
    profit_list = []
    dict_firm = {}
    firm_profit_list = []

    for line in content:
        firm = line.split(' ')
        profit = int(firm[2]) - int(firm[3])
        dict_firm[firm[0]] = profit
        if profit > 0:
            profit_list.append(profit)
    try:
        avg_profit = dict(average_profit=sum(profit_list) / len(profit_list))
    except ZeroDivisionError:
        avg_profit = dict(average_profit=" All firms are unprofitable")
    firm_profit_list = [dict_firm, avg_profit]

with open('lesson5.7.json', 'w') as write_f:
    json.dump(firm_profit_list, write_f)

with open('lesson5.7.json', 'r') as read_f:
    data = json.load(read_f)
    print(data)


