#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.res = []
        prelist = []
        latlist = []
        temp = 1
        for item in nums:
            temp = temp * item
            prelist.append(temp)
        temp = 1
        for item in reversed(nums):
            temp = temp * item
            latlist.append(temp)
        for i in range(len(nums)):
            if i == 0:
                self.res.append(latlist[-2])
            elif i == len(nums) - 1:
                self.res.append(prelist[-2])
            else:
                self.res.append(prelist[i - 1] * latlist[(len(nums) - (i + 1)) - 1])
        return self.res
# @lc code=end