#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """listlist = []
        p = head
        while p:
            if p in listlist:
                return p
            listlist.append(p)
            p = p.next
        return None"""
        slowp = fastp = head
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if slowp == fastp:
                break
        if not (fastp and fastp.next):
            return None
        while head != slowp:
            head = head.next
            slowp = slowp.next
        return head
# @lc code=end