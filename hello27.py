"""
Дана строка, в которой буква h встречается 
минимум два раза. Удалите из этой строки первое 
и последнее вхождение буквы h, а также все символы, 
находящиеся между ними.
"""
s = str(input("Input string: "))
s1 = s[s.find('h'):s.rfind('h') + 1] # знаходимо перше та останнє входження
s = s.replace(s1,'') #замінюємо (видаляємо) все між символами h
print(s)