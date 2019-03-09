# -*- coding:utf-8 -*-

__author__ = 'huanghf'

import re

# def test():
#     s = "112233"
#     print(re.findall(r'((.)\2)*', s))

def countAndSay(nums):
    s = '1'
    for _ in range(nums - 1):
        s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s))
    return s
print(countAndSay(10))

# test()