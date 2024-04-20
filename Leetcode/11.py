"""
link:   https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked
Author: hhy
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """ # TLE
        self.res = 0
        for i, h in enumerate(height):
            for j in range(i + 1, len(height)):
                v = min(height[i], height[j]) * (j - i)
                self.res = max(self.res, v)
        return self.res
        """

        self.res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            v0 = (j - i) * min(height[i], height[j])
            self.res = max(self.res, v0)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return self.res
