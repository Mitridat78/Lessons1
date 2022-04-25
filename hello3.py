line1 = int(input("line 1: "))
column1 = int(input("column 1: "))
line2 = int(input("line 2: " ))
column2 = int(input("column 2: "))
if (line1 + column1) % 2 == 0 and (line2 + column2) % 2 == 0:
    print("YES")
elif (line1 + column1) % 2 > 0 and (line2 + column2) % 2 > 0:
    print("YES")
else:
    print("NO")
