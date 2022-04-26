# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
from math import *
number1 = float(input("Input Number: "))
if number1 - int(number1) > 0:
    print(f"{floor((number1 - int(number1)) * 10)}")
else:
     print(f"0")