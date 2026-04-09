nums = [1, 1, 0, 1, 1, 1]

count = 0
position = 0
for i in range(0, len(nums)):
    if count == 0 and nums[i] == 1:
        count+=1
        position = i
        
print(count)
print(position)