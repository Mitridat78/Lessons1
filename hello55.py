"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя
"""

def power(a, n):
    res = 1
    if n > 0:
        for i in range(n):
            res = res * a
        return res
    elif n < 0:
        for i in range(-n):
            res = res * a
        return 1 / res
    else:
        return 1

a = float(input("a = "))
n = int(input("n = "))
print(power(a, n))


        
        