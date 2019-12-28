# -*- coding:utf-8 -*-

"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。



示例：



输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15


提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。

mid
只想到了bfs的解法
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = [0] * 10010
        q = [(root, 0)]
        level = 0
        while q:
            cur, level = q.pop(0)
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))
            if not cur.left and not cur.right:
                s[level] += cur.val
        return s[level]
