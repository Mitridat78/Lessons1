"""
Определите среднее значение всех элементов 
последовательности, завершающейся числом 0. 
В этой и во всех следующих задачах 
числа, следующие за первым нулем, учитывать не нужно. 
"""

n = int(input("Введіть кількість чисел: "))

j = 1
sum = 0
i = 0
k = 0

while j <= n:
    n1 = int(input(f"Введіть {j} число: "))
    j += 1
    if n1 != 0 and i == 0 : # якщо число не нуль і це перший випадок (перший нуль)
        sum += n1 # сума не нульових елементів
        k += 1 # кількість не нульових елементів
    else:
        i += 1 # рахуємо всі інші нулі в послідовності
print(sum / k)