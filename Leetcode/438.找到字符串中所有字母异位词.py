#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """self.res = []
        lenp = len(p)
        for i in range(len(s)):
            tempstr = s[i:i + lenp]
            tempstr = sorted(tempstr)
            if tempstr == sorted(p):
                self.res.append(i)
        return self.res"""
        cntp = Counter(p)
        cnttemp = Counter(s[:len(p) - 1])
        self.res = []
        for i in range(len(p) - 1, len(s)):
            cnttemp[s[i]] += 1
            if cnttemp == cntp:
                self.res.append(i - (len(p) - 1))
            cnttemp[s[i - (len(p) - 1)]] -= 1
            if cnttemp[s[i - (len(p) - 1)]] == 0:
                del cnttemp[s[i - (len(p) - 1)]]
        return self.res
# @lc code=end

