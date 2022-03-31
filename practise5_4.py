"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл
"""
my_file = open('my_text_5_4.txt', 'r+')
with my_file as f:
    my_list = list()
    for line in f.readlines():
        my_list.extend(line.split(' '))
rus_list = ["Один", "Два", "Три", "Четыре"]
a = 0
for i in range(0, len(my_list), 3):
    my_list[i] = rus_list[a]
    a += 1
new_file = open('my_text_5_4.txt', 'w', encoding='utf-8')
new_file.writelines(my_list)
new_file.close()
