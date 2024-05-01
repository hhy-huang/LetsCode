#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def reverse(self, nums, i ,j):
        ll = i
        rr = j
        while ll < rr:
            temp = nums[ll]
            nums[ll] = nums[rr]
            nums[rr] = temp
            ll += 1
            rr -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        """for i in range(k):
            temp = nums[-1]
            temp1 = nums[0]
            for j in range(len(nums) - 1):
                temp2 = nums[j + 1]
                nums[j + 1] = temp1
                temp1 = temp2
            nums[0] = temp"""
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
# @lc code=end

