# Дано N чисел: сначала вводится число N, затем вводится 
# ровно N целых чисел. Подсчитайте количество нулей среди 
# введенных чисел и выведите это количество. Вам нужно 
# подсчитать количество чисел, равных нулю, а не количество цифр.


n = int(input("Введіть кількість чисел: "))

zero = 0
for i in range(n):
    n1 = int(input(f"Введіть {i + 1} число: "))
    if n1 == 0:
        zero += 1
print(zero)
