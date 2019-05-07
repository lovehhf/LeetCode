# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

示例：



输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """'
        修已改版bfs 只使用常数项空间
        经有上一层的next了，所以就不需要队列来存储了
        :type root: Node
        :rtype: Node
        """
        if not root or not root.left:
            return root
        pre = root
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:  # 左子树的右子树next指针指向右子树的左子树
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

    def connect2(self, root):
        """
        bfs遍历每一层 下一个节点在同一个节点的时候next指向下一个节点
        不符合常数空间要求
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = [(root, 0)]
        while queue:
            cur, depth = queue.pop(0)
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
            if queue and queue[0][1] == depth:
                cur.next = queue[0][0]
        return root

    def connect3(self, root):
        """'
        递归版
        :type root: Node
        :rtype: Node
        """
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect3(root.left)
        self.connect3(root.right)
        return root
