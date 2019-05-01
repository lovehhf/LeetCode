# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.TreeNode import TreeNode, List2TN


class Solution:
    def levelOrder(self, root):
        """
        bfs
        :param root:
        :return:
        """
        if not root:
            return []
        queue = [(root, 0)]
        ls = []
        while queue:
            cur, level = queue.pop(0)
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
            ls.append((cur.val, level))
            # print(ls)
        level = ls[-1][-1]
        res = [[] for _ in range(level + 1)]
        for i, j in ls:
            res[j].append(i)
        return res

    def levelOrder4(self, root):
        """
        层序遍历一般来说确实是用队列实现的，但是这里很明显用递归前序遍历就能实现呀，而且复杂度O(n)。。。
        要点有几个：
        - 利用depth变量记录当前在第几层（从0开始），进入下层时depth + 1；
        - 如果depth >= vector.size()说明这一层还没来过，这是第一次来，所以得扩容咯；
        - 因为是前序遍历，中-左-右，对于每一层来说，左边的肯定比右边先被遍历到，实际上后序中序都是一样的。。。
        :param root:
        :return:
        """
        def pre(node, depth, ans):
            if not node:
                return
            if depth >= len(ans):
                ans.append([])
            ans[depth].append(node.val)
            pre(node.left, depth + 1, ans)
            pre(node.right, depth + 1, ans)
        ans = [[]]
        pre(root, 0, ans)
        return ans

    def levelOrder3(self, root):
        """
        递归实现前序遍历
        同时将节点以及所在层次写入辅助字典中
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}

        def helper(node, lv):
            if not node:
                return
            if not lv in d:
                d[lv] = [node.val]
            else:
                d[lv].append(node.val)
            helper(node.left, lv + 1)
            helper(node.right, lv + 1)

        helper(root, 1)
        print(d)
        return [d[x] for x in d]

    def lo(self, nodes):
        while nodes:
            yield [n.val for n in nodes]
            nodes = [m for n in nodes for m in (n.left, n.right) if m is not None]

    def levelOrder2(self, root):
        """
        copy来的代码 暂时还没看懂
        :param root:
        :return:
        """

        if root is None:
            return []
        return list(self.lo([root]))


l = [3, 9, 20, None, None, 15, 7]
root = List2TN(l)
s = Solution()
print(s.levelOrder4(root))
