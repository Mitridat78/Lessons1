"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите индекс наибольшего элемента последовательности. 
Если наибольших элементов несколько, выведите индекс первого из них. 
Нумерация элементов начинается с нуля. В этой и во всех следующих задачах 
числа, следующие за первым нулем, учитывать не нужно. 
"""

n = int(input("Введіть кількість чисел: "))

j = 1
max = 0
i = 0
k = 0

while j <= n:
    n1 = int(input(f"Введіть {j} число: "))
    j += 1
    if n1 != 0 and i == 0: # якщо число не нуль і це перший випадок (перший нуль)
        if n1 > max:
            max = n1
            k = j # індекс найбільшого елемента
    else:
        i += 1 # рахуємо всі інші нулі в послідовності
print(max, k - 1) # виводимо саме число та індекс
