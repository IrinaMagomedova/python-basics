'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([' '.join(map(str, row)) for row in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


matrix1 = Matrix([[31, 32], [37, 43], [51, 86]])
print(matrix1.matrix)
print(matrix1)
matrix2 = Matrix([[9, 8], [3, -3], [19, -16]])

print(matrix1+matrix2)




"""
Второй вариант перегрузки __str__ (который был первым):
    def __str__(self):
        new_row = []
        for row in self.matrix:
            my_list = []
            for i in row:
                my_list.append(str(i))
            new_row.append(' '.join(my_list))
        return str('\n'.join(new_row))

"""