# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = False
        if num < 0:
            flag = True
            num = -num
        num = int(num)
        m, n = num // 7, num % 7
        res = str(n)
        while m:
            m, n = m // 7, m % 7
            res = str(n) + res
        # print(int(res,7))
        return res if not flag else '-' + res


num = -100052566
s = Solution()
print(s.convertToBase7(num))
