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


class Solution(object):
    def find_left_bonder(self, nums, target):
        """
        找左边界
        :param nums:
        :param target:
        :return:
        """
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) >> 1
            if nums[mid] < target:
                L = mid + 1
            else:
                R = mid
        return L

    def find_right_bonder(self, nums, target):
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R + 1) >> 1
            if nums[mid] <= target:
                L = mid
            else:
                R = mid - 1
        return L

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        left = self.find_left_bonder(nums, target)
        right = self.find_right_bonder(nums, target)
        return [left, right] if left <= right else [-1, -1]


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(s.searchRange(nums, target))
