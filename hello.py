# print("Hello Word!")
# name = input("You name? ")
# print(f"Hi, {name}")
import sys

try:
    minute = int(input("Minute (N): "))
#    number2 = int(input ("Яблук (K): "))
except ValueError:
    print("Помилка!!!")
    sys.exit(1)

print(f"Min: {minute % 60} Hour: {minute // 60}")
#print(f"Залишилось: {number2 % number1}")
#print(f"Result: {number1 + number2}")