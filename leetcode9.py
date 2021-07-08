"""
Palindrome Number
Y.Wang
Date: 08.07.2021
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


a = Solution()
print(a.isPalindrome(121))
