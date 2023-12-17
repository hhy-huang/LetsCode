"""
link:   https://leetcode.cn/problems/squares-of-a-sorted-array/?envType=study-plan-v2&envId=bytedance-2023-spring-sprint
author: hhy
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_2 = [x**2 for x in nums]
        nums_res = sorted(nums_2)
        return nums_res