"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), 
вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре 
действительных числа и выведите результат работы этой функции. 
"""
from math import *


def distance(x1, y1, x2, y2):
    res = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if res - int(res) > 0: 
        return float(round(res, 5))
    else:
        return int(res)

x1 = float(input("Input x1: "))
y1 = float(input("Input y1: "))
x2 = float(input("Input x2: "))
y2 = float(input("Input y2: "))
print(distance(x1, y1, x2, y2))