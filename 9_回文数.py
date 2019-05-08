# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        反转整数 如果反转后到一半出现反转后一半与前一半相等(abba型)或者等于前一半整除10则是回文串(aba型)
        121 -> 12,1
        1221 -> 12,21
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        s = 0
        while s <= x:
            y = x % 10
            s = s * 10 + y
            if s == x // 10 or s == x:
                return True
            x //= 10
        return False

    def isPalindrome2(self, x):
        """
        转字符串处理
        :param x:
        :return:
        """
        return str(x) == str(x)[::-1]


x = 12121
s = Solution()
print(s.isPalindrome(x))
print(s.isPalindrome2(x))
