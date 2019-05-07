# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

示例：



输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

你只能使用**常量级额外空间**。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

与116不同的是给的只是普通二叉树不是完全二叉树

需要先确保 root.right 下的节点的已完全连接，因 root.left 下的节点的连接
需要 root.left.next 下的节点的信息，若 root.right 下的节点未完全连
接（即先对 root.left 递归），则 root.left.next 下的信息链不完整，将
返回错误的信息。可能出现的错误情况如下图所示。此时，底层最左边节点将无
法获得正确的 next 信息：
所以要先递归右子树
                 o root
                / \
    root.left  o —— o  root.right
              /    / \
             o —— o   o
            /        / \
           o        o   o
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def nextNode(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.right
            return

        if not root:
            return
        if root.right and root.left:
            # 左右子树都存在 则左子树的节点就是右子树
            root.left.next = root.right
        elif root.left:
            # 如果右子树不存在 左子树的next指针要看root的next
            root.left.next = nextNode(root.next)
        if root.right:
            # 右子树的 next指针 由根节点的 next 得出
            root.right.next = nextNode(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

