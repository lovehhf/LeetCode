# -*- coding:utf-8 -*-

"""
590. N叉树的后序遍历
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal

给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
[1,null,3,2,4,null,5,6]
返回其后序遍历: [5,6,3,2,4,1].

说明: 递归法很简单，你可以使用迭代法完成此题吗?
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Recursive_Solution:

    def dfs(self, root):
        if not root:
            return []
        res = []
        for child in root.children:
            res += self.dfs(child)
        res.append(root.val)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        return self.dfs(root)
