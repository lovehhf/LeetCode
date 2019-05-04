# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        前序遍历
        :param root:
        :return:
        """
        stack = [root]
        while stack and root:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if cur != root:
                root.left, root.right = None, TreeNode(cur.val)
                root = root.right

    def flatten2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        res = []
        while stack and root:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            res.append(cur.val)
        if res:
            while res:
                root.left = None
                root.right = TreeNode(res.pop(0))
                root = root.right


root = List2TN([1, 2, 5, 3, 4, None, 6])
s = Solution()
s.flatten(root)
print(TN2List(root))
