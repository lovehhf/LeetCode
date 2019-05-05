# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出二叉搜索树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树的值之和，这个值应该大于或等于 node.val。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键小于节点键的节点。
节点的右子树仅包含键大于节点键的节点。
左右子树也必须是二叉搜索树。
 

示例：



输入：[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
输出：[30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
 

提示：

树中的节点数介于 1 和 100 之间。
每个节点的值介于 0 和 100 之间。
给定的树为二叉搜索树。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution:
    def __init__(self):
        self.s = 0

    def bstToGst(self, root):
        """
        累加树
        :param root:
        :return:
        """

        def helper(root):
            if not root:
                return
            helper(root.right)
            root.val += self.s
            self.s = root.val
            helper(root.left)

        helper(root)
        return root


root = List2TN([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
s = Solution()
res = TN2List(s.bstToGst(root))
print(res)
