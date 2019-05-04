# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.TreeNode import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        bfs 常规做法 没有利用到完全二叉树的性质
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            res += 1
        return res

    def countNodes2(self, root: TreeNode) -> int:
        """
        完全二叉树的高度可以直接通过不断地访问左子树就可以获取
        判断左右子树的高度:
        如果相等说明左子树是满二叉树, 然后进一步判断右子树的节点数(最后一层最后出现的节点必然在右子树中)
        如果不等说明右子树是深度小于左子树的满二叉树, 然后进一步判断左子树的节点数(最后一层最后出现的节点必然在左子树中)
        :param root:
        :return:
        """

        def getDepth(node):
            """
            :param node:
            :return:
            """
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        if not root:
            return 0
        ld = getDepth(root.left)
        rd = getDepth(root.right)
        if ld == rd:
            return 1 << ld + self.countNodes2(root.right)  # 1(根节点) + (1 << ld)-1(左完全左子树节点数) + 右子树节点数量
        else:
            return 1 << rd + self.countNodes2(root.left)  # 1(根节点) + (1 << rd)-1(右完全右子树节点数) + 左子树节点数量

    def countNodes3(self, root: TreeNode) -> int:
        return 0 if not root else self.countNodes3(root.left) + self.countNodes3(root.right)
