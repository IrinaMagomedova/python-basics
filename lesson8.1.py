"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

from datetime import date

class MyDate:
    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def get_data(cls, dat):
        return list(map(int, dat.split('-')))

    @staticmethod
    def validation(dat):
        numbers = MyDate.get_data(dat)
        try:
            new_date = date(numbers[2], numbers[1], numbers[0])
        except ValueError:
            return "Введено недопустимое значение", dat
        else:
            return "Дата введена успешно", dat


print(MyDate.get_data('19-01-2023'))
print(MyDate.validation('31-1-1982'))
print(MyDate.validation('31-29-2021'))