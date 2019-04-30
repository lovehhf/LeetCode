# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utils.ListNode import ListNode,LN2List,List2LN

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法三 看了大佬的代码后 修改出的代码
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)
        p = head
        carry = 0
        while l1 or l2:
            x,y = l1.val if l1 else 0,l2.val if l2 else 0
            s = x + y + carry
            r,carry = s%10,s//10
            p.next = ListNode(r)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            p.next = ListNode(1)
        return head.next

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法二  不使用额外的列表
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)
        p = head
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            r,carry = s%10,s//10
            p.next = ListNode(r)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if not l1 and not l2:
            if carry:
                p.next = ListNode(1)
                p = p.next
        if l1:
            # print(l1,carry)
            if not carry:
                p.next = l1
            else:
                while l1 and l1.val == 9:
                    p.next = ListNode(0)
                    p = p.next
                    l1 = l1.next
                if not l1:
                    p.next = ListNode(1)
                else:
                    p.next = ListNode(l1.val + 1)
                    p = p.next
                    l1 = l1.next
                    p.next = l1
        if l2:
            if not carry:
                p.next = l2
            else:
                while l2 and l2.val == 9:
                    p.next = ListNode(0)
                    p = p.next
                    l2 = l2.next
                if not l2:
                    p.next = ListNode(1)
                else:
                    p.next = ListNode(l2.val + 1)
                    p = p.next
                    l2 = l2.next
                    p.next = l2
        return head.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法一 计算两数之和存放到列表中,再将列表转为链接
        :param l1:
        :param l2:
        :return:
        """

        head = ListNode(0)
        a,b,i,j = 0,0,0,0
        while l1:
            a += l1.val*10**i
            i += 1
            l1 = l1.next
        while l2:
            b += l2.val*10**j
            j += 1
            l2 = l2.next
        l = [int(x) for x in list(str(a+b))]
        p = head
        for i in l[::-1]:
            p.next = ListNode(i)
            p = p.next
        p.next = None
        return head.next

l1 = List2LN([9,9,9])
l2 = List2LN([1])
s = Solution()
print(s.addTwoNumbers(l1,l2))