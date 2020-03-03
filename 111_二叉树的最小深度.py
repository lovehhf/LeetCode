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


from utils.TreeNode import TreeNode


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # 左子树最小深度
        l = self.minDepth(root.left)

        # 右子树最小深度
        r = self.minDepth(root.right)

        # 没有左子树, 深度为右子树最小深度 + 1
        if not root.left:
            return r + 1

        # 没有右子树, 深度为左子树最小深度 + 1
        if not root.right:
            return l + 1

        return min(l, r) + 1