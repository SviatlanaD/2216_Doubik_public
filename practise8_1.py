"""
1. Реализовать класс «Дата»
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
В рамках класса реализовать:

    Первый метод - с декоратором @classmethod.
    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число»

    Второй метод - с декоратором @staticmethod
    Он должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)

Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def transform(cls, data):
        data = data.split('-')
        day = int(data[0])
        month = int(data[1])
        year = int(data[2])
        return f'День - {day}, месяц - {month}, год - {year}' \
            f'\nТип данных {type(day), type(month), type(year)}'

    @staticmethod
    def valid(data):
        data = data.split('-')
        day = int(data[0])
        month = int(data[1])
        year = int(data[2])
        if day > 31:
            return f'Неправильно введена дата (день)'
        elif month > 12:
            return f'Неправильно введена дата (месяц)'
        elif year <= 0:
            return f'Неправильно введена дата (год)'
        else:
            return f'Дата введена корректно'


d = '06-12-1987'
print(Date.transform(d))
print(Date.valid(d))
