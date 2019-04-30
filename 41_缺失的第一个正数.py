# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        遍历一次数组把大于等于1的和小于等于数组大小的值放到原数组对应位置，
        然后再遍历一次数组查当前下标是否和值对应，如果不对应那这个下标就是答案，否则遍历完都没出现那么答案就是数组长度加1
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] >= 1 and nums[i] <= n and nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    i += 1
                else:
                    nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
                    # tmp = nums[nums[i]-1]
                    # nums[nums[i]-1] = nums[i]
                    # nums[i] = tmp
                # print(nums)
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            else:
                i += 1

        for i in range(1, n+1):
            if i != nums[i-1]:
                return i
        return n + 1

nums = [1,2,0]
s = Solution()
print(s.firstMissingPositive(nums))