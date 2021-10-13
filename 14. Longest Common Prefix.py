"""
Longest Common Prefix
Y.Wang
Date: 08.07.2021
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_l=len(strs[0])
        for word in strs:
            min_l=min(min_l,len(word))
        common=strs[0][:min_l]

        for index,item in enumerate(strs):
            i=0

            while (i < min_l and item[i] == common[i]):
                i += 1

            min_l = min(min_l, i)
            common = common[:min_l]

        return common



a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))