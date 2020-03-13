# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""

from typing import List


class Solution:
    def find(self, nums, target):
        """
        二分查找nums中第一个 >= target 的索引
        """
        n = len(nums)
        l, r = 0, n - 1
        while (l < r):
            mid = (l + r) >> 1
            if (nums[mid] >= target):
                r = mid
            else:
                l = mid + 1
        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0x3f3f3f3f] * n  # 辅助数组, 只存最优的递增的子序列
        res = 0
        for i in range(n):
            j = self.find(f, nums[i])  # 找到第一个 >= nums[i] 的数并更新辅助数组
            f[j] = nums[i]
            res = max(res, j + 1)
        return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution()
print(s.lengthOfLIS(nums))
