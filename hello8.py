#Дано натуральное число. Выведите его последнюю цифру. 
number1 = int(input("Input Number: "))
print(f"Остання цифра: {number1 % 10}")
#Дано положительное действительное число X. Выведите его дробную часть. 
from math import *
number1 = float(input("Input Number: "))
if number1 - int(number1) > 0: # Якщо саме мінус ціла його частина більше за нуль
    print(f"Дробна частина: {round(number1 - int(number1), 2)}")
else:
    print(f"Дробна частина: 0")
