# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""

from utils.ListNode import ListNode, List2LN


class Solution(object):
    def merge(self, left, right):
        """
        归并2条有序链表 使用常数级别额外空间
        :param left:
        :param right:
        :return:
        """
        dummy = ListNode(0)
        head = dummy
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        if right:
            head.next = right
        return dummy.next

    def sortList(self, head):
        """
        链表的归并排序
        1.快慢指针找中间点
        2.归并2条链表
        时间复杂度O(nlogn)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p, q = head, head
        pre = p
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        pre.next = None
        l = self.sortList(head)
        r = self.sortList(p)
        return self.merge(l, r)


head = List2LN([4, 2, 3, 1])
s = Solution()
print(s.sortList(head))
print(s.merge(List2LN([2, 4]), List2LN([1, 3])))
