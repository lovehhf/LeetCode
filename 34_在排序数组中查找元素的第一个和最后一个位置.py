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
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        L, R = 0, len(nums) - 1
        # 先二分一次找到最左边的 target
        # 再二分一次找最右边的 target
        while L < R:
            mid = (L + R) >> 1
            if nums[mid] < target:
                L = mid + 1
            else:
                R = mid

        if nums[L] != target:
            return [-1, -1]
        left = L  # 记录最左边的
        # 再次二分找最右边的target
        L, R = L, len(nums) - 1

        # 使用L+1可以避免死循环
        # while L + 1 < R:
        #     mid = (L + R) >> 1
        #     if nums[mid] == target:
        #         L = mid
        #     else:
        #         R = mid - 1
        while L < R:
            mid = (L + R + 1) >> 1 # mid 落在右边
            if nums[mid] == target:
                L = mid
            else:
                R = mid - 1
        # if L + 1 < len(nums) and nums[L + 1] == target:
        #     return [left, L + 1]

        return [left, R]

    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) >> 1
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                # 不符合要求
                # low, high = mid, mid
                # while low >= L and nums[low] == target:
                #     low -= 1
                # while high <= R and nums[high] == target:
                #     high += 1
                # return low + 1, high - 1

                #
                # if len(nums) == 2:
                #     if nums[-1] == target:
                #         return [0,1]
                #     else:
                #         return [0,0]

                ##### 处理边界烦死了 没写出来
                # (L,mid) (mid,R) 区间再分别二分找出边界
                LL, RR = mid, mid
                while L < LL:
                    m = (L + LL) >> 1
                    if nums[m] < target:
                        L = m + 1
                    else:
                        LL = m

                while RR < R:
                    print(RR,R)
                    m = (R + RR + 1) >> 1
                    if nums[m] > target:
                        R = m - 1
                    else:
                        RR = m
                return [L, R]
        return [-1, -1]

    def searchRange3(self, nums, target):
        if nums and (target<nums[0] or target>nums[-1]):
            return [-1,-1]
        l = bisect.bisect_left(nums,target)
        r = bisect.bisect_right(nums,target) - 1
        return [l,r] if l<=r else [-1,-1]


s = Solution()
nums = [1]
target = 1
print(s.searchRange(nums, target))
print(s.searchRange3(nums, target))
