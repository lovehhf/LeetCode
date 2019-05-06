# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
子集一: 78
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
        如果nums[i]==nums[i-1],不需要添加所有的子集都+nums[i],只需要添加上一次新创建的子集
        使用cur记录这个新创建的子集
        # 1,2,2,2 -> [],[1] -> [],[1] + [2],[1,2] -> [],[1],[2],[1,2] + [2,2],[1,2,2] -> [],[1],[2],[1,2],[2,2],[1,2,2] + [2,2,2],[1,2,2,2]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res, cur = [[]], []
        for i in range(n):
            if nums[i] != nums[i - 1] or i == 0:
                cur = [x + [nums[i]] for x in res]
            else:
                # 使用cur列表记录上一次新创建的数组
                cur = [x + [nums[i]] for x in cur]
            res += cur
        return res

    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [[[]] for _ in range(n)]
        dp[0] = [[], [nums[0]]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                dp[i] = dp[i - 1] + [x + [nums[i]] for x in dp[i - 1]]
            else:
                # 这么去重有点太暴力了
                dp[i] = dp[i - 1] + [x + [nums[i]] for x in dp[i - 1] if not (x + [nums[i]]) in dp[i - 1]]
        return dp[-1]


nums = [1, 2, 2, 2]
s = Solution()
print(s.subsetsWithDup(nums))
