"""
Link:       https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
Author:     Hhy
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        temp1 = head
        if head.next == None:
            return head
        temp2 = head.next
        temp3 = temp2.next
        temp1.next = None
        while temp3 != None:
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = temp3.next
        temp2.next = temp1
        return temp2
