# -*- coding:utf-8 -*-

"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        序列化, 队列, bfs
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = [root]
        res = []

        while queue:
            cur = queue.pop(0)
            if cur:
                res.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('null')

        while (res[-1] == 'null'):
            res.pop()

        return ','.join([str(x) for x in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        反序列化, 队列
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(',')
        root = TreeNode(nodes[0])
        queue = [root]
        n = len(nodes)
        i = 0

        while (queue):
            # 队列的队头节点是 i + 1, i + 2 的父节点
            cur = queue.pop(0)

            # 左子树
            if i + 1 < n and nodes[i + 1] != 'null':
                cur.left = TreeNode(nodes[i + 1])
                queue.append(cur.left)

            # 右子树
            if i + 2 < n and nodes[i + 2] != "null":
                cur.right = TreeNode(nodes[i + 2])
                queue.append(cur.right)

            i += 2

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
