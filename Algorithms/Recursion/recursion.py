nums = [1, 1, 2, 3, 4]

for i in range(0, len(nums)-1):
    if nums[i] == 1:
        nums.pop(i)
        nums = nums

print(nums)