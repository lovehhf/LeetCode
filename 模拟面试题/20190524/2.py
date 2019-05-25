# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
from utils.ListNode import List2LN, ListNode


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next


head = List2LN([1, 1, 1, 1, 2, 3, 4, 5])
s = Solution()
print(s.removeElements(head, 1))
