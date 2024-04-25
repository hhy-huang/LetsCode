#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.res = 0
        seen = {}
        l = 0
        for i, item in enumerate(s):
            if item not in seen:
                self.res = max(self.res, i + 1 - l)
            else:
                if seen[item] >= l:
                    l = seen[item] + 1
                else:
                    self.res = max(self.res, i + 1 - l)
            seen[item] = i
        return self.res
# @lc code=end

