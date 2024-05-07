#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def itera(self, root):
        global res
        if not root:
            return res
        if root.left:
            self.itera(root.left)
        res.append(root.val)
        if root.right:
            self.itera(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global res
        res = []
        if not root:
            return res
        if root.left:
            self.itera(root.left)
        res.append(root.val)
        if root.right:
            self.itera(root.right)
        return res

# @lc code=end

