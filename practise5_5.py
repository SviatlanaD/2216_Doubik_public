"""
Создать (программно) текстовый файл
записать в него программно набор чисел, разделённых пробелами
Программа должна подсчитывать сумму чисел в файле и выводить её на экран
"""

file = open('my_text_5_5.txt', 'w')
file.write(input('Введите числа через пробел: '))
with open('my_text_5_5.txt', 'r') as file:
    a = map(int, file.read().split())
print(f'Summa vvedennih chisel ravna {sum(a)}')
file.close()
