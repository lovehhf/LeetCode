# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):

    def combine(self, n, k):
        """
        dfs
        :param n:
        :param k:
        :return:
        """

        def dfs(nums, u, res, path):
            if u == k:
                res.append(path)
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[i + 1:], u + 1, res, path + [nums[i]])

        res = []
        nums = list(range(1, n + 1))
        dfs(nums, 0, res, [])
        return res

    def combine3(self, n, k):
        """
        回溯
        :param n:
        :param k:
        :return:
        """
        def backtracking(n, k, t, res, path):
            if len(path) == k:
                import copy
                tmp = copy.copy(path)
                res.append(tmp)
                return
            else:
                for i in range(t, n + 1):
                    path.append(i)
                    backtracking(n, k, i + 1, res, path)
                    path.pop()

        res,path = [],[]
        backtracking(n, k, 1, res, path)
        return res

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return list(combinations(list(range(1, n + 1)), k))


n, k = 4, 2
s = Solution()
print(s.combine3(n, k))
