#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        curSum = nums[0]
        self.res = nums[0]
        for item in nums[1:]:
            curSum = max(curSum + item, item)
            self.res = max(curSum, self.res)
        return self.res
# @lc code=end

