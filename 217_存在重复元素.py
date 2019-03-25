# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

    def containsDuplicate_2(self, nums):
        """
        转为集合 长度不相等说明有相同的数
        """
        return len(nums) != len(set(nums))

    def containsDuplicate_3(self, nums):
        """
        排序后 遍历一遍数组
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

from timeit import timeit

sol = Solution()
print([1,1,1,3,3,4,3,2,4,2])

# time1 = timeit("Solution().containsDuplicate(nums=[1,5,6,3,3,4,3,2,4,2])",'from __main__ import Solution',number=10000)
# time2 = timeit("Solution().containsDuplicate_2(nums=[1,5,6,3,3,4,3,2,4,2])",'from __main__ import Solution',number=10000)
# time3 = timeit("Solution().containsDuplicate_3(nums=[1,5,6,3,3,4,3,2,4,2])",'from __main__ import Solution',number=10000)
#
# print(time1)
# print(time2)
# print(time3)
