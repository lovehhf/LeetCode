# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


class Solution(object):
    def missingNumber(self, nums):
        """'
        使用异或
        0 ^ 4 = 4
        4 ^ 4 = 0
        不用求和，直接使用异或运算^进行 抵消，剩下的数字就是缺失的了。
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return nums[-1]+1

s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))