"""
Link:       https://leetcode.cn/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-100-liked
Author:     Hhy
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        sett = set()
        p = head
        while p:
            if p in sett:
                return True
            sett.add(p)
            p = p.next
        return False
