#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farr = 0
        for i, item in enumerate(nums):
            if i > farr:
                return False
            farr = max(farr, i + item)
        return True
# @lc code=end

