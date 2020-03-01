# -*- coding:utf-8 -*-

"""
给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

示例 1：
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。

示例 2：

输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true

示例 3：
输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。
 
提示：
二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
链表包含的节点数目在 1 到 100 之间。
二叉树包含的节点数目在 1 到 2500 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode
from utils.ListNode import ListNode


class Solution:
    def dfs(self, head, root):
        """
        :param head:
        :param root:
        :return:
        """
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        if self.dfs(head.next, root.left) or self.dfs(head.next, root.right):
            return True
        return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        """
        双重dfs, 枚举以每个点作为根节点是否有满足要求的树
        与剑指offer 面试题26. 树的子结构 类似
        :param head:
        :param root:
        :return:
        """
        if not root:
            return False
        if self.dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
