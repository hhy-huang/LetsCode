#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        self.res = 1
        farr_list = [-1] * 10**5 
        flagg = -1
        for i, item in enumerate(nums):
            farr_list[i] = i + item
            if farr_list[i] >= len(nums) - 1 and flagg == -1:
                flagg = i
        while flagg != 0:
            for i in range(flagg):
                if farr_list[i] >= flagg:
                    flagg = i
                    self.res += 1
                    break
        return self.res
        
# @lc code=end

