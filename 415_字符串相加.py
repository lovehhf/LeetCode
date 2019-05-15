# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        和第二题类似, 取长度大的用于循环能省很多麻烦
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        m, n = len(num1), len(num2)
        res = ''
        carry = 0
        for i in range(max(m, n)):
            n1 = ord(num1[i]) - ord('0') if i < m else 0
            n2 = ord(num2[i]) - ord('0') if i < n else 0
            s = n1 + n2 + carry
            carry, r = s // 10, s % 10
            res = str(r) + res
        if carry:
            res = str(carry) + res
        return res


num1 = "9999999"
num2 = "99889"

s = Solution()
print(s.addStrings(num1, num2))
