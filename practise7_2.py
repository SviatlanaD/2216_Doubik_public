"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5)
    для костюма (2*H + 0.3)
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, v, h):
        self.size = v
        self.high = h

    @property
    def consumption_total(self):
        total = round((self.size / 6.5 + 0.5 + 2 * self.high + 0.3), 2)
        return f'Общий расход составляет {total} метров ткани'

    @abstractmethod
    def abstract(self):
        return 'абстрактный метод'


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    def consumption_coat(self):
        return f'Для пошива пальто необходимо {round((self.size / 6.5 + 0.5), 2)} метров ткани'

    def abstract(self):
        return 'абстрактный метод Coat'


class Costume(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    def consumption_costume(self):
        return f'Для пошива костюма необходимо {round((2 * self.high + 0.3), 2)} метров ткани'

    def abstract(self):
        return 'абстрактный метод Costume'


ct = Coat(6, 1)
cm = Costume(6, 1)
print(ct.consumption_total)
print(ct.consumption_coat())
print(cm.consumption_costume())
