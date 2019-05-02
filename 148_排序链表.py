# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils.ListNode import ListNode, List2LN, LN2List


class Solution(object):

    def sortList(self, head):
        """
        * 归并排序法：在动手之前一直觉得空间复杂度为常量不太可能，因为原来使用归并时，都是 O(N)的，
        * 需要复制出相等的空间来进行赋值归并。对于链表，实际上是可以实现常数空间占用的（链表的归并
        * 排序不需要额外的空间）。利用归并的思想，递归地将当前链表分为两段，然后merge，分两段的方
        * 法是使用 fast-slow 法，用两个指针，一个每次走两步，一个走一步，知道快的走到了末尾，然后
        * 慢的所在位置就是中间位置，这样就分成了两段。merge时，把两段头部节点值比较，用一个 p 指向
        * 较小的，且记录第一个节点，然后 两段的头一步一步向后走，p也一直向后走，总是指向较小节点，
        * 直至其中一个头为NULL，处理剩下的元素。最后返回记录的头即可。
        *
        * 主要考察3个知识点，
        * 知识点1：归并排序的整体思想
        * 知识点2：找到一个链表的中间节点的方法
        * 知识点3：合并两个已排好序的链表为一个新的有序链表
        :param head:
        :return:
        """

        def mergeSort(head):
            """
            对链表进行归并排序
            :param head:
            :return:
            """
            if not head or not head.next:
                return head
            p, q = head, head  # 快慢指针
            r = None  # 记录慢指针前的一个节点,用于中断head,截取链表前半段，链表后半段为慢指针所指向的链表
            while q and q.next:
                r = p
                p = p.next
                q = q.next.next
            r.next = None
            l, r = mergeSort(head), mergeSort(p)
            return merge(l, r)

        def merge(l1, l2):
            """
            归并2条有序链表
            :param l:
            :param r:
            :return:
            """
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    p = p.next
                    l1 = l1.next
                else:
                    p.next = l2
                    p = p.next
                    l2 = l2.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next
        if not head:
            return
        return mergeSort(head)

    def sortList2(self, head):
        """
        插排 不符合题目要求
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        MIN = -2 ** 32
        p = ListNode(MIN)
        while head:
            q = p
            while q.next and q.next.val < head.val:
                q = q.next
            t = ListNode(head.val)
            q.next, t.next = t, q.next
            head = head.next
        return p.next

    def sortList3(self, head):
        """
        空间复杂度不符合要求
        :param head:
        :return:
        """
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ls.sort()
        dummy = ListNode(0)
        p = dummy
        for i in ls:
            p.next = ListNode(i)
            p = p.next
        return dummy.next



s = Solution()
head = List2LN([4, 2, 1, 3])
print(LN2List(s.sortList3(head)))
