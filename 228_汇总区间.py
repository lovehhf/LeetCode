# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        双指针
        i:遍历到的当前元素
        j:从i开始与前一个元素差为1的最大区间的右边界
        时间复杂度O(n)
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            if j == i:
                res.append(str(nums[i]))
                i += 1
            else:
                res.append(str(nums[i]) + '->' + str(nums[j]))
                i = j + 1
        return res

nums = [0,2,3,4,6,8,9]
s = Solution()
print(s.summaryRanges(nums))