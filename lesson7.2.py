'''2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_for_1pc(self):
        return f'Calculation based on a size or height'


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_for_1pc(self):
        """Метод рассчитывает расход ткани на одно пальто. На вход подаётся значение размера."""
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_for_1pc(self):
        """Метод рассчитывает расход ткани на один костюм. На вход подаётся значение размера."""
        return round(2 * self.height + 0.3, 2)


class Fabric:
    def __init__(self):
        self.coats = []
        self.suits = []
        self.fabric_clothes = []

    def add_coats_fabric(self, name, size):
        """Метод добавляет расход ткани на данное пальто к общему расходу ткани на все уже введённые пальто.
        На вход подаются значения названия и размер экземпляра."""
        self.coats.append(Coat(name, size).fabric_for_1pc)
        return sum(self.coats)

    def add_suit_fabric(self, name, hight):
        """Метод добавляет расход ткани на данный костюм к общему расходу ткани на все уже введённые костюмы.
               На вход подаются значения названия и размер экземпляра."""
        self.suits.append(Suit(name, hight).fabric_for_1pc)
        return sum(self.suits)

    @property
    def total_fabric(self):
        """Метод суммирует расходы ткани на все учтённые пальто и костюмы."""
        self.fabric_clothes = self.coats + self.suits
        return sum(self.fabric_clothes)


coat1 = Coat('casual', 44)
print(f'На пальто {coat1.name} расход ткани составляет {coat1.fabric_for_1pc}м')
coat2 = Coat('new', 46)
print(f'На пальто {coat2.name} расход ткани составляет {coat2.fabric_for_1pc}м')

suit = Suit('official', 185)
print(f'На костюм {suit.name} расход ткани составляет  {suit.fabric_for_1pc}м')

f = Fabric()
f.add_coats_fabric('casual', 44)
f.add_coats_fabric('new', 46)
f.add_suit_fabric('official', 185)
print(f'Расход ткани на пальто и костюмы составляет {round(f.total_fabric, 2)}м')
