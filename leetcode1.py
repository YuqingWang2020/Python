"""
Two Sum
Y.Wang
Date: 08.07.2021
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        for index, item in enumerate(nums):
            for count in range(index + 1, len(nums)):
                if nums[count] + nums[index] == target:
                    return [index, count]


a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
