# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def mySqrt(x):
    # return int(x ** 0.5)

    # if x <= 1:
    #     return x
    # r = x
    # while r > x / r:
    #     r = (r + x / r) // 2
    # return int(r)

    # 二分
    res = 0
    l, r = 1, x
    if x == 0 or x == 1:
        return x
    while l <= r:
        mid = (l + r) // 2
        if mid == x / mid:
            return mid
        elif mid > x / mid:
            r = mid - 1
        else:
            l = mid + 1
            res = mid
    return res

print(mySqrt(4))