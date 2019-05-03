# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""

from utils.ListNode import ListNode, List2LN,LN2List

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        dummy = ListNode(0)
        pre = dummy  # p的前一个节点 用于删除最后的重复节点
        pre.next = p

        while pre.next and p and p.next:
            if p.val == p.next.val:
                t = p
                while t.next and t.val == t.next.val:  # t指向重复的最后一个节点
                    t = t.next
                if t.next:
                    p.val = t.next.val
                    p.next = t.next.next
                else:
                    # print(pre,p,t)
                    if dummy is pre:
                        return  # 处理所有节点都相同的特殊情况,pre没有移动过
                    pre.next = None
            else:
                p = p.next
                pre = pre.next
        return head

    def deleteDuplicates2(self, head):
        """
        记录下是否需要删除最右一个节点
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        flag = False # flag 用于记录是否删除最后一个节点
        while p and p.next:
            if p.val == p.next.val:
                t = p
                while t.next and t.val == t.next.val:  # t指向重复的最后一个节点
                    t = t.next
                if t.next:
                    p.val = t.next.val
                    p.next = t.next.next
                else:
                    flag = True
                    p.next = None
            else:
                p = p.next
        if flag:
            if not head.next:  # 所有节点都相同,直接返回
                return
            # 删除最后一个节点
            p,q = head,head.next
            print(p,q)
            while q.next:
                p = p.next
                q = q.next
            p.next = None
        return head

    def deleteDuplicates3(self, head):
        """
        看大佬cpp代码后想到的处理方式
        精简了一些上面的代码中不需要的步骤
        用left和right两个指针判断是否有重复出现的元素,如果有重复元素,p指向right.next
        不需要像上面的代码一样处理最后一个重复的字符
        :param head:
        :return:
        """
        p = ListNode(0)
        p.next = head
        dummy = p
        while p.next:
            left = p.next
            right = left
            while right.next and right.next.val == left.val:
                right = right.next
            if left == right:
                p = p.next
            else:
                p.next = right.next
        return dummy.next

    def deleteDuplicates4(self, head):
        """
        递归实现
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        node = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            if node or head.val == node.val:
                return node.next
            elif(node and head.val!=node.val):
                return node
            else:
                return
        else:
            head.next = node
            return head


head = List2LN([1,2,2,3,3,4,4,5,5,6])
s = Solution()
print(s.deleteDuplicates4(head))