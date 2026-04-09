"""
Question:
Delete a number at i'th place and then Shift numbers to the right 
of the number ons step to left.
"""

"""
Algorithm Summary:
1. Iterate starting from the index until the end of the list 
2. Assign the number with their right neighbor
3. Replace the last value with 0
4. Return the list
"""

nums = [1, 2, 3, 4, 5]
index = 0

def removeShift(index: int, numbersList: list):
    for i in range(index, len(numbersList)-1):
        numbersList[i] = numbersList[i+1]
    numbersList[-1] = 0
    
    return numbersList

print(removeShift(index, nums))
    