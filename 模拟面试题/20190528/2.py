# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
          
中序:左根右

"""

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution(object):
    def antiInorder(self, root):
        """
        反中序遍历
        :param root:
        :return: 返回反中序遍历的数的节点的引用
        """
        if not root:
            return []
        return self.antiInorder(root.right) + [root] + self.antiInorder(root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = self.antiInorder(root)
        n = len(nodes)
        for i in range(1, n):
            nodes[i].val = nodes[i - 1].val + nodes[i].val
        return root


s = Solution()
root = List2TN([5, 2, 13])
r = TN2List(s.convertBST(root))
print(r)
