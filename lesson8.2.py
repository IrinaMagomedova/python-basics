"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой."""


class DivisorError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(dividend, divisor):
    try:
        if divisor == 0:
            raise DivisorError("Делитель не может быть равен нулю")
    except DivisorError as err:
        print(err)
    else:
        print(dividend / divisor)


division(10, 5)
division(10, 0)
