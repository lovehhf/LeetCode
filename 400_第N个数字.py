# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 231)。

示例 1:
输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        for d in range(1, 10):
            if d * 9 * (10 ** (d - 1)) >= n:
                digit = d
                break
        num = 0
        for d in range(1, digit + 1):
            num += int(9 * (d - 1) * 10 ** (d - 2))
        ret = (n - num - 1) / digit + 10 ** (digit-1)
        return int(str(ret)[(n - num - 1) % digit])

    def findNthDigit2(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_n = range(1, n + 1)
        tmp = []
        for x in list_n:
            tmp += list(str(x))
        return tmp[n-1]

n = 10000000
s = Solution()
print(s.findNthDigit(n))