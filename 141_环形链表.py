# -*- coding:utf-8 -*-

__author__ = 'huanghf'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast = head.next  # 快指针先行一步
        slow = head  # 慢指针
        while (fast != slow):  # 快慢指针赛跑
            # 快指针跑完整个链表说明有环
            if not fast or not fast.next:
                return False
            fast = fast.next.next  # 快指针每次走两步
            slow = slow.next  # 慢指针每次走一步
        # 快指针与慢指针相遇 说明有环
        return True
