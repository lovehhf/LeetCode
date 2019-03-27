# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.count_floor(root.right)-self.count_floor(root.left))>1:
            return False
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

    def count_floor(self,root):
        if not root:
            return 0
        return 1+max(self.count_floor(root.left),self.count_floor(root.right))