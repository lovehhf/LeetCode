# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return [l, r - 1] if l < r else [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 4
s = Solution()
print(s.searchRange(nums, target))
