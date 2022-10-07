# Считайте из файла список чисел. Напишите программу, которая покажет большее и меньшее число, в качестве разделителя 
# используйте пробел. Запишите результат в другой файл.

pathRead = r'HelloPython\lesson4\file.txt'
pathWrite = r'HelloPython\lesson4\file2.txt'

try:
    with open(pathRead, 'r') as data:
        file = data.read().split(' ')
except:
    print("Файл не найден")

print(file)

for i in range(len(file)):
    if file[i].isdigit():
        file[i] = int(file[i])
print(file)
print(min(file))
print(max(file))

data = open(pathWrite, 'w')
data.write(f"{min(file)} \n")
data.write(f"{max(file)} \n")
data.close()



# ещё
try:
    with open(pathRead, 'r') as data:
        file = data.read().split(' ')
except:
    print("Файл не найден")

listInt = []
print(file)

for elem in file:
    if elem.isdigit():
        listInt.append(int(elem))

print(min(listInt))
print(max(listInt))

try:
    with open(pathWrite, 'w') as data:
        data.write(str(min(listInt)))
        data.write('\n')
        data.write(str(max(listInt)))
except:
    print("Ошибка работы с файлом")