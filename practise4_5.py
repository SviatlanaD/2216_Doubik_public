from functools import reduce
my_list = [el for el in list(range(100, 1001)) if el % 2 == 0]


def mult(a, b):
    return a * b


print(reduce(mult, my_list))
