"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль
Проверьте его работу на данных, вводимых пользователем
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ErrorDivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        delimoe = int(input('Введите делимое: '))
        delitel = int(input('Введите делитель: '))
        if delitel == 0:
            raise ErrorDivZero('Делить на ноль нельзя!')
        else:
            result = delimoe / delitel
            return result
    except ErrorDivZero as err:
        return err


print(div())
