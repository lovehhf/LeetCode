# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

1.判断是否循环
2.寻找循环节
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        int_part, numerator = numerator // denominator, numerator % denominator
        if numerator == 0:
            return sign+str(int_part)
        dec_part = []
        d = {}
        i = 0
        while numerator != 0 and numerator not in d:
            d[numerator] = i
            numerator *= 10
            m, numerator = numerator // denominator, numerator % denominator
            dec_part.append(m)
            i += 1
        if numerator != 0:
            dec_part.insert(d[numerator], '(')
            dec_part.append(')')
        res = "%s%s.%s" % (sign, int_part, ''.join([str(x) for (x) in dec_part]))
        # print(res)
        # print(int_part,dec_part)
        return res


numerator, denominator = 1, -12345
s = Solution()
print(s.fractionToDecimal(numerator, denominator))
