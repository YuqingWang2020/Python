class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for i,char in enumerate(s):
            if char not in dic:
                stack.append(char)
            else:
                if not stack or dic[char]!=stack[-1]:
                    return False
                stack.pop()
        return len(stack)==0


a = Solution()
print(a.isValid(["{[]}"]))