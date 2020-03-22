# -*- coding:utf-8 -*-

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
     偷窃到的最高金额 = 1 + 3 = 4
"""

from typing import List


class Solution:
    def rob_help(self, nums):
        """
        考虑是直线的情况下, 最多能偷到多少钱 (打家劫舍1)
        :param nums:
        :return:
        """
        n = len(nums)
        f = [0] * (n + 2)

        for i in range(2, n + 2):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 2])

        return f[n + 1]

    def rob(self, nums: List[int]) -> int:
        """
        断环: 只考虑 0 ~ n-1 和 1 ~ n 这两部分
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_help(nums[:-1]), self.rob_help(nums[1:]))


nums = [1, 2, 3, 1]
s = Solution()
print(s.rob(nums))
