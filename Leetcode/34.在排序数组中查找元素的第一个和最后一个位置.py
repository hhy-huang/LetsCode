#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            midd = int((l + r) / 2)
            if target < nums[midd]:
                r = midd - 1
            elif target > nums[midd]:
                l = midd + 1
            else:
                return midd
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = self.binarySearch(nums, target)
        if pos == -1:
            return [-1, -1]
        minn = pos
        maxx = pos
        for i in range(pos + 1, len(nums)):
            if nums[i] == target:
                maxx = max(maxx, i)
            else:
                break
        for i in range(pos, -1, -1):
            if nums[i] == target:
                minn = min(minn, i)
            else:
                break
        return [minn, maxx]

        
# @lc code=end

