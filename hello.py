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

print(f"Min: {minute % 60} Hour: {minute % 1440 // 60}") # 1440 це кількість хвилин за добу = 24 * 60 (24 години * 60 хвилин)
#print(f"Залишилось: {number2 % number1}")
#print(f"Result: {number1 + number2}")