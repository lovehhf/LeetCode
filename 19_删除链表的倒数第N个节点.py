# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # p指针先走n+1步,然后p,q指针一起走,找到倒数n+1个元素
        p = head
        for _ in range(n+1):
            if p:
                p  = p.next
            else:
                # 需要删除的是头结点,处理头结点
                head = head.next
                return head
        q = head
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head