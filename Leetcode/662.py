"""
link:       https://leetcode.cn/problems/maximum-width-of-binary-tree/description/?envType=study-plan-v2&envId=bytedance-2023-spring-sprint
author:     hhy
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])      # 使用双端队列存储当前层的节点
        index_queue = deque([1])   # 使用双端队列存储当前层的节点索引值

        max_width = 0

        while queue:
            size = len(queue)      # 当前层的节点个数
            left = index_queue[0]  # 当前层最左边节点的索引值
            right = left           # 设定当前层最右边节点的索引值为left

            for _ in range(size):  # 遍历当前层的节点
                node = queue.popleft()
                right = index_queue.popleft()  # 获取右节点位置（当前节点位置）

                if node.left:      # 如果当前节点有左子节点
                    queue.append(node.left)                        # 将左子节点加入队列
                    index_queue.append(right * 2)                  # 计算左子节点的索引值，加入索引队列
                if node.right:     # 如果当前节点有右子节点
                    queue.append(node.right)                       # 将右子节点加入队列
                    index_queue.append(right * 2 + 1)              # 计算右子节点的索引值，加入索引队列

            max_width = max(max_width, right - left + 1)

        return max_width