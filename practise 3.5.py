"""
Задача решена, но у меня есть вопросы, на которые я не смогла ответить:
** как можно было бы выйти из цикла While True. Изначально использовала While True,
но после введение символа '/' программа все равно продолжалась. Поэтому я ввела переменную 'x'
** не могу понять как сделать, чтобы сумма выводилась только конечная, а не по очереди
Проще говоря, на мою проверку код работает, но чую что-то с ним не так(
"""


def my_func(a):
    b = 0
    i = int(a)
    b = b + i
    return b


result = 0
x = 1
while x == 1:
    numbers = input('vvodite cifri cherez probel, a dlya okonchaniya programmi vvedite "/": ')
    numbers = numbers.split(' ')
    for number in numbers:
        if number != '/':
            result = result + my_func(number)
            print('summa vvedennih elementov = {}'.format(result))
        else:
            x = 2
            print('programma okonchena, summa vvedennich cifr ravna {}'.format(result))
