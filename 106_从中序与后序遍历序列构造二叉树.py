# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, TN2List


class Solution:
    def buildTree(self, inorder, postorder):
        """
        inorder 左根右
        postorder 左右根
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder or not postorder:
            return
        root = TreeNode(postorder[-1])
        in_index = inorder.index(root.val)
        left_inorder, right_inorder = inorder[:in_index], inorder[in_index + 1:]
        left_postorder, right_postorder = postorder[:in_index], postorder[in_index:-1]
        # print(left_inorder, right_inorder)
        # print(left_postorder, right_postorder)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root


s = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = s.buildTree(inorder, postorder)
print(root)
res = TN2List(root)
print(res)
