"""
link:   https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
Author: hhy
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        self.res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                lengthh = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    lengthh += 1
                self.res = max(self.res, lengthh)

        return self.res
