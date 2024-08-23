nums = [2, 43, 12, 7, 3]
target = 9

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# time complexity: O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums):
            if target - num in my_dict:
                return [i, my_dict[target - num]]
            my_dict[num] = i

# time cmplexity: O(n) - Linear time
