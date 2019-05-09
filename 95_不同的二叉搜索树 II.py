# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


以n=5为例,枚举12345这五个根节点
1: 左:空  右:[2,3,4,5]组成的二叉搜索树
2: 左:[1] 右:[3,4,5]组成的二叉搜索树
3: 左:[1,2]组成的二叉搜索树, 右:[4,5]组成的二叉搜索树
4: 左:[1,2,3]组成的二叉搜索树,右:[5]
5: 左:[1,2,3,4]组成的二叉搜索树,右:空

定义函数helper(nums):作用为为给定的有序数组生成所有二叉搜索树
"""

from utils.TreeNode import TreeNode, TN2List, List2TN

import copy

class Solution(object):
    def helper(self, nums):
        """
        递归生成给定有序数组能组成的所有二叉搜索树
        :param nums:
        :return:
        """
        if not nums:
            return [None]
        n = len(nums)
        if n == 1:
            return [TreeNode(nums[0])]
        tns = []
        for i in range(n):
            lefts = self.helper(nums[:i])
            rights = self.helper(nums[i + 1:])
            for l in lefts:
                for r in rights:
                    # append传入的是root引用,如果root定义放上面的话,在这里root被修改的话前面append的也会被修改,所以要么root放在这里,要么放上面,append的时候使用copy(root)
                    root = TreeNode(nums[i])
                    root.left = l
                    root.right = r
                    tns.append(copy.copy(root))
        return tns

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        nums = list(range(1, n + 1))
        for i in range(n):
            root = TreeNode(nums[i])
            lefts = self.helper(nums[:i])
            rights = self.helper(nums[i + 1:])
            for l in lefts:
                for r in rights:
                    root.left = l
                    root.right = r
                    res.append(copy.copy(root))   # root定义放在上面的情况需要copy 不然会出Bug
        return res


n = 4
s = Solution()

print([TN2List(x) for x in s.helper([2,3])])

# print(s.generateTrees(n))
tns = [TN2List(x) for x in s.generateTrees(n)]
print(tns)
