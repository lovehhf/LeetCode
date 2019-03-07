# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for i in range(0, n - 1):
        a, b = b, a + b
    return a