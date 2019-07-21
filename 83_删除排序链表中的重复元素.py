# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from utils.ListNode import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        指针p指向头结点head
        q指向p的后 一个节点
        如果p和q的值相同,p指向q的后一个节点
        如果pq值不同,p往前走一步
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p:
            q = p.next
            if q and q.val==p.val:
                p.next = q.next
            else:
                p = p.next
        return head

