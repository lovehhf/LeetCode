# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
不使用运算符 + 和 -，计算两整数a 、b之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
"""


class Solution(object):
    def getSum(self, a: int, b: int) -> int:
        """
        a*b>=0 , or
        a < 0 and abs(a) > b > 0 (the negative number has a larger absolute value)
        b < 0 and abs(b) > a > 0
        :param a:
        :param b:
        :return:
        """
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a*b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)
        return add(a, b)  # a*b >= 0 or (-a) > b > 0

    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7fffffff
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1)
        return a if a <= MAX else ~(a ^ mask)

a = -2
b = 3
s = Solution()
print(s.getSum2(a,b))