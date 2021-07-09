"""
Reverse Integer
Y.Wang
Date: 08.07.2021
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = -2 ** 31
        max = 2 ** 31 - 1
        op = 1
        if x < 0:
            s = str(x)[1:]
            op = -1
        else:
            s = str(x)[::-1]
        res = op * int(s)
        return res if min <= res <= max else 0


a = Solution()
print(a.reverse(123))
