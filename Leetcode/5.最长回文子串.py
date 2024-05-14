#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def itrr(self, i, j, s):
        while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1 : j]

    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        for i in range(len(s)):
            temp = self.itrr(i, i, s)
            if len(temp) > len(self.res):
                self.res = temp
            temp = self.itrr(i, i + 1, s)
            if len(temp) > len(self.res):
                self.res = temp
        return self.res


# @lc code=end
