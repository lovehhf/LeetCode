# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 没有根节点深度为0
        if not root:
            return 0
        # # 没有左右子树,深度为1
        if not root.left and not root.right:
            return 1
        # 没有左子树,深度为右子树的最小深度+1
        if not root.left:
            return 1 + self.minDepth(root.right)
        # 没有右子树,深度为左子树的最小深度+1
        if not root.right:
            return 1 + self.minDepth(root.left)
        # 有左右子树，深度为左右子树中深度小的树的深度+1
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
