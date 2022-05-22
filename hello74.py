"""
Вам дан словарь, состоящий из пар слов. Каждое слово является 
синонимом к парному ему слову. Все слова в словаре различны.
Для слова из словаря, записанного в последней строке, определите 
его синоним.
"""
num = int(input("Input number: "))
a = {}

for i in range(num):
    (president, points) = input().split()
    if president not in a:
        a[president] = int(points)
    else:
        a[president] += int(points)
for president in sorted(a):
    print(president, a[president])


