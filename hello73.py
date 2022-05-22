"""
Вам дан словарь, состоящий из пар слов. Каждое слово является 
синонимом к парному ему слову. Все слова в словаре различны.
Для слова из словаря, записанного в последней строке, определите 
его синоним.
"""
num = int(input("Input number: "))
a = {}

for i in range(num):
    para = input().split()
    a[para[0]] = para[1]

slovo  = input("Input word: ")
for key, val in a.items():
    if slovo == key:
        print(val)
    elif slovo == val:
        print(key)

