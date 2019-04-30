# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # 回溯
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

    def combinationSum(self, candidates, target):
        """
        dp[i]: target为i时的解
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[[]]] + [[] for _ in range(target)]
        for i in range(1, target + 1):
            for num in candidates:
                if num > i:
                    break
                elif num == i:
                    dp[i] += [[num]]
                else:
                    for j in dp[i - num]:
                        if num >j[0]:
                            continue
                        else:
                            dp[i] += [[num] + j]
                        # if not j or num >= j[-1]:
                        #     dp[i] += [j + [num]]
        return dp[target]

        # 三维数组，记录每个和对应的最终结果
        # dp = []
        # candidates.sort()

        # cur代表这个下标，也就是这个和，所以从1开始
        # for cur in range(1, target + 1):
        #     conbinations = []
        #     for num in candidates:
        #         if num > cur:
        #             break
        #         elif num == cur:
        #             conbinations.append([cur])
        #             break
        #         else:
        #             # 减去1是因为下标的关系
        #             for conbination in dp[cur - num - 1]:
        #                 if num > conbination[0]:
        #                     continue
        #                 conbinations.append([num] + conbination)
        #     dp.append(conbinations)
        #
        # print(dp)
        # return dp[target - 1]


candidates = [2, 3, 5]
target = 10
s = Solution()
print(s.combinationSum2(candidates, target))
