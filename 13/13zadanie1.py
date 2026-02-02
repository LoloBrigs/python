import random


def generate_matrix(rows, cols, min_value=-200, max_value=200):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)
    return matrix


def add_matrices(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Ошибка: матрицы должны быть одинаковой размерности!")
        return None

    rows = len(matrix_1)
    cols = len(matrix_1[0])

    matrix_3 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        matrix_3.append(row)

    return matrix_3


def print_matrix(matrix, name="Матрица"):
    print(f"\n{name}:")
    print("[", end="")
    for i, row in enumerate(matrix):
        if i > 0:
            print(" ", end="")
        print(row, end="")
        if i < len(matrix) - 1:
            print(",")
        else:
            print("]")


if __name__ == "__main__":
    print("=== Задание №1: Генерация и сложение матриц ===\n")

    print("Часть 1: Проверка на примере из задания")
    print("-" * 50)

    matrix_1 = [[0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
                [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
                [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
                [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
                [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
                [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
                [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
                [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
                [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
                [43, 111, 38, 149, 5, 112, 79, 53, 15, 92]]

    matrix_2 = [[0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
                [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
                [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
                [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
                [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
                [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
                [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
                [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
                [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
                [32, -67, -75, -92, 15, -163, 18, 31, -162, -16]]

    print_matrix(matrix_1, "Матрица 1 (из задания)")
    print_matrix(matrix_2, "Матрица 2 (из задания)")

    matrix_3 = add_matrices(matrix_1, matrix_2)
    print_matrix(matrix_3, "Матрица 3 (сумма)")

    print("\n\nЧасть 2: Генерация случайных матриц 10x10")
    print("-" * 50)

    random_matrix_1 = generate_matrix(10, 10)
    random_matrix_2 = generate_matrix(10, 10)

    print_matrix(random_matrix_1, "Случайная матрица 1 (10x10)")
    print_matrix(random_matrix_2, "Случайная матрица 2 (10x10)")

    random_matrix_3 = add_matrices(random_matrix_1, random_matrix_2)
    print_matrix(random_matrix_3, "Сумма случайных матриц (10x10)")

    print("\n\nЧасть 3: Пример с матрицами 4x3")
    print("-" * 50)

    matrix_a = generate_matrix(4, 3)
    matrix_b = generate_matrix(4, 3)

    print_matrix(matrix_a, "Матрица A (4x3)")
    print_matrix(matrix_b, "Матрица B (4x3)")

    matrix_c = add_matrices(matrix_a, matrix_b)
    print_matrix(matrix_c, "Матрица C (сумма 4x3)")

    print("\n\n=== Программа завершена ===")
