# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""


def singleNumber(nums):
    a = 0
    for num in nums:
        a ^= num    # 亦或的巧妙运用 相同为0 不同为1
        print(a)
    return a

print(singleNumber([4,1,2,1,2]))