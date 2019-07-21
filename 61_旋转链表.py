# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k) -> ListNode:
        """
        第n-k个数的next节点指向None
        尾节点指向头结点
        :param head:
        :param k:
        :return:
        """
        if not head or k == 0 or not head.next:
            return head
        t = head
        n = 0    # 长度
        while t:
            n += 1
            t = t.next
        if k%n == 0:
            return head
        p = head
        for i in range(n-k%n-1):
            p = p.next
        newhead = p.next
        q = newhead
        for i in range(k%n-1):
            q = q.next
        q.next = head
        p.next = None
        return newhead

    def rotateRight2(self, head, k):
        """
        20190718
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 求链表长度
        n = 1
        end = head
        while end and end.next:
            end = end.next
            n += 1
        k = k % n
        # 特殊情况
        if not head or not k:
            return head
        # 找出链表的倒数k+1个节点和倒数第k个节点
        dummy = ListNode(0)
        dummy.next = head
        start = head
        for _ in range(n - k):
            dummy = dummy.next
            start = start.next
        # 尾结点指向头结点,倒数第k+1个节点指向倒数第k个节点，返回倒数第k个节点
        end.next = head
        dummy.next = None
        return start
