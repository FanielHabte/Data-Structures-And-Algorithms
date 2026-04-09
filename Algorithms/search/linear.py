def linear_search(list: list, target: int):
    """ 
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i 
    return None 

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
result = linear_search(numbers, target)

verify(result)
