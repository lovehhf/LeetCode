# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

from utils.ListNode import List2LN, ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        while head:
            p = dummy
            # 链表插排 找到最后一个比head小的节点指向head
            while p.next and p.next.val < head.val:
                p = p.next
            q = head # q替换head head往前走
            head = head.next
            p.next, q.next = q, p.next
        return dummy.next

head = List2LN([4, 2, 1, 3])
s = Solution()
print(s.insertionSortList(head))
