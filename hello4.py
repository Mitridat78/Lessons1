number1 = int(input("Input Number: "))
if (number1 % 4 == 0 and number1 % 100 > 0) or number1 % 400 == 0:
    print("YES")
else:
    print("NO")
