"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
 Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
 Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
Дополнительные материалы"""


class Complex_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = a + b*1j

    def __add__(self, other):
        self. a_res = self.a + other.a
        self. b_res = self.b + other.b
        return self.a_res + self.b_res*1j

    def __mul__(self, other):
        self.a_res = self.a * other.a - self.b * other.b
        self.b_res = self.a * other.b + self.b * other.a
        return self.a_res + self.b_res * 1j


num1 = Complex_number(2, 1)
num2 = Complex_number(3, 4)
print(num1.z)

print(num1 + num2)
print(num1 * num2)

