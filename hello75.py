"""
Дан текст: в первой строке задано число строк, далее идут 
сами строки. Выведите слово, которое в этом тексте встречается 
чаще всего. Если таких слов несколько, выведите то, которое 
меньше в лексикографическом порядке.
"""
num = int(input("Input number: "))
a = {}
word_count = 0

for i in range(num):
    str = input().split()
    for elem in str:
        a[elem] = a.get(elem, 0) + 1
        if a[elem] > word_count:
            word_count = a[elem]
print(a)
for word in a:
    if a[word] == word_count:
        print(word)

