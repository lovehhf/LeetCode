# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        """
        :param pHead1:
        :param pHead2:
        :return:
        """
        pHead = ListNode(0)
        p = pHead
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pHead.next = pHead1
                pHead1 = pHead1.next
            else:
                pHead.next = pHead2
                pHead2 = pHead2.next
            pHead = pHead.next
        if pHead1:
            pHead.next = pHead1
        if pHead2:
            pHead.next = pHead2
        return p.next
