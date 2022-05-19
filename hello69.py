"""
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если 
это число ранее встречалось в последовательности или NO, если 
не встречалось..
"""

numbers = [int(i) for i in input().split()]
"""entered = list()
for elem in numbers:
    if elem in entered:
        print("YES")
    else:
        entered.append(elem)
        print("NO")
"""
for i in range(len(numbers)):
    if numbers[i+1] in numbers[0:i-1]:
        print("yes")