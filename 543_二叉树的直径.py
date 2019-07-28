# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import List2TN


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        左子树深度 + 右子树深度
        :type root: TreeNode
        :rtype: int
        """

        def get_bt_depth(node):
            if not node:
                return 0
            return max(get_bt_depth(node.left), get_bt_depth(node.right)) + 1

        return max(get_bt_depth(root.left) + get_bt_depth(root.right), self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right)) if root else 0


s = Solution()
root = List2TN(
    [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4,
     None, None, None, -2])
print(s.diameterOfBinaryTree(root))
