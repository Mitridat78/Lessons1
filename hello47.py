"""
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.
"""

a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]
j = 0

for i in range(len(a)-1):
    if a[i] != a[i + 1]:
        j += 1
if j == len(a) + 1:
    print(j + 2)
else:
    print(j + 1)