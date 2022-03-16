def my_funct(arg_1, arg_2):
    try:
        arg_3 = arg_1 / arg_2
        return arg_3
    except ZeroDivisionError:
        return 'Delit na 0 nelzya'


a = int(input('Vvedite delimoe: '))
b = int(input('Vvedite delitel: '))
print('Chastnoe ot {} i {} budet {}'.format(a, b, my_funct(a, b)))