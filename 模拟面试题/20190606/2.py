# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""

from utils.ListNode import ListNode, List2LN


class Solution(object):
    def reverseList(self, head):
        p = head
        q = p.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
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
        p = self.reverseList(p)
        while head.next and p.next:
            head.next, p.next, p, head = p, head.next, p.next, head.next
        head.next = p



head = List2LN([1, 2, 3, 4, 5])
s = Solution()
# print(s.reverseList(head))
s.reorderList(head)
print(head)