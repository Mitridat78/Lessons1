# По данному натуральному n вычислите сумму 1^+2^3+3^3+...+n^3.
n = int(input("Input n = "))

sum = 0
for i in range(n + 1):
    sum += i ** 3
print(sum)




