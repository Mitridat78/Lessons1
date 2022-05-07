"""
Выведите все четные элементы списка. При этом используйте цикл for, 
перебирающий элементы списка, а не их индексы! 
"""
# нижче короткий варіант рішення з використанням генераторів, 
# більш довгий, але зрузумілий варіант рішення дивись у файлі hello40.py

a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]
for elem in a:
    if elem % 2 == 0:
        print(elem)
