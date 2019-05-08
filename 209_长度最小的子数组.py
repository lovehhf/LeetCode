# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        滑动窗口
        如果窗口内的和>=s 窗口左边界右移,更新res,直到窗口内的和不再大于等于s
        然后窗口右边界右移
        :param s: 
        :param nums: 
        :return: 
        """
        n = len(nums)
        L, R = 0, 0  # 滑动窗口左右边界
        total = 0    # 窗口内的和
        res = n + 1
        while R < n:
            total += nums[R]
            while total >= s:
                res = min(res, R - L + 1)
                total -= nums[L]
                L += 1
            R += 1
        return res if res < n + 1 else 0

    def minSubArrayLen2(self, s, nums):
        """
        想错了 应该用滑动窗口
        超时
        ls[i] 前i-1个数组的前缀和
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or min(nums) > s or sum(nums) < s:
            return 0
        n = len(nums)
        ls = nums  # 前缀和
        for i in range(1, n):
            ls[i] += ls[i - 1]
        ls = [0] + ls
        res = n
        for i in range(n, -1, -1):
            for j in range(i):
                if ls[i] - ls[j] >= s:
                    # print(i, j)
                    res = min(res, i - j)
                else:
                    break
        return res


s = 5
nums = [2, 3, 1, 1, 1, 1, 1]
sol = Solution()
print(sol.minSubArrayLen(s, nums))
