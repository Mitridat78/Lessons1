#Шахматный король ходит по горизонтали, вертикали и диагонали, 
#но только на 1 клетку. Даны две различные клетки шахматной доски, 
#определите, может ли король попасть с первой клетки на вторую одним 
#ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
#задающие номер столбца и номер строки сначала для первой клетки, 
#потом для второй клетки. Программа должна вывести 
#YES, если из первой клетки ходом короля можно попасть во 
#вторую или NO в противном случае. 
line1 = int(input("line 1: "))
column1 = int(input("column 1: "))
line2 = int(input("line 2: " ))
column2 = int(input("column 2: "))
if (line2 == line1 + 1) or (line2 == line1 - 1) or (column2 == column1 + 1) or (column2 == column1 - 1):
    print("YES")
else:
    print("NO")