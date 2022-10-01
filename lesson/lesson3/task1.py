# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

# list = ["fkcdje2", "hello3", "d22", "122"]

# trigger = False

# for i in range(len(list)):
#     if list[i].find("3") >= 0:
#         trigger = True
#         break
# if trigger:
#     print(f"Число присутствует")
# else:
#     print(f"Число отсутствует")


# 2 способ
# list = ["fkcdje2", "hello3", "d22", "122"]
# num = input("Введите число: ")

# for element in list:
#     if num in element:
#         print("Присутствует")


# 3 способ
# list = ["fkcdje2", "hello3", "d22", "122"]
# num = input("Введите число: ")

# for element in list:
#     for el in element:
#         if num == el:
#             print("Присутствует")
#             break


# ещё
list = ["fkcdje2", "hello3", "d22", "122"]
num = input("Введите число: ")

for element in list:
    if num in element:
        print("Присутствует")
        break
else:
    print("Отсутствует")