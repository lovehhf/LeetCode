# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        dfs 回溯
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(nums, u, path, res, target):
            """
            :param nums: 搜索的数组
            :param u: 已经搜索的路径数量，==k 时结束搜索
            :param path: 搜索的路径
            :param res: 结果列表
            :param target: 目标值,n
            :return:
            """
            if target < 0:
                return
            if target == 0 and u == k:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i + 1:], u + 1, path + [nums[i]], res, target - nums[i])

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        dfs(nums, 0, [], res, n)
        return res


s = Solution()
k = 3
n = 9
print(s.combinationSum3(k, n))
