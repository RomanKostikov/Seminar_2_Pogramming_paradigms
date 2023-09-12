# След матрицы: процедурный
# ● Контекст
# След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
# (количество столбцов = количеству строк).
# ● Задача
# Добавить процедурную парадигму в имеющуюся реализацию вычисления следа.
def matrix_mark(m):
    result = 0
    for i in range(len(m)):
        result += m[i][i]
    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(matrix_mark(m))


if __name__ == "__main__":
    main()