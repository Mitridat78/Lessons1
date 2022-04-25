number1 = int(input("First number: "))
number2 = int(input("Second number: "))
if number1 > number2:
    print(f"Max: {number1} Min: {number2}")
elif number1 < number2:
    print (f"Max: {number2} Min: {number1}")
else:
    print(f"{number1} = {number2}")
if number1 > 0:
    print(f"sign(x) = 1")
elif number1 < 0:
    print(f"sign(x) = -1")
else:
    print(f"sign(x) = 0")