#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        temp2 = head.next
        head.next = head.next.next
        temp2.next = head
        head = temp2

        temp = head
        curnum = 1
        lasttemp = head.next
        while temp.next:
            if curnum == 1 or curnum == 2:
                temp = temp.next
                curnum += 1
                continue
            if curnum % 2 == 1:
                curtemp = temp.next
                temp.next = temp.next.next
                curtemp.next = temp
                lasttemp.next = curtemp
                
                lasttemp = curtemp.next
                temp = curtemp
                temp = temp.next
                curnum += 1
            elif curnum % 2 == 0:
                temp = temp.next
                curnum += 1
        return head    

# @lc code=end

