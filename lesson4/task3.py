# Найдите корни квадратного уравнения

import math

pathRead = r'HelloPython\lesson4\file3.txt'
pathWrite = r'HelloPython\lesson4\file4.txt'

try:
    with open(pathRead, 'r') as data:
        file = data.read().split(' ')
except:
    print("Файл не найден")

print(file)
coef = []

for elem in file:
    if elem[0].isdigit():
        coef.append(elem[0])

print(coef)

a = int(coef[0])
b = int(coef[1])
c = int(coef[2])

result = ''

discr = b**2 - 4*a*c
print(discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    result = f"x1 = {x1}\nx2 = {x2}"
elif discr == 0:
    x = -b / (2 * a)
    result = f"x1 = x2 = {x}"
else:
    result = "Корней нет"

try:
    with open(pathWrite, 'w') as data:
        file = data.write(result)
except:
    print("Ошибка работы с файлом")
