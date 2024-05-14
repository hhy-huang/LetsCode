#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def binarySearch(self, lline, target):
        l = 0
        r = len(lline) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if target < lline[mid]:
                r = mid - 1
            elif target > lline[mid]:
                l = mid + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lline = []
        for item in matrix:
            lline += item
        return self.binarySearch(lline, target)
        

# @lc code=end

