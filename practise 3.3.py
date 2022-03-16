# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# возвращает сумму наибольших двух аргументов
def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(d))
    result = sum(d)
    return result


print(my_func(-5, 125, 0))
