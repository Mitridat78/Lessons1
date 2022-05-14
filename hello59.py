"""
Напишите функцию fib(n), которая по данному целому 
неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию
"""

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

n = int(input("n= "))
print(fib(n))

