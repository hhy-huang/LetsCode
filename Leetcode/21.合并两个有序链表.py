#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        p1 = list1
        p2 = list2
        list3 = None
        if p1.val > p2.val:
            list3 = p2
            p2 = p2.next
        else:
            list3 = p1
            p1 = p1.next
        while p1 and p2:
            if p1.val > p2.val:
                list3.next = p2
                list3 = list3.next
                p2 = p2.next
            else:
                list3.next = p1
                list3 = list3.next
                p1 = p1.next
        if p1:
            while p1:
                list3.next = p1
                list3 = list3.next
                p1 = p1.next
        else:
            while p2:
                list3.next = p2
                list3 = list3.next
                p2 = p2.next
        if list1.val > list2.val:
            return list2
        else:
            return list1

            

# @lc code=end

