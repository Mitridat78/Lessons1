"""
Дано целое число, не меньшее 2. Выведите его 
наименьший натуральный делитель, отличный от 1.
"""
n = int(input("Input number: "))

i = 2 #делитель отличный от 1
while n % i != 0:
    i += 1
print(i)
