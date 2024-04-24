#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_0 = 0
        num_10 = 0
        cur = ListNode()
        dum = cur
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            num_0 = (l1.val + l2.val + num_10) % 10
            num_10 = (l1.val + l2.val + num_10) // 10
            cur.next = ListNode(val=num_0)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if num_10 != 0:
            cur.next = ListNode(val=num_10)
        return dum.next
# @lc code=end

