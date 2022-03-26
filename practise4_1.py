from sys import argv
script_name, parametr_1, parametr_2, parametr_3 = argv
print('Virobotka v chasah', parametr_1)
print('Stavka v chas', parametr_2)
print('Premiya', parametr_3)


def my_func(a, b, c):
    d = float(a) * float(b) + float(c)
    return d


print(f'Zarabotnaya plata sotrudnika sostavlyaet: {my_func(parametr_1, parametr_2, parametr_3)}')
