"""
Question: Add a number at i'th place of the list
"""

"""
Algorithm Summary:
1. Create function that takes a list, index(position), number(literal to be places at index)
1. Created a new list by extending the original list by one 
2. Then iterate backwards starting from last value.
3. Assign the current value by the left neighbor
4. Place the new value at index
5. Return the newList
"""


def insertShift(numbersList: list, index: int, numberValue: int):
    newList = numbersList + [0]
    for i in range(len(newList) - 1, index, -1):
        newList[i] = newList[i - 1]
    newList[index] = numberValue

    return newList


numbers = [1, 2, 3, 4]
index = 2
replaceWith = 5

print(insertShift(numbers, index, replaceWith))
