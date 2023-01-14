'''5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pensil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handler(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen('pen')
pensil = Pensil('pensil')
handler = Handler('handler')
my_list = [pen, pensil, handler]
for el in my_list:
    el.draw()
