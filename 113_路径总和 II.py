# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from utils.TreeNode import List2TN


class Solution(object):
    def dfs(self, root, s, path, res):
        if not root:
            return []
        if not root.left and not root.right:
            if sum(path) + root.val == s:
                res.append(path + [root.val])
                return
        self.dfs(root.left, s, path + [root.val], res)
        self.dfs(root.right, s, path + [root.val], res)

    def pathSum(self, root, sum):
        """
        dfs path记录走过得路径,碰到叶子节点检查路径和是不是符号要求
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, [], res)
        return res


root = List2TN([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
s = Solution()
print(s.pathSum(root, 22))
