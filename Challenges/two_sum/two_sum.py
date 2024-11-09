from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()

# example
nums = [2, 7, 11, 15]
target = 22
result = solution.twoSum(nums, target)

print(result)
