"""
Выведите все четные элементы списка. При этом используйте цикл for, 
перебирающий элементы списка, а не их индексы! 
"""
# більш короткий варіант рішення дивись у файлі hello41.py
a = []
n = int(input("Введіть кількість елементів списку: "))

for i in range(n):
    elem = int(input(f"Введіть {i} елемент списку: "))
    # додаємо елементи до списку
    a.append(elem)
for elem in a: # перебираємо елементи списку
    if elem % 2 == 0:
        print(elem)
# другий спосіб
for i in range(n): # а тут перебираємо індекси
    if a[i] % 2 == 0:
        print(a[i])