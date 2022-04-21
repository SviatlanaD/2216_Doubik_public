"""
Формула умножения комплексных чисел a 1 *a 2 - b 1 *b 2 +i*(a 1 *b 2 +a 2 *b 1)
"""


def my_func_a(d):
    if d < 0:
        return f'- {abs(d)} '
    else:
        return f'{d} '


def my_func_b(d):
    if d < 0:
        return f'- {abs(d) }'
    else:
        return f'+ {d}'


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a_1 = my_func_a(self.a + other.a)
        b_1 = my_func_b(self.b + other.b)
        return f'Сумма заданных комплексных чисел равна: \n {a_1}{b_1} * i'

    def __mul__(self, other):
        a_2 = my_func_a(self.a * other.a - self.b * other.b)
        b_2 = my_func_b(self.a * other.b + self.b * other.a)
        return f'Произведение заданных комплексных чисел равно: \n {a_2}{b_2} * i'

    def __str__(self):
        return f'Комплексное число: \n {my_func_a(self.a)}{my_func_b(self.b)} * i'


cn_1 = ComplexNumber(-1, 2)
cn_2 = ComplexNumber(-3, -4)
print(cn_1)
print(cn_2)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
