# -*- coding:utf-8 -*-

"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:
输入: [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。

注意:
给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。
"""

from typing import List


class Solution:
    def dfs(self, nums, arr, i, r) -> bool:
        """
        回溯
        :param nums: 火柴数组
        :param arr: 表明当前状态下每条边长的长度
        :param i: 当前搜索到的下标
        :param r: 正方形边长
        :return:
        """
        if all(x == r for x in arr):
            return True

        for j in range(4):
            if nums[i] + arr[j] > r:
                continue
            arr[j] += nums[i]
            if self.dfs(nums, arr, i + 1, r):
                return True
            arr[j] -= nums[i]  # 恢复现场
        return False

    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4 or sum(nums) & 3:
            return False

        r = sum(nums) >> 2
        print(r)
        arr = [0] * 4
        nums.sort(reverse=True)  # 逆序排序, 尽可能降低dfs深度
        return self.dfs(nums, arr, 0, r)


# 超时, 待优化
# class Solution:
#
#     def dfs(self, nums, i, u, k):
#         """
#         :param i: 当前搜索到的数
#         :param u: 已经搜索到的火柴
#         :return:
#         """
#         if u > self.r:
#             return False
#
#         if u == self.r:
#             # if k == 3:
#             #     return True
#             if k == 2:
#                 return True if sum(nums) & 3 else False
#             u = 0
#             k += 1
#
#         for j in range(len(nums)):
#             if self.dfs(nums[:i] + nums[i + 1:], j, u + nums[j], k):
#                 return True
#         return False
#
#     def makesquare(self, nums: List[int]) -> bool:
#         if len(nums) < 4:
#             return False
#
#         nums.sort(reverse=True)
#         s = sum(nums)
#         self.r = s // 4
#         if (s & 3 or any([x > self.r for x in nums])):
#             return False
#         return self.dfs(nums, 0, 0, 0)


nums = [5,5,5,5,4,4,4,4,3,3,3,3]
s = Solution()
print(s.makesquare(nums))
