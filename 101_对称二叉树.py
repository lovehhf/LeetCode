# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""

from utils.TreeNode import List2TN


class Solution(object):
    def isSymmetric(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: bool
        """

        def check(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            return check(l.left, r.right) and check(l.right, r.left) if l.val == r.val else False

        return check(root, root)

    def isSymmetric2(self, root):
        """
        类bfs
        每次提取两个结点并比较它们的值。
        然后，将两个结点的左右子结点按相反的顺序插入队列中。
        当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时,算法结束。
        :param root:
        :return:
        """
        queue = [root,root]
        while queue:
            t1,t2 = queue.pop(0),queue.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

    def isSymmetric3(self, root):
        """
        迭代 用栈模拟递归 对根节点的左子树用中序遍历，对根节点的右子树，使用反中序遍历
        当且仅当同时遍历两课子树时，对应节点的值相等 两个子树互为镜像
        :param root:
        :return:
        """
        if not root:
            return True
        left, right = [], []
        lc, rc = root.left, root.right
        while lc or rc or left:
            while lc and rc:
                left.append(lc)
                right.append(rc)
                lc, rc = lc.left, rc.right
            if lc or rc:
                return False
            lc, rc = left.pop(), right.pop()
            if lc.val != rc.val:
                return False
            lc, rc = lc.right, rc.left
        return True


root = List2TN([1,2,3])
s = Solution()
print(s.isSymmetric2(root))
print(s.isSymmetric(root))
print(s.isSymmetric3(root))
