# -*- coding:utf-8 -*-

"""
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。

示例：

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。

提示：
树中节点的数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode
import collections


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        bfs
        给偶数节点的儿子打上标记, 有标记的节点加上这个节点的儿子的值
        :param root:
        :return:
        """
        queue = collections.deque([(root, False)])
        res = 0
        while queue:
            cur, flag = queue.popleft()
            if cur.left:
                if flag:
                    res += cur.left.val
                queue.append((cur.left, cur.val & 1 == 0))
            if cur.right:
                if flag:
                    res += cur.right.val
                queue.append((cur.right, cur.val & 1 == 0))
        return res
