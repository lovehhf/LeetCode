# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution(object):
    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates,target,0,res,[])
        return res

        # for i in range(1,target+1):
        #     for num in candidates:
        #         if num > i:
        #             break
        #         if num == i:
        #             dp[i] += [[num]]
        #         else:
        #             for j in dp[i-num]:
        #                 dp[i] += [j + [num]]
        #     dp[i] = [list(x) for x in set([tuple(x) for x in dp[i]])]
        #     # print(dp[i])
        # print(dp)
        # return dp[target]


candidates = [10, 1, 2, 7, 6, 1, 5, 1]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))
