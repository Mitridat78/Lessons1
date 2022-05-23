"""
В файловую систему одного суперкомпьютера проник вирус, который сломал 
контроль за правами доступа к файлам. Для каждого файла известно, с 
какими действиями можно к нему обращаться:

    запись W,
    чтение R,
    запуск X. 

В первой строке содержится число N — количество файлов содержащихся в 
данной файловой системе. В следующих N строчках содержатся имена файлов 
и допустимых с ними операций, разделенные пробелами. Далее указано чиcло 
M — количество запросов к файлам. В последних M строках указан запрос вида 
Операция Файл. К одному и тому же файлу может быть применено любое колличество запросов.
Вам требуется восстановить контроль над правами доступа к файлам 
(ваша программа для каждого запроса должна будет возвращать OK если 
над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.
"""

num = int(input("Input number: "))
names_files = {}
access_files = {'write' : 'W', 'read' : 'R', 'execute' : 'X'}

for i in range(num):
    str = input().split() # ім'я файлу та права доступу
    names_files[str[0]] = ''.join(str[1:])
print(names_files)
m = int(input()) # кількість запитів до файлів
for i in range(m):
    (rights_access, n_file) = input().split() # доступ та ім'я файлу
    if access_files[rights_access] in names_files[n_file]:
        print("OK")
    else:
        print("Access denied")

