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
        if not headA or not headB:
            return None
        len_a = 0
        len_b = 0
        a = headA
        b = headB
        while a:
            a = a.next
            len_a += 1
        while b:
            b = b.next
            len_b += 1
        k = len_a-len_b
        # print(len_a,len_b)
        if k>0:
            for i in range(k):
                headA = headA.next
        if k<0:
            k = -k
            for i in range(k):
                headB = headB.next
        if not headA.next or headB.next:
            if headA == headB:
                return headA
        while headA:
            headA = headA.next
            headB = headB.next
            if headA == headB:
                return headA
        return None