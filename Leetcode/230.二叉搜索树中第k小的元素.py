#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, output):
        if not root:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        self.inorder(root, output)
        return output[k - 1]
# @lc code=end

