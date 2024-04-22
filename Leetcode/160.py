"""
Link:           https://leetcode.cn/problems/intersection-of-two-linked-lists/description/?envType=study-plan-v2&envId=top-100-liked
Author:         Hhy
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA == headB:
            return headA
        if headA == None or headB == None:
            return None

        pa = copy.deepcopy(headA)
        lena = 0
        pb = copy.deepcopy(headB)
        lenb = 0
        while pa != None:
            pa = pa.next
            lena += 1
        while pb != None:
            pb = pb.next
            lenb += 1
        pa = headA
        pb = headB
        if lena > lenb:
            while lena != lenb:
                pa = pa.next
                lena -= 1
        elif lena < lenb:
            while lenb != lena:
                pb = pb.next
                lenb -= 1
        while pa != None:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None
