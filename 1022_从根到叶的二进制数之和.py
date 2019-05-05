# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。

 

示例：



输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 深度优先遍历
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = self.binaryTreePaths(root)
        paths_sum = sum([int(x,2) for x in paths])%(10**9 + 7)
        return paths_sum

    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val), res)
        if root.right:
            self.dfs(root.right, ls + str(root.val), res)


    def sumRootToLeaf2(self, root: TreeNode) -> int:
        M = 10 ** 9 + 7
        def helper(root, t=0):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return (t*2+root.val) % M
            else:
                t *= 2
                t += root.val
                t %= M
                return (helper(root.left, t) + helper(root.right, t)) % M
        return helper(root)