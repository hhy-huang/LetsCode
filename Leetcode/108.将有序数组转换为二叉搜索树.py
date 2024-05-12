#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        midd = len(nums) // 2
        root = TreeNode(nums[midd])
        root.left = self.sortedArrayToBST(nums[:midd])
        root.right = self.sortedArrayToBST(nums[midd+1:])

        return root
# @lc code=end

