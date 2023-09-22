nums = [2, 43, 12, 7, 3]
target = 9

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

        
