# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
示例：
输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
 
提示：

树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5
"""

from utils.TreeNode import List2TN


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, level_sum_max, res = 0, 0, 0
        queue = [root]
        while queue:
            q = []
            level_sum = 0
            level += 1
            while queue:
                cur = queue.pop(0)
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            queue = q
            if level_sum > level_sum_max:
                res = level
                level_sum_max = level_sum
        return res


root = List2TN([989, None, 10250, 98693, -89388, None, None, None, -32127])
s = Solution()
res = s.maxLevelSum(root)
print(res)
