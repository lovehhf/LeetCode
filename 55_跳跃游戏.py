# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""


class Solution:
    def canJump(self, nums):
        """
        从后往前遍历数组，如果遇到的元素可以到达最后一行，则截断后边的元素。
        否则继续往前，若最后剩下的元素大于1个，则可以判断为假。否则就是真，时间复杂度O(n)
        :param nums:
        :return:
        """
        n = 1
        for i in range(len(nums) - 2, -1, -1):
            print(n)
            if nums[i] >= n:
                n = 1
            else:
                n += 1
        if n > 1:
            return False
        return True

    def canJump3(self, nums):
        """
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        max_length = 0  # 最远能调到的地方
        for i in range(0, n):
            if not dp[i]:
                return False
            if i + nums[i] >= n - 1:
                return True
            if i + nums[i] > max_length:
                for j in range(max_length, nums[i] + i + 1):
                    dp[j] = 1
                max_length = i + nums[i]

            # if i + nums[i] > max_length:
            #     max_length = i + nums[i]
            #     for j in range(nums[i]+1):
            #         dp[i+j] = 1

    def canJump2(self, nums):
        """
        超时
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(0, n):
            if not dp[i]:
                return False
            if i + nums[i] >= n - 1:
                return True
            for j in range(nums[i] + 1):
                dp[i + j] = 1
        return True


nums = [0]
s = Solution()
print(s.canJump(nums))
