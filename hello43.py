"""
Дан список чисел. Если в нем есть два соседних элемента 
одного знака, выведите эти числа. Если соседних элементов одного 
знака нет — не выводите ничего. Если таких пар соседей 
несколько — выведите первую пару
"""
k = 0
k1 = 0
a = [int(input(f"Введіть {i} елемент списку: ")) for i in range(int(input("Введіть кількість елементів списку: ")))]
for i in range(0, len(a)): # перший (довгий) спосіб
    if a[i] > 0 and a[i + 1] > 0 and k == 0:
        k += 1
        if k >= 1:
            print(a[i], a[i + 1])
            break
    elif a[i] < 0 and a[i + 1] < 0 and k1 == 0:
        k1 += 1
        if k1 >= 1:
            print(a[i], a[i + 1])
            break
    else:
        print("Пари не виявлено!")
        break
for i in range(0, len(a)): # другий спосіб (корооткий)
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
        break
      
