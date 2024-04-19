"""
link:   https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
Author: hhy
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num0 = 0
        for item in nums:
            if item == 0:
                num0 += 1
        for i in range(num0):
            nums.remove(0)

        nums += [0] * num0
