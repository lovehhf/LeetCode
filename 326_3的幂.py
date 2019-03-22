# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
"""


def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    while n > 1:
        if n % 3 != 0:
            break
        n /= 3
    return n == 1
    
    # if n == 0:
    #     return False
    # if n == 1:
    #     return True
    # while n:
    #     if n%3:
    #         return False
    #     elif n/3==1:
    #         return True
    #     else:
    #         n = n//3
    # return False

print(isPowerOfThree(9*9))
