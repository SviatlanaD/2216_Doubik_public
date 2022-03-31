# Создать программный файл в текстовом формате
# записать в него построчно данные, вводимые пользователем
# Об окончании ввода данных будет свидетельствовать пустая строка
# ПОСТРОЧНО - текст вводится с новой строчки пользователем и записывается в файл с новой строчки:

f_obj = open('my_text.txt', 'w', encoding='utf-8')
line = input('vvedite text: \n')
while line:
    f_obj.writelines(line + '\n')
    line = input('vvedite text: \n')
    if not line:
        break

f_obj.close()
f_obj = open('my_text.txt', 'r', encoding='utf-8')
content = f_obj.readlines()
print(content)

f_obj.close()

# ПОСТРОЧНО - текст вводится с новой строчки пользователем,
# а в файл записывается не важно как (напр. через пробел)
# чтобы инфа сохранилась в txt использую 'a' вместо 'r':

f_obj = open('my_text.txt', 'a', encoding='utf-8')
line = input('vvedite text: \n')
while line:
    f_obj.writelines(line + ' ')
    line = input('vvedite text: \n')
    if not line:
        break

f_obj.close()
f_obj = open('my_text.txt', 'r', encoding='utf-8')
content = f_obj.readlines()
print(content)

f_obj.close()
