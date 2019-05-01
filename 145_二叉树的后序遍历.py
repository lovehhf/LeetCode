# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.TreeNode import TreeNode,List2TN

class Solution(object):
    def postorderTraversal(self, root):
        """
        左右根
        :type root: TreeNode
        :rtype: List[int]
        """
        stack1 = [root]
        stack2 = []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur.val)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        return stack2[::-1]

root = List2TN([1,2,3,4,5,6,7])
s = Solution()
print(s.postorderTraversal(root))