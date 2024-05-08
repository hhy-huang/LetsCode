#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertChild(self, root):
        if root.left:
            self.invertChild(root.left)
        if root.right:
            self.invertChild(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root.left:
            self.invertChild(root.left)
        if root.right:
            self.invertChild(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root
# @lc code=end