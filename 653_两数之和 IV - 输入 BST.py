# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution:
    def inorder(self, root):
        """
        中序遍历二叉树
        :param root: 
        :return: List
        """

        # 非递归实现
        stack, cur= [], root
        ls = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                ls.append(node.val)
                cur = node.right
        # print(ls)
        return ls
        # 递归实现
        # if not root:
        #     return []
        # return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = self.inorder(root)
        n = len(nums)
        if n >= 2:
            L, R = 0, n - 1
            while L<R:
                num = nums[L] + nums[R]
                if num == k:
                    return True
                elif num > k:
                    R -= 1
                else:
                    L += 1
        return False

    def findTarget2(self, root, k):
        """
        bfs遍历二叉树
        使用了辅助列表存储节点
        :param root:
        :param k:
        :return:
        """
        if not root or (not root.left and not root.right):
            return False
        # dfs
        from collections import deque
        queue = deque([root])
        ls = []
        while queue:
            node = queue.popleft()
            ls.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        for i in ls:
            if (k-i) in ls and k!=2*i:
                return True
        return False

    def findTarget3(self, root, k):
        """
        使用辅助集合, bfs遍历二叉树的同时将值存入集合中
        :param root:
        :param k:
        :return:
        """
        if not root:
            return False

        return self.helper(root, set(), k)

    def helper(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True
        nodes.add(node.val)
        return self.helper(node.left, nodes, k) or self.helper(node.right, nodes, k)


l = [5,3,6,2,4,None,7]
root = List2TN(l)
k = 9
s = Solution()
print(s.findTarget(root,k))