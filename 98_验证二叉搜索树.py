# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    中序遍历
    """

    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST2(self, root):
        """
        20190728
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(node):
            """
            中序遍历
            """
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        in_order = inorder(root)
        return list(sorted(set(in_order))) == in_order
