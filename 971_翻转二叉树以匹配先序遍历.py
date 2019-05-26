# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个有 N 个节点的二叉树，每个节点都有一个不同于其他节点且处于 {1, ..., N} 中的值。

通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。

考虑从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程。

（回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）

我们的目标是翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。 

如果可以，则返回翻转的所有节点的值的列表。你可以按任何顺序返回答案。

如果不能，则返回列表 [-1]。

示例 1：

输入：root = [1,2], voyage = [2,1]
输出：[-1]
示例 2：

输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]
示例 3：

输入：root = [1,2,3], voyage = [1,2,3]
输出：[]
 

提示：
1 <= N <= 100

前序遍历 根左右
dfs
全局遍历i指向voyage数组中下一个索引
如果当前节点的值与voyaga[i]的值不一致,返回False
左子树存在但不是想要的值的话交换左右子树,给它一次机会变成我们想要的值
比对到到最后root为空的话说明可以通过交换左右子树达到目的
"""

from utils.TreeNode import TreeNode, List2TN


class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res = []
        self.i = 0
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.i]:
                return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left,root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]


s = Solution()
root = List2TN([1, 2, 3, 4, 5])
voyage = [1, 3, 2, 5, 4]
print(s.flipMatchVoyage(root, voyage))
