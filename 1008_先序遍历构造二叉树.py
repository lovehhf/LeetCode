# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）

 

示例：

输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            curr = TreeNode(preorder[i])
            if curr.val < stack[-1].val:
                stack[-1].left = curr
            else:
                par = None
                while stack and curr.val > stack[-1].val:
                    par = stack.pop()
                par.right = curr
            stack.append(curr)

        def bstFromPreorder2(self, preorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            i = 1
            while i < len(preorder):
                if preorder[i] < preorder[0]:
                    i += 1
                else:
                    break
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root
        return root


def print_tree(root):
    if not root:
        return []
    return [root.val] + print_tree(root.left) + print_tree(root.right)

preorder = [8,5,1,7,10,12]
s = Solution()
root = s.bstFromPreorder(preorder)
print(print_tree(root))