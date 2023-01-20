"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
class QantityError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    equipment_list = []

    @classmethod
    def receipt(cls, obj):
        cls.equipment_list.append(obj.consignment)

    @classmethod
    def write_off(cls, obj, div):
        pass


class Equipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        try:
            if isinstance(quantity, int):
                self.consignment = {
                    'наименование': self.name,
                    'цена за шт' : self.price,
                    'количество в поставке' : self.quantity}
            else:
                self.consignment = {}
                raise QantityError('Недопустимое значение количества. Данные не будут записаны.')
        except QantityError as err:
            print(err)

class Printer(Equipment):
    def test_printer(self):
        return 'Print test'


class Scanner(Equipment):
    def test_scanner(self):
        return 'Scan test'


class Copier(Equipment):
    def test_xerox(self):
        return 'Make test copy'


consignment1 = Printer('xp laserjet', 700, 100)
consignment2 = Copier('xerox', 500, 10)
consignment3 = Scanner('good one', 600, 50)

print('consignment1', consignment1.consignment)
Warehouse.receipt(consignment1)
Warehouse.receipt(consignment2)

print(Warehouse.equipment_list)
print(consignment3.test_scanner())
