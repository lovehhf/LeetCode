# -*- coding:utf-8 -*-

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
"""

from typing import List
from utils.TreeNode import TreeNode, List2TN


class Solution:
    def dfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + [root.val] + right

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.dfs(root)


s = Solution()
root = List2TN([5, 1, 4, None, None, 3, 6])
res = s.inorderTraversal(root)
print(res)
