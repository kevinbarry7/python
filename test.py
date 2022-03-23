from sys import argv

print("Today is Wednesday")


def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList


newList = [12, 35, 9, 56, 24]

print(swapList(newList))
print("today is not Thursday")

# this is a comment


