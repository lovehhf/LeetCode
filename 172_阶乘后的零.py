# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        0-25:
        n//5
        25-125:
        n//5+n//25
        ...
        思路: 数n中含有5的幂次的个数之和就是答案，直观一点 answer = n//5+n//25 +n// 125 +n//625 + n//3125+.......
        :param n:
        :return:
        """
        count = 0
        """
        不断除以 5, 是因为每间隔 5 个数有一个数可以被 5 整除,
        然后在这些可被 5 整除的数中, 每间隔 5 个数又有一个可以被 25 整除, 故要再除一次, ... 
        直到结果为 0, 表示没有能继续被 5 整除的数了.
        """
        while n//5:
            count += n//5
            n //= 5
        return count

    # def trailingZeroes2(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     res = 1
    #     for i in range(1,n+1):
    #         res *= i
    #     return res

s = Solution()
print(s.trailingZeroes(125))