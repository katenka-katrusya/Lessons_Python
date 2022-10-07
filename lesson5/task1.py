import random


listInt = list([i for i in range(10)])
random.shuffle(listInt)

print(listInt)

distance = []
new = []

for i in range(0, (len(listInt)-1)):
    sub = []
    sub.append(listInt[i])
    while True:

        if listInt[i] < listInt[i+1]:
            sub.append(listInt[i+ 1])
            i += 1
        else:
            break
    distance.append(sub)

for i in range(len(distance)):
    if len(distance[i]) != 1:
        new.append(distance[i])

print(new)