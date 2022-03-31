"""
Создать вручную и заполнить несколькими строками текстовый файл
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.


Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Пример json-объекта: # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

with open('my_text_5_7.txt', 'r+', encoding='utf-8') as file:
    info = []
    dic_profit = {}
    dic_loss = {}
    dic_average_profit = {}
    profit = 0
    loss = 0
    a = 0
    av = 0
    for line in file:
        name, firm, income, damage = line.split()
        fin_result = int(income) - int(damage)
        if fin_result >= 0:
            a += 1
            profit = profit + fin_result
            av = profit / a
            dic_profit[name] = fin_result
        else:
            loss = 0
            loss = loss + fin_result
            dic_loss[name] = loss
info.append(dic_profit)
info.append(dic_loss)
if av != 0:
    dic_average_profit['average_profit'] = round(av)
    info.append(dic_average_profit)
else:
    print('Все компании работают в убыток')
print(info)
with open('f.json', 'a+', encoding='utf-8') as json_file:
    json.dump(info, json_file)
