# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

from utils.TreeNode import List2TN

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            res.append(cur.val)
        return res

root = List2TN([1,None,2,3])
s = Solution()
print(s.preorderTraversal(root))