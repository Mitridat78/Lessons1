"""
В списке все элементы различны. Поменяйте местами 
минимальный и максимальный элемент этого списка.
"""
a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]

for elem in a:
    max1 = max(a)
    min1 = min(a)

for i in range(len(a)):
    if a[i] == max1:
        a[i] = min1
    elif a[i] == min1:
        a[i] = max1
print(a[::])
# короткий варіант
for i in range(len(a)):
    a[a.index(max(a))], a[a.index(min(a))] = min(a), max(a)
print(a, sep = ', ')