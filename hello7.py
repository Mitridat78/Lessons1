number1 = int(input("number 1: "))
number2 = int(input("number 2: "))
number3 = int(input("number 3: "))
if number1 == number2 == number3:
    print("Співпадають всі 3 числа")
elif (number1 == number2 != number3) or (number1 != number2 == number3) or (number1 == number3 != number2):
    print("Співпадають 2 числа")  
else:
    print("Жодного співпадіння")
