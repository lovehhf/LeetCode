# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from utils.ListNode import List2LN

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        1. 添加虚拟头结点方便删除第一个节点
        2. 找到倒数第n个节点的前一个节点(也就是倒数k+1节点) 指向倒数第n个节点的下一个节点
        使用两个指针p,q,q先走k+1步,然后p,q一起走知道q走完整条链表,最后p指向的就是倒数k+1个节点
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy
        for _ in range(n + 1):
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     # p指针先走n+1步,然后p,q指针一起走,找到倒数n+1个元素
    #     p = head
    #     for _ in range(n+1):
    #         if p:
    #             p  = p.next
    #         else:
    #             # 需要删除的是头结点,处理头结点
    #             head = head.next
    #             return head
    #     q = head
    #     while p:
    #         p = p.next
    #         q = q.next
    #     q.next = q.next.next
    #     return head

head = List2LN([1,2,3,4,5])
s = Solution()
print(s.removeNthFromEnd(head,5))