"""
Дан список целых чисел, число k и значение C. Необходимо вставить 
в список на позицию с индексом k элемент, равный C, сдвинув все 
элементы, имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, 
используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого 
при выводе и не создавая дополнительного списка.  
"""
a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]
k = int(input("k = "))
c = int(input("c = "))

a.append(c)
print(a, sep = ', ')

for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = c
print(a, sep = ', ')