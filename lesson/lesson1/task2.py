# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a = int(input("1 число: "))
# b = int(input("2 число: "))
# c = int(input("3 число: "))
# d = int(input("4 число: "))
# e = int(input("5 число: "))
# max = a
# if b > max: max = b
# if c > max: max = c
# if d > max: max = d
# if e > max: max = e
# print("Максимальное число = ", max)

# 2 способ:
# list = [- 1, 4, 8, 7, 5]
# print(list)
# print(max(list))

# 3 способ:
# list = []
# for i in range(5):
#     list.append(int(input("Введите число: ")))

# max = list[0]
# for i in list:
#     if i > max: max = i
# print("Максимальное число = ", max)

# 4 способ:
list = []
for i in range(5):
    list.append(int(input(f"Введите {i+1} число: ")))
max = min = list[0]
for k in range(5):
    if list[k] > max: max = list[k]
    if list[k] < min: min = list[k]
print("Минимальное число = ", min)
print("Максимальное число = ", max)