# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

 

示例：



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 

提示：
next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator3(object):
    """
    使用生成器实现
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = None
        self.g = self.iterrate(root)

    def iterrate(self,node):
        if not node:
            return
        for x in self.iterrate(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterrate(node.right):
            yield x

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return next(self.g)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.current is not self.last

class BSTIterator2(object):
    """
    对中序遍历的修改，使用栈实现，空间复杂度符合要求
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


class BSTIterator(object):
    """
    空间复杂度不符合要求
    """
    def inOrder(self, root):
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right
        return res

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # 中序遍历
        self.inorder = self.inOrder(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.inorder.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.inorder:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()