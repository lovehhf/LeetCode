# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, List2TN


class Solution(object):
    def __init__(self):
        self.res = 0

    def dfs(self, root, path):
        if not root:
            return
        if not root.left and not root.right:  # 叶子节点
            self.res += int(path + str(root.val))
            return
        self.dfs(root.left, path + str(root.val))
        self.dfs(root.right, path + str(root.val))

    # def dfs(self, root, path):
    #     if not root:
    #         return
    #     num = path * 10 + root.val  # num 代表当前节点所代表的数
    #     if not root.left and not root.right:  # 叶子节点
    #         self.res += num
    #         return
    #     self.dfs(root.left, num)
    #     self.dfs(root.right, num)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, '')
        return self.res

    def sumNumbers2(self, root):
        """
        非递归实现
        :param root:
        :return:
        """
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            cur, num = stack.pop()   # num表示根节点到当前节点所代表的数
            if cur.right:
                stack.append((cur.right, num * 10 + cur.right.val))
            if cur.left:
                stack.append((cur.left, num * 10 + cur.left.val))
            if not cur.left and not cur.right:
                res += num
        return res


root = List2TN([4, 9, 0, None, 1])
s = Solution()
print(s.sumNumbers2(root))
