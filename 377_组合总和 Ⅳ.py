# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

致谢：
特别感谢 @pbrother 添加此问题并创建所有测试用例。
nums = [1, 2, 3]
target = 4


状态转移方程:
dp[i] = sum(dp[i-x] for x in nums)
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        if not nums or min(nums)>target:
            return 0
        nums = [x for x in nums if x<=target]
        nums.sort()
        dp = [0] * (target + 1)
        for num in nums:
            dp[num] = 1
        for i in range(nums[0] + 1, target + 1):
            dp[i] += sum(dp[i - x] for x in nums if i > x)
        print(dp)
        return dp[-1]

    def combinationSum42(self, nums, target):
        """
        超时
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(nums, target, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for num in nums:
                dfs(nums, target - num, path + [num], res)
        res = []
        dfs(nums, target, [], res)
        return len(res)


s = Solution()
nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
target = 10
print(s.combinationSum4(nums, target))
# for target in range(1, 15):
#     print(s.combinationSum42(nums, target))
