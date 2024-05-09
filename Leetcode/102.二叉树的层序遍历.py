#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        curls = []
        
        curls.append(root)
        while curls:
            temp = []
            temp2 = []
            for item in curls:
                temp.append(item.val)
                if item.left:
                    temp2.append(item.left)
                if item.right:
                    temp2.append(item.right)
            curls = temp2
            self.res.append(temp)
        return self.res


# @lc code=end