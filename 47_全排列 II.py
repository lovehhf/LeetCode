# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums,[],res)
        return res

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(set(permutations(nums)))


nums = [1, 1, 2]
s = Solution()
print(s.permuteUnique(nums))
