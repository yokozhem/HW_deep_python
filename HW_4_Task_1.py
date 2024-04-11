"""
1. Напишите функцию для транспонирования матрицы
"""

def transpose(matrix):
    """
    Функция для транспонирования матрицы.

    Аргументы:
    matrix (list[list]): Матрица, представленная в виде списка списков.

    Возвращает:
    list[list]: Транспонированная матрица.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Пример использования функции
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose(matrix)
print("Исходная матрица:")
for row in matrix:
    print(row)
print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
