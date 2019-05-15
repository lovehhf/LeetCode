# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

1013. 将数组分成和相等的三个部分 升级款

dfs:
直接dfs找所有路径一定会超时(27/104)
需要改进一下,只递归找是不是存在一条路径的和为target,存在的话就直接返回(超时+1,53/104 )
再改进一下,增加剪枝策略,对nums排序,然后遍历,如果出现数字与上一个相同,直接遍历下一个数字(类似于全排列2) AC,500ms (canPartition2)
再改进一下,使用字典统计每个数字出现的频率,遍历字典,先把数字统计频率-1,递归,无解的话回溯(AC,500ms canPartition)

dp: 01背包问题
https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
背包容量(v)=sum/2
首先考虑二维dp: 
dp[i][j]表示j是否可以从前i个数中取到,如果能在前i个数中取出一系列的数和为j则dp[i][j]为True,否则为False
状态转移方程:
对于每一个数字,可以选择取或者不取它
如果不取nums[i],则dp[i][j] = dp[i-1][j] 表示看dp[i-1][j]能否凑出j,
如果取了nums[i] 则dp[i][j] = dp[i-1][j-nums[i]]
所以状态转移方法是j>nums[i]: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]], j<nums[i]: dp[i-1][j]

优化为一维dp: 
dp[i]表示能否填满容量为i的背包
"""


class Solution(object):
    def canPartition(self, nums):
        """
        回溯
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(d, target):
            if target < 0:
                return
            if target == 0:
                return True
            for key, value in d.items():
                if value == 0:
                    continue
                d[key] -= 1
                if dfs(d, target - key):
                    return True
                d[key] += 1
            return False

        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        if target in nums:
            return True
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        res = dfs(d, target)
        return res

    def canPartition2(self, nums):
        """
        dfs
        :param nums:
        :return:
        """

        def dfs(nums, target):
            if target < 0:
                return
            if target == 0:
                return True
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    if dfs(nums[:i] + nums[i + 1:], target - nums[i]):
                        return True
            return False

        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        nums.sort()
        res = dfs(nums, target)
        return res

    def canPartition3(self, nums):
        """
        01背包问题
        :param nums:
        :return:
        """
        if sum(nums) & 1:
            return False
        v = sum(nums) // 2
        n = len(nums)
        dp = [[0] * (v + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
        for i in range(1, v + 1):
            dp[0][i] = 0
        for i in range(1, n + 1):
            for j in range(1, v + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] | dp[i - 1][j - nums[i - 1]]
        return dp[n][v] == 1

    def canPartition4(self, nums):
        """
        01背包的空间优化
        :param nums:
        :return:
        """
        if sum(nums) & 1:
            return False
        v = sum(nums) // 2
        dp = [0] * (v + 1)
        dp[0] = 1
        for num in nums:
            for i in range(v, 0, -1):
                if i >= num:
                    dp[i] = dp[i] | dp[i - num]
        print(dp)
        return dp[v] == 1


nums = [1,5,5,11]
s = Solution()
print(s.canPartition(nums))
print(s.canPartition2(nums))
print(s.canPartition3(nums))
print(s.canPartition4(nums))
