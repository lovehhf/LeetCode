# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""


class Solution:
    def findMin(self, nums):
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) >> 1
            if mid == L:  # [2,1]
                return min(nums[L], nums[R])
            if nums[mid] > nums[L]:
                if nums[L] > nums[R]:
                    L = mid + 1
                else:
                    return nums[L]
            else:
                R = mid
        return nums[L]


nums = [2, 1]
s = Solution()
print(s.findMin(nums))
