# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

思路: 
定义一颗新的二叉树,节点存储根节点到这个节点所有可能的路径和
       [10]
       /  \
  [5,15]   [-3,7]
    /   \        \
[3,8,18][2,7,17] [11,8,18]
   / \    \
  3...-2...1
"""

from utils.TreeNode import TreeNode, List2TN


class Solution(object):
    def __init__(self):
        self.pathNum = 0

    def pathSum(self, root, sum):
        """
        非递归bfs实现 没有建新树，直接对树修改:
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        root.val = [root.val]
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                cur.left.val = [cur.left.val] + [cur.left.val + x for x in cur.val]
                queue.append(cur.left)
            if cur.right:
                cur.right.val = [cur.right.val] + [cur.right.val + x for x in cur.val]
                queue.append(cur.right)
            for i in cur.val:
                if i == sum:
                    res += 1
        return res

    def pathSum2(self, root, sum):
        """
        类变量 + 双重递归实现
        dfs:搜索以root为根节点的二叉树的路径数量
        :param root:
        :param sum:
        :return:
        """

        def dfs(root, s):
            if not root:
                return
            if s == root.val:  # 这里不能 return
                self.pathNum += 1
            dfs(root.left, s - root.val)
            dfs(root.right, s - root.val)

        if not root:
            return 0
        dfs(root, sum)
        self.pathSum2(root.left, sum)
        self.pathSum2(root.right, sum)
        return self.pathNum

    def pathSum3(self, root, sum):
        """
        双重递归+引用
        dfs:搜索以root为根节点的二叉树的路径数量
        :param root:
        :param sum:
        :return:
        """

        def dfs(root, s, res):
            if not root:
                return 0
            if s == root.val:
                res[0] += 1
            dfs(root.left, s - root.val, res)
            dfs(root.right, s - root.val, res)

        def helper(root, s, res):
            if not root:
                return 0
            dfs(root, s, res)
            helper(root.left, sum, res)
            helper(root.right, sum, res)

        res = [0]
        helper(root, sum, res)
        return res[0]

root = List2TN([1, -2, -3, 1, 3, -2, None, -1])
sum = -1
s = Solution()
print(s.pathSum3(root, sum))
