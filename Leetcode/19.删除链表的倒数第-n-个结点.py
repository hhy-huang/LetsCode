#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        lenl = 0
        while temp:
            temp = temp.next
            lenl += 1
        if n == lenl:
            return head.next
        temp = head
        curnum = 0
        while temp:
            curnum += 1
            if curnum == (lenl - n):
                curtemp = temp
            if curnum == (lenl - n) + 1:
                curtemp.next = temp.next
                break
            temp = temp.next
        return head
                
# @lc code=end

