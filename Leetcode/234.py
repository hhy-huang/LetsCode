"""
Link:       https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
Author:     Hhy
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        lenl = 1
        pend = head
        while pend.next != None:
            pend = pend.next
            lenl += 1
        if lenl == 1:
            return True

        temp = head
        curlen = 1
        while curlen != lenl / 2:
            temp = temp.next
            curlen += 1

        temp1 = temp
        temp2 = temp.next
        temp3 = temp2.next
        temp1.next = None
        while temp3 != None:
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = temp3.next
        temp2.next = temp1

        p = head
        while p != None:
            if p.val != pend.val:
                return False
            p = p.next
            pend = pend.next
        return True
