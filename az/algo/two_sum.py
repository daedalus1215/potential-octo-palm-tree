from typing import List


class Solution:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for count, num in enumerate(nums):
            if num in hash:
                return [hash[num], count]
            else:
                hash[target - num] = count
        return hash


print(Solution().twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
