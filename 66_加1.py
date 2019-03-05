# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def plusOne(digits):
    sum, res = 0, 0
    for i, v in enumerate(reversed(digits)):
        sum += v * 10 ** i
    res = sum + 1
    return list(map(int, list(str(res))))
    # return list(map(int, list(str(int(''.join(list(map(str,digits))))+1))))

print(plusOne(99))