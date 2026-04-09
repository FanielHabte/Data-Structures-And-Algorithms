"""
Question: Add a number to the end of a list
"""

"""
Algorithm Summary:
1. Take the list and add a place holder 
2. and then add the number to length of the original list
"""


def addToList(numbersList: list, addNumber: int) -> list:
    newNumberList = numbersList + [0]
    newNumberList[len(numbersList)] = addNumber

    return newNumberList


numbersList = [1, 2, 3, 4]
newNumberList = addToList(numbersList, 5)

print("Old list: ", numbersList)
print("New list: ", newNumberList)
