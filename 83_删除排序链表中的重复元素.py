# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(head):
        cur = head
        while(cur and cur.next):
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head