# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。'
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""


class Solution(object):
    def rob(self, nums):
        """
        dp1: 从第一个房间开始偷
        dp2: 从第二个房间开始偷
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        if n <= 3:
            return max(nums)
        # dp1 = [0] * (n - 1)
        # dp2 = [0] * (n - 1)
        # dp1[0] = nums[0]
        # dp2[0] = nums[1]
        dp1 = self.helper(nums[:-1])
        dp2 = self.helper(nums[1:])
        return max(dp1, dp2)

    def helper(self, nums):
        """
        房子在是直线的情况
        dp1,dp2 边界的处理有一点麻烦 借助helper处理就简单很多
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


nums = [1, 2, 3, 1]
s = Solution()
print(s.rob(nums))
