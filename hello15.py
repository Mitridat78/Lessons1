# Дано 10 целых чисел. Вычислите их сумму. Напишите 
# программу, использующую наименьшее число переменных
# !!! ОБЪЕДИНИЛ РЕШЕНИЕ ДВУХ ЗАДАЧ В ОДНУ !!!!
# Дано несколько чисел. Вычислите их сумму. Сначала 
# вводите количество чисел N, затем вводится ровно N целых 
# чисел. Какое наименьшее число переменных нужно 
# для решения этой задачи?

number = int(input("Введіть кількість чисел: "))

sum = 0
for i in range(number):
    sum += int(input(f"Введіть {i+1} число: "))
print(f"Сума = {sum}")



