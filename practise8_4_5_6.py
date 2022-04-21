"""
4. Начните работу над проектом «Склад оргтехники»
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники
а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class StorageOfficeEquipment:
    def __init__(self):
        pass


class OfficeStorage:

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        self.product = {'Модель': brand, 'Стоимость': price, 'Цвет': color}
        self.products = []
        self.all_products = []

    def __str__(self):
        return f'На складе Офисная техника--> \n Модель:{self.brand}\n Стоимость:{self.price}\n Цвет:{self.color}\n'

    def product_enter(self):
        try:
            brand_new = input(f'Введите модель: ')
            price_new = int(input(f'Введите стоимость: '))
            color_new = input(f'Введите цвет: ')
            new = {'Модель': brand_new, 'Стоимость': price_new, 'Цвет': color_new}
            self.product.update(new)
            print(f'Приход на склад (новый) -\n {self.product}')
            self.products.append(new)
        except:
            return f'Ошибка ввода данных'

        print(f'Для продолжения нажмите - Enter, Для выхода - Q')
        q = input('--> ')
        if q == 'Q' or q == 'q':
            self.all_products.append(self.products)
            print(f'Приход на склад -\n {self.all_products}')
            return f'Ввод товаров на склад окончен'
        else:
            return OfficeStorage.product_enter(self)


class Printer(OfficeStorage):
    def __init__(self, brand, price, color, power):
        super().__init__(brand, price, color,)
        self.power = power
        self.printer_dict = []

    def __str__(self):
        return f'Приход на склад Принтер--> \n Модель:{self.brand}\n Стоимость:{self.price}\n Цвет:{self.color}\n' \
               f' Тип кабеля подключения:{self.power}\n'


class Scaner(OfficeStorage):
    def __init__(self, brand, price, color, resolution):
        self.resolution = resolution
        super().__init__(brand, price, color)
        self.scaner_dict = []

    def __str__(self):
        return f'Приход на склад Сканер--> \n Модель:{self.brand}\n Стоимость:{self.price}\n Цвет:{self.color}\n' \
            f' Разрешение печати:{self.resolution} dpi\n'


class Xerox(OfficeStorage):
    def __init__(self, brand, price, color, speed):
        self.speed = speed
        super().__init__(brand, price, color)
        self.xerox_dict = []

    def __str__(self):
        return f'Приход на склад Ксерокс--> \n Модель:{self.brand}\n Стоимость:{self.price}\n Цвет:{self.color}\n' \
            f' Скорость печати:{self.speed} стр/мин\n'


p = Printer('Lenovo', 2500, 'black', 'Type A')
print(p)
s = Scaner('HP', 2100, 'black', '1200x1200')
print(s)
x = Xerox('Acer', 1800, 'grey', '20')
print(x)
print(p.product_enter())
