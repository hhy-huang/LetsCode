"""
link:   https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=bytedance-2023-spring-sprint
author: hhy
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 双指针
        left = 0
        right = 1
        res = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                res = max(prices[right] - prices[left], res)
            right += 1
        return res
        