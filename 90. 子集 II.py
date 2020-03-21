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

dfs: 

1. 预排序
2. dfs 搜索, 递归到的所有的路径都是子集
3. 遇到 i > 0 && nums[i] == nums[i - 1] 的情况说明这个数不是第一遇到
   加上的话它的子集之前肯定在搜索 i - 1 的时候添加过, 剪枝
"""

from typing import List

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

class DFS_Solution:
    def dfs(self, nums, res, path):
        res.append(path)
        n = len(nums)
        for i in range(n):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[i + 1:], res, path + [nums[i]])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        self.dfs(nums, res, [])
        return res


nums = [1, 2, 2, 2]
s = Solution()
print(s.subsetsWithDup(nums))
