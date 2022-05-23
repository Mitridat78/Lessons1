
"""
Дан список стран и городов каждой страны. Затем даны названия городов. 
Для каждого города укажите, в какой стране он находится.
"""

num = int(input("Input number: "))
a = {}

for i in range(num):
    countries_and_city = input().split()
    a[countries_and_city[0]] = ''.join(countries_and_city[1:])
print(a)
m = int(input("m = "))
for i in range(m):
    city = input()
    for elem in a:
        if city in a[elem]:
            print(elem)


