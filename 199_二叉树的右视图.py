# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

from utils.TreeNode import TreeNode, List2TN


class Solution:
    def rightSideView(self, root):
        """
        bfs res添加每层的最右边的值
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            count = len(queue)  # 第i层的节点数量
            while count > 0:
                count -= 1
                cur = queue.pop(0)
                if count == 0:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
        # [1,2,3,4] --> [1,3]
        # 下面的代码没有考虑左子树比右子树层数高的情况
        # while stack:
        #     cur = stack.pop()
        #     if cur.right:
        #         stack.append(cur.right)
        #     else:
        #         if cur.left:
        #             stack.append(cur.left)
        #     res.append(cur.val)
        # return res

    def rightSideView2(self, root):
        """
        递归dfs
        这道题的本质就是获取每层最右边的元素，可以用当前遍历深度和结果集的大小作为限定条件，当
        当前深度还没有添加元素时，优先遍历最右的元素并添加，添加后遍历本层其他元素也不影响结果集中的值
        :param root:
        :return:
        """

        def dfs(node, depth, res):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            # 优先遍历右子树,添加了右子树的元素后len(res)+1
            # 再遍历同层的左子树时不会往res添加元素
            dfs(node.right, depth + 1, res)
            dfs(node.left, depth + 1, res)

        res = []
        dfs(root, 0, res)
        return res


s = Solution()
root = List2TN([1,2,3,4])
print(s.rightSideView2(root))
