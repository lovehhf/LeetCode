# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        时间复杂度:O(n) 空间复杂度:O(1)
        :param head:
        :return:
        """
        n = 0  # 链表长度
        t = head
        while t:
            n+=1
            t = t.next
        # 这里可以使用快慢指针找到中间节点
        mid = n // 2
        # 从mid后开始翻转链表
        phead = head
        for _ in range(mid):
            phead = phead.next
        p = phead
        q = phead.next
        phead.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        # 1>2 3<2<1
        #head     p
        for _ in range(mid):
            if head.val!=p.val:
                return False
            head = head.next
            p = p.next
        return True

    def isPalindrome_3(self, head):
        """
        利用辅助空间
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = None
    s = Solution()
    print(s.isPalindrome(head))