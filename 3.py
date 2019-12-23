class Solution:
    def twoSum(self, nums, target: int):
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                if n + m == target:
                    return [i, j+i+1]