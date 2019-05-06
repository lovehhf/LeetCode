# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
子集2: 90
"""


class Solution:
    def subsets(self, nums):
        """
        从前往后遍历,遇到一个数则就把上一个的所有子集 加上该数组成新的子集
        [1]的子集: [[],[1]]
        [1,2]的子集: [[],[1]] + [[]+[2],[1]+[2]]

        dp[i] 前i个数的所有子集
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [[[]] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + [x + [nums[i - 1]] for x in dp[i - 1]]
        return dp[-1]

    def subsets2(self, nums):
        """
        节省空间
        dp[i]只与dp[i-1]有关
        所以只需要记录最后一个res就行了
        """
        res = [[]]
        for i in nums:
            res += [t + [i] for t in res]
        return res


nums = [1, 2, 3, 4]
s = Solution()
print(s.subsets(nums))
