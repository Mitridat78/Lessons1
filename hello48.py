"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). 
Если элементов нечетное число, то последний элемент остается на своем месте
"""
a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]

for i in range(0, len(a)-1, 2):
    a[i], a[i+1] = a[i+1], a[i]
    
print(a[::])

