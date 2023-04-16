"""
Task 1
Напишите функцию для транспонирования матрицы.
"""


def matrix_transposition(data: list[list[int]]) -> list[list[int]]:
    trans_matrix = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return trans_matrix


matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print(matrix_transposition(matrix))
