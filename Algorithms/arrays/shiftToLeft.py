"""
Question:
Shift number one to the left
"""

"""
Algorithm Summary:
1. Save the first value, iterate through n-1 and pull each element one slot left by copying from the right,
then place the saved value at the end.
"""

nums = [1, 2, 3, 4, 5]

def shiftToLeft(numbersList :list):
    "Optional you can create a copy of the array to preserve the original list using [:]"
    numbersListCopy = numbersList[:]
    firstValue = numbersListCopy[0]
    for i in range(0, len(numbersListCopy) - 1):
        numbersListCopy[i] = numbersListCopy[i + 1]
    numbersListCopy[-1] = firstValue
    
    return numbersList, numbersListCopy


print(shiftToLeft(nums))