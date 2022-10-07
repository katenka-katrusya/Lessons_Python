# Работа со списком

import random

myList = []
def fillArray(list):
    list.clear()
    for i in range(10):
        list.append(random.randint(-10, 10))
    return list

print(myList)
fillArray(myList)
print(myList)


def getArray():
    myList = []
    for i in range(10):
        myList.append(random.randint(-10, 10))
    return myList

newList = getArray()
print(newList)