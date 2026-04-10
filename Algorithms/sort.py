arr = [2, 4, 5, 3, 1, 2]

maxValue = arr[-1]
for i in range(len(arr)-2, -1, - 1):
    print("Index Value:", i, "\nCurrent number:", arr[i], "\nMax Value:", maxValue,"\n")
    maxValue = max(maxValue, arr[i + 1])
    
    
arr[-1] = -1

