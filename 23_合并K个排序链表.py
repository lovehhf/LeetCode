# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge2Lists(self, phead, qhead):
        """
        合并2个有序链表
        """
        head = ListNode(0)
        p = head
        while phead and qhead:
            if phead.val < qhead.val:
                p.next = phead
                phead = phead.next
            else:
                p.next = qhead
                qhead = qhead.next
            p = p.next

        if phead:
            p.next = phead
        if qhead:
            p.next = qhead
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        from functools import reduce
        res = reduce(self.merge2Lists, lists)
        # res = self.merge2Lists(lists[0],lists[1])
        return res