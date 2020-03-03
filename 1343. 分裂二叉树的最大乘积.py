# -*- coding:utf-8 -*-

"""
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。
由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

示例 1：
输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）

示例 2：
输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）

示例 3：
输入：root = [2,3,9,10,7,8,6,5,4,11,1]
输出：1025

示例 4：
输入：root = [1,1]
输出：1

提示：
每棵树最多有 50000 个节点，且至少有 2 个节点。
每个节点的值在 [1, 10000] 之间。



和 124. 二叉树中的最大路径和类似

解题步骤:
1. 算出树的所有节点的和
2. dfs 遍历二叉树求以所有节点为根节点的子二叉树的和, 总的和减掉这个子二叉树的和就是另一棵二叉树的和
3. 找出最大的积
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0
        self.s = 0
        self.mod = 10 ** 9 + 7

    def get_sum(self, root):
        """
        求整棵二叉树的和
        :param root:
        :return:
        """
        if not root:
            return 0
        return root.val + self.get_sum(root.left) + self.get_sum(root.right)

    def dfs(self, root):
        if not root:
            return 0
        ss = self.dfs(root.left) + self.dfs(root.right) + root.val  # 子二叉树的和
        self.res = max(self.res, (self.s - ss) * ss)  # 找出最大的积
        return ss  # 返回子二叉树的和, 用于它的父节点计算父节点的二叉树的和

    def maxProduct(self, root: TreeNode) -> int:
        self.s = self.get_sum(root)
        self.dfs(root)
        return self.res % self.mod
