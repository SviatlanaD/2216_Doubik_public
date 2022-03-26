from math import factorial


def factorial_gen(n):
    for i in range(n+1):
        print(i, end='! = ')
        yield factorial(i)


for el in factorial_gen(int(input('Funkciya factoriala chisel nachinaya c 1! do n!. Vvedite znachenie "n": '))):
    print(el)
