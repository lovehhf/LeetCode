# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]
"""
from  utils.TreeNode import TreeNode,List2TN


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            q = []
            t_max = float('-inf')
            while queue:
                cur = queue.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                t_max = max(cur.val,t_max)
            queue = q
            res.append(t_max)
        return res


s = Solution()
root = List2TN([1,3,2,5,3,None,9])
print(s.largestValues(root))
