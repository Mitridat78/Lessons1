#name = input("You name: ")
#print(f"Hello, {name}!")
number1 = int(input("Кількість учнів: "))
#print(f"The next number for the number {number} is {number + 1}")
#print(f"The previous number for the number {number} is {number - 1}")
number2 = int(input("Кількість учнів 2: "))
number3 = int(input("Кількість учнів 3: "))
# по 2 учня за партою, ціла частина + залишок
print(f"Кількість парт для всіх класів: {(number1 + number2 + number3) // 2 + (number1 + number2 + number3) % 2}")
