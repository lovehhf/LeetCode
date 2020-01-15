# -*- coding:utf-8 -*-

"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
from utils.TreeNode import TreeNode, List2TN, TN2List


class Codec:

    def str2list(self, s):
        """
        树的字符串形式转成列表形式
        :param s:
        :return:
        """
        return s.split(',')

    def list2str(self, ls):
        """
        树的列表形式转成字符串形式，方便序列化
        :param ls:
        :return:
        """
        res = ','.join([str(x) for x in ls]).replace("#", "null")
        return res

    def serialize(self, root):
        """Encodes a tree to a single string.
        利用层次遍历将树序列化
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("#")
                continue
            res.append(node.val)
            # 左右子树进队列
            queue.append(node.left)
            queue.append(node.right)

        # 弹出底层叶子节点的左右节点
        while (res[-1] == '#'):
            res.pop()

        return self.list2str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = self.str2list(data)
        n = len(data)
        root = TreeNode(data[0])
        queue = collections.deque([root])
        l, r = 0, 0
        for i in range(1, n):
            node = queue[0]
            if not l:
                node.left = TreeNode(data[i])
                l = 1
                if data[i] != '#':
                    queue.append(node.left)
                continue

            if l and not r:
                node.right = TreeNode(data[i])
                r = 1
                if data[i] != '#':
                    queue.append(node.right)

            if l and r:
                queue.popleft()
                l, r = 0, 0
        return root


root = List2TN([1,2,None,3,None,4,None,5,None,6])
c = Codec()
#  序列化
s = c.serialize(root)

print(s)

# 反序列化
new_root = c.deserialize(s)

print(TN2List(new_root))
