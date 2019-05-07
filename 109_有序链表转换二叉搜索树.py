# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
 """
from utils.ListNode import List2LN
from utils.TreeNode import TreeNode, TN2List


class Solution(object):
    def sortedListToBST(self, head):
        """
        1. 快慢指针找中间点
        2. 递归建立左右子树
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        p, q, pre = head, head, None  # p:慢指针 q:快指针 pre:截断中间点
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        pre.next = None
        root = TreeNode(p.val)
        p = p.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p)
        return root


head = List2LN([-10, -3, 0, 5, 9])
s = Solution()
root = s.sortedListToBST(head)
print(TN2List(root))
