"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве 
столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем 
элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j)
"""

def swap_columns(a, i, j):
    for k in range(n):
        for k1 in range(m):
            if k1 == i:
                a[k][i], a[k][j] = a[k][j], a[k][i]


n = int(input("Введіть кількість строк (n): "))
m = int(input("Введіть кількість стовбців (m): "))
a = [[int(k1) for k1 in input().split()] for k in range(n)]
i = int(input())
j = int(input())

swap_columns(a, i, j)
for line in a:
    print(' '.join(str(elem) for elem in line))