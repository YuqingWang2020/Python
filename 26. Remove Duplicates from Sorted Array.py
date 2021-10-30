"""
Y.Wang
Date: 30.10.2021
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(0, len(nums)):
            if i < 1 or (i>0 and nums[i] != nums[i - 1]):
                nums[j] = nums[i]
                j += 1
        print(nums[:j])
        return j


a=Solution()
print(a.removeDuplicates([1,1,2]))
