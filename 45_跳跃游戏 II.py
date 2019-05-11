# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。


定义两个指针last和i，数组f[i]表示到达i所需要的最少步数。
定义last为第一次到达i时上一步的位置，last从0开始。
"""


class Solution(object):
    def jump(self, nums):
        """
        max_dump 在第i个元素最远能跳到的距离
        dp[i]:跳到第i个元素最少需要多少步
        没用到动态规划
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        n = len(nums)
        dp = [0] * n
        max_dump = nums[0]
        dp[0] = 0
        dp[1:max_dump + 1] = [1] * max_dump
        if max_dump >= n - 1:
            return 1
        for i in range(1, n):
            if i + nums[i] >= n - 1:
                return dp[i] + 1
            if i + nums[i] > max_dump:
                dp[max_dump + 1:i + nums[i] + 1] = [dp[i] + 1] * (i + nums[i] - max_dump)
                max_dump = i + nums[i]
        return dp[-1]

    def jump2(self, nums):
        """
        优化代码
        与上面不同的是,这是根据i更新last,上面是根据num[i]和i的和判断是不是能跳过前面跳得最大值。

        f[i]: 到达i所需要的最少步数
        last: 第一次到达i时上一步的位置
        根据贪心得知，令f[i]=f[last]+1后，f[i]就会是最优值。
        故可以根据i来让last向后移动，找到最早得可以一步到达i的位置，然后根据f[last]更新f[i]。
        :param nums:
        :return:
        """
        n = len(nums)
        f = [0] * n
        last = 0
        for i in range(1, n):
            # print(i, f, last)
            while i > last + nums[last]:
                last += 1
            f[i] = f[last] + 1
        return f[n - 1]


nums = [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 4]
s = Solution()
print(s.jump(nums))
