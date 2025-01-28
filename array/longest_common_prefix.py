#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"


class Solution(object):
    def longestCommonPrefix(self, strs):

        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

