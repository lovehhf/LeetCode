# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        phead = head
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        # 处理头结点
        if phead and phead.val == val:
            phead = phead.next
        return phead
