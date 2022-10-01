# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

num = int(input("Введите число N: "))

result = []
for degree in range(num):   # num+1, если включительно последнее чило
    result.append(str((-3)**degree))

print(", ".join(result), end=".")

# 2 способ
num = int(input("Введите число N: "))

for i in range(num):
    print((-3)**i, end=" ")
