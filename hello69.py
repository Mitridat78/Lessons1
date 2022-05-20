"""
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если 
это число ранее встречалось в последовательности или NO, если 
не встречалось..
"""

a = [int(i) for i in input().split()]
b = []
for elem in a:
    if elem in b:
        print("YES")
    else:
        b.append(elem)
        print("NO")
# другий спосіб
for i in range(len(a)):
    if a[i] in a[:i]:
        print("yes")
    else:
        print("no")