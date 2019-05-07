# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请**不要使用除法**，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        p[i] 除第i个元素的前缀积
        q[i] 除第i个元素的后缀积
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        p = [1] * n
        q = [1] * n
        res = [1] * n
        for i in range(1, n):
            p[i] = p[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            q[i] = q[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = p[i] * q[i]
        return res

    def productExceptSelf2(self, nums):
        """
        使用常数空间实现
        变量t 存储前缀积和后缀积
        :param nums:
        :return:
        """
        n = len(nums)
        res = [1] * n
        t = 1
        for i in range(n):
            res[i] *= t
            t *= nums[i]
        t = 1
        for i in range(n - 1, -1, -1):
            res[i] *= t
            t *= nums[i]
        return res


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
