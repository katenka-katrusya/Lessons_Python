# Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.

text1 = input("Введите первую строку = ")
text2 = input("Введите вторую строку = ")
count = 0
string = ""
subString = ""
if len(text1) > len(text2):
    string = text1
    subString = text2
else:
    string = text2
    subString = text1
print(string.count(subString))  