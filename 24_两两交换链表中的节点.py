# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

迭代：

-1 -> 1 -> 2 -> 3 -> 4 -> None
p     q    r
第一次迭代:
-1 -> 2 -> 1 -> 3 -> 4 -> None
      r   p,q  
第二次迭代：
-1 -> 2 -> 1 -> 4 -> 3 -> None
                r   p,q
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代解法, 使用三个指针 p, q, r 不停地改变他们的  next 指针
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while(p.next and p.next.next):
            q = p.next
            r = q.next
            p.next = r
            q.next = r.next
            r.next = q
            p = q
        return dummy.next
        

class Recursion_Solution:

    def swapPairs(self, head):
        """
        方法一使用递归来解决该题，主要就是递归的三部曲：

        1. 找终止条件：本题终止条件很明显，当递归到链表为空或者链表只剩一个元素的时候，没得交换了，自然就终止了。
        2. 找返回值：返回给上一层递归的值应该是已经交换完成后的子链表。
        3. 单次的过程：因为递归是重复做一样的事情，所以从宏观上考虑，只用考虑某一步是怎么完成的。我们假设待交换的俩节点分别为head和next，next的应该接受上一级返回的子链表(参考第2步)。就相当于是一个含三个节点的链表交换前两个节点，就很简单了，想不明白的画画图就ok。
        """
        if not head or not head.next:
            return head
        nextNode = head.next
        head.next = self.swapPairs(nextNode.next)
        nextNode.next = head
        return nextNode
