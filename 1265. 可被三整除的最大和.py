# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。

 

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 

提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if (s % 3 == 0):
            return s
        nums.sort()
        a = []
        b = []
        for i in nums:
            if (i % 3 == 1 and len(a) < 2):
                a.append(i)
            if (i % 3 == 2 and len(b) < 2):
                b.append(i)
            if (len(a) > 1 and len(b) > 1):
                break
        if (s % 3 == 1):
            if (len(b) == 2):
                return s - min(sum(b), a[0])
            else:
                return s - a[0]
        else:
            if (len(a) == 2):
                return s - min(sum(a), b[0])
            else:
                return s - b[0]
