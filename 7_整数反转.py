# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        if ((x<(-2**31)) or (x>(2**31-1))):
            return 0
        else:
            str_x = str(x)
            list_x = list(str_x)
            if list_x[0]=='-':
                result = int('-'+''.join((list(reversed(list_x[1:])))))
            else:
                result = int(''.join((list(reversed(str_x)))))
            if ((result<(-2**31)) or (result>(2**31-1))):
                return 0
            return result

s = Solution()
print(s.reverse(-123))