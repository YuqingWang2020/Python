"""
Y.Wang
Date: 30.10.2021
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        print(nums[:j])
        return j
a=Solution()
print(a.removeElement([3,2,2,3],3))