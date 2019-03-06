# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def removeDuplicates(nums):
    """
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

    数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。
    :param nums:
    :return:
    """
    n = len(nums)
    i = 0
    if not nums:
        return 0
    for j in range(1,n):
        if nums[j]!=nums[i]:
            i += 1
            nums[i] = nums[j]
    return i+1,nums

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))