# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def isPalindrome(self, x):
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    return False