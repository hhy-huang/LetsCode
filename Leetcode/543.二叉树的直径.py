#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        global res
        global mem
        if not root:
            return 0
        if root in mem:
            depth = mem[root]
        else:
            depth = max(self.depth(root.left), self.depth(root.right)) + 1
            mem[root] = depth
        return depth
    
    def everynode(self, root):
        global res
        global mem

        left = self.depth(root.left)
        right = self.depth(root.right)
        diameter = left + right
        mem[root] = diameter
        res = max(res, diameter)

        if left < right:
            if root.right:
                self.everynode(root.right)
        else:
            if root.left:
                self.everynode(root.left)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global res
        global mem
        mem = {}
        res = 0

        if not root:
            return 0

        self.everynode(root)

        return res


# @lc code=end

