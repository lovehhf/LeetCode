# -*- coding:utf-8 -*-

"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = -float('inf')

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # 计算以node为根节点的路径的最大值
        self.res = max(self.res, left + right + node.val)
        # 返回节点对父节点的贡献
        return max(0, node.val + max(left, right))

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return int(self.res)
