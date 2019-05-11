# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

回溯+去重
"""


class Solution(object):
    def dfs(self, nums, target, index, res, path):
        """
        :param nums: candidates数组
        :param target:目标值
        :param index: 当前搜索到的索引
        :param res: 存放结果数组
        :param path: 走过的路径
        :return:
        """
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])

    def dfs2(self, nums, target, path, res):
        # print(nums, target, path)
        if target < 0:
            return
        if target == 0:
            # print(path)
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs2(nums[i + 1:], target - nums[i], path + [nums[i]], res)  # 不使用索引 而使用Python的切片操作剪枝

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = [x for x in candidates if x <= target]
        candidates.sort()
        res = []
        # self.dfs(candidates, target, 0, res, [])
        self.dfs2(candidates, target, [], res)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5, 1]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))
