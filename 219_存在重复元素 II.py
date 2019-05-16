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
        """
        时间复杂度 O(n) 空间复杂度O(n)
        从左往右遍历列表
        如果列表中的数在字典中有记录 则比对它们的索引差是否小于等于k
        如果小于等于k 说明存在这样的i,j
        :param nums: list
        :param k: int
        :return: bool
        """
        n = len(nums)
        d = {}
        for i in range(n):
            v = nums[i]
            if d.get(v)!=None and i-d.get(v)<=k:
                return True
            d[v] = i
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        时间复杂度O(n^2)
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if k < n:
            for i in range(n):
                for j in range(i + 1, i + k + 1):
                    if j > n - 1:
                        continue
                    if nums[i] == nums[j]:
                        return True
            return False
        return n > len(set(nums))


nums = [1, 2, 3, 1, 2, 3]
k = 2

# nums = [1,2,3,1,2,3]
# k = 2
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
