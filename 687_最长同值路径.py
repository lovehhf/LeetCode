# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, val):
            """
            返回当前树的最长等值路径 和 当前根节点延伸下去值为val的最高深度
            :param root:
            :param val:
            :return:
            """
            if not root:
                return 0, 0
            l_max, l_val = dfs(root.left, root.val)
            r_max, r_val = dfs(root.right, root.val)
            now_max = max(l_max, r_max, l_val + r_val)
            if root.val != val:
                return now_max, 0
            now_val = max(l_val, r_val) + 1
            return now_max, now_val

        if not root:
            return 0
        return dfs(root, root.val)[0]


root = List2TN([5, 4, 5, 1, 1, 5])
s = Solution()
print(s.longestUnivaluePath(root))
