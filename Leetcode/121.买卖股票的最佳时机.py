#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ll = 0
        rr = 1
        self.res = 0
        while rr < len(prices):
            if prices[ll] >= prices[rr]:
                ll = rr
            else:
                self.res = max(prices[rr] - prices[ll], self.res)
            rr += 1
        return self.res

# @lc code=end

