"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве 
столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем 
элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j)
"""

def swap_columns(a, i, j):
    for i in range(n):
        for j in range(m):
            if j == column1:
                a[i][column1], a[i][column2] = a[i][column2], a[i][column1]


n = int(input("Введіть кількість строк (n): "))
m = int(input("Введіть кількість стовбців (m): "))
a = [[int(j) for j in input().split()] for i in range(n)]
column1 = int(input())
column2 = int(input())
"""
for i in range(n):
    for j in range(m):
        if j == column1:
            a[i][column1], a[i][column2] = a[i][column2], a[i][column1]
"""
for line in a:
    print(' '.join(str(elem) for elem in line))