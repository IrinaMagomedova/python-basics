'''4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость автомобиля:{self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed <= 60:
            print(f'Скорость автомобиля:{self.speed} км/ч')
        else:
            print(f'Превышение скорости на :{self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed <= 40:
            print(f'Скорость автомобиля:{self.speed} км/ч')
        else:
            print(f'Превышение скорости на :{self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car1 = TownCar(200, 'красный', 'городская VW', False)
car2 = SportCar(400, 'белый', 'спортивная Ferrari', False)
car3 = WorkCar(100, 'жёлтый', 'рабочая VAZ', False)
car4 = PoliceCar(200, 'серый+синий', 'VAZ', True)

my_list = [car1, car2, car3, car4]
for el in my_list:
    print(f'Машина {el.color} {el.name}, макс скорость {el.speed} км/ч, полицейская: {el.is_police}')
    el.go()
    el.stop()
    el.turn('направо')
    el.show_speed(70)