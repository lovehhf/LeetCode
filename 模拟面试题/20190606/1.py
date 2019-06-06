# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        nums = sorted([(nums[i], i) for i in range(n)])
        i, j = 1, 0
        while i < n:
            while j < i and nums[j][0] != nums[i][0]:
                j += 1
            if any(abs(nums[i][1] - nums[x][1]) <= k for x in range(j, i)):
                return True
            i += 1
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        i, j = 0, 0
        while i < n:
            j = max(0, i - k)
            while j < i:
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2

s = Solution()
print(s.containsNearbyDuplicate(nums, k))
