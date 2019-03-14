# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head):
        """
        迭代
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        p = head
        q = head.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        p = head.next
        newHead = self.reverseList(p)
        p.next = head
        head.next = None
        return newHead