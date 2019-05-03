# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

from utils.ListNode import ListNode, List2LN


class Solution(object):
    def partition(self, head, x):
        """
        借助两个虚拟头节点实现
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p,q = dummy1,dummy2
        while head:
            if head.val<x:
                p.next = head
                p = p.next
                head = head.next
            else:
                q.next = head
                q = q.next
                head = head.next
        p.next,q.next = dummy2.next,None
        return dummy1.next


s = Solution()
head = List2LN([1, 4, 3, 2, 5, 2])
x = 3
print(s.partition(head, x))
