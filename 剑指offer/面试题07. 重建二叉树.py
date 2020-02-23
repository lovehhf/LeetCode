# -*- coding:utf-8 -*-

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 
限制：
0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)

        # 用左子树的前序和中序遍历恢复左子树
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])

        # 右子树的前序和中序遍历恢复右子树
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root
