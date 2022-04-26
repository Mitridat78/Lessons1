# Даны два целых числа A и B (при этом A ≤ B). 
# Выведите все числа от A до B включительно. 
a = int(input("a: "))
b = int(input("b: "))
if a <= b:
    for i in range(a, b+1):
        print(i)
else:
    print("Помилка! a має бути <= b!")



