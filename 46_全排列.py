# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        """
        深度优先搜索
        :param nums:
        :param path:
        :param res:
        :return:
        """
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def permute2(self, nums):
        """
        递归
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        if n <= 1:
            return [nums]
        for i in range(n):
            s = nums[:i] + nums[i + 1:]
            p = self.permute(s)
            for x in p:
                res.append([nums[i]] + x)
        return res

    def permute3(self, nums):
        """
        one line
        :param nums:
        :return:
        """
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

nums = [1, 2, 3]
s = Solution()
print(s.permute2(nums))
