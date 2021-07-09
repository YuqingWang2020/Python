"""
Roman to Integer
Y.Wang
Date: 08.07.2021
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        stack=[]
        res=0
        for index,item in enumerate(s):
            res += mapping[item]
            if item=="V"or item=="X":
                if stack and stack[-1]=="I":
                    res-=2
            elif item == "L"or item == "C":
                if stack and stack[-1] == "X":
                     res-=20
            elif item == "D" or item == "M":
                if stack and stack[-1] == "C":
                    res-=200
            stack.append(item)
        return res

a = Solution()
print(a.romanToInt("III"))