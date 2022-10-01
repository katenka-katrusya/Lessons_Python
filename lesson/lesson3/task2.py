# Напишите программу, которая определит позицию второго вхождения строки в списке лтбо сообщит об её отсутствии

list = ["qwe", "asd", "zxc", "qwe", "ertyu"]
count = 0
findWord = "qwe"

for i in range(len(list)):
    if list[i] == findWord:
        count += 1
        if count == 2:
            print(i)
            break
else:
    print("Error")