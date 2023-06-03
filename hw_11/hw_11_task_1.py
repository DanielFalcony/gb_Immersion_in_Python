"""
Создайте класс Матрица.
Добавьте методы для:
1) вывода на печать,
2) сравнения,
3) сложения,
4) умножения матриц (транспонирование)
"""


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def __str__(self) -> str:
        rows = []
        for row in self.matrix:
            row_str = ' '.join(str(elem) for elem in row)
            rows.append(row_str)
        return '\n'.join(rows)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.matrix == other.matrix

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type for +: 'Matrix' and {}".format(type(other)))
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Cannot add matrices of different sizes")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def transpose(self):
        transposed = []
        for j in range(len(self.matrix[0])):
            row = []
            for i in range(len(self.matrix)):
                row.append(self.matrix[i][j])
            transposed.append(row)
        return Matrix(transposed)


# Создание матриц
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])

# Вывод на печать
print(matrix1)

# Сравнение матриц
print(matrix1 == matrix2)  # False
print(matrix1 == Matrix([[1, 2, 3], [4, 5, 6]]))  # True

# Сложение матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Умножение матриц (транспонирование)
transposed_matrix = matrix3.transpose()
print(transposed_matrix)
