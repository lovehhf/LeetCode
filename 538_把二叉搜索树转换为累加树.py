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
"""

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution(object):
    def convertBST(self, root):
        """
        右->根->左的中序遍历
        非递归写法
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        cur = root
        s = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                node = stack.pop()
                s += node.val
                # TreeNode append到链表中的是TreeNode的引用，修改会对原二叉树生效
                node.val = s
                cur = node.left
        return root

    def convertBST2(self, root):
        """
        递归+类变量
        :param root:
        :return:
        """
        self.s = 0

        def helper(root):
            if not root:
                return
            helper(root.right)
            root.val += self.s
            self.s = root.val
            helper(root.left)

        # helper(root)
        return root

    def convertBST3(self, root):
        """
        递归+方法参数
        :param root:
        :return:
        """
        def helper(root, s):
            if not root:
                return
            helper(root.right, s)
            root.val += s[0]
            s[0] = root.val
            helper(root.left, s)
        helper(root, [0])
        return root

    def convertBST4(self, root):
        """
        递归+方法返回值
        :param root:
        :return:
        """
        def helper(root, s1):
            if not root:
                return s1
            s2 = helper(root.right, s1)
            root.val += s2
            s2 = root.val
            s2 = helper(root.left, s2)
            return s2
        helper(root, 0)
        return root


root = List2TN([5, 2, 13])
s = Solution()
print(TN2List(s.convertBST4(root)))
