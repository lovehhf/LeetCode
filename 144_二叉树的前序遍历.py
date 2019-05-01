# -*- coding:utf-8 -*-

__author__ = 'huanghf'


# Definition for a binary tree node.
from utils.TreeNode import TreeNode,List2TN

class Solution(object):
    def preorderTraversal(self,root):
        """
        根->左->右
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

root = List2TN([1,2,3,4,5,6,7])
s = Solution()
print(s.preorderTraversal(root))