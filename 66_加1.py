# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        res = [0] * (n)
        if digits[-1] == 9:
            res[-1] = 0
            carry = 1
        else:
            digits[-1] = digits[-1] + 1
            return digits
        for i in range(n - 2, -1, -1):
            carry, res[i] = (digits[i] + carry) // 10, (digits[i] + carry) % 10
        if carry:
            return [1] + res
        else:
            return res

    def plusOne2(self, digits):
        sum, res = 0, 0
        for i, v in enumerate(reversed(digits)):
            sum += v * 10 ** i
        res = sum + 1
        return list(map(int, list(str(res))))
        # return list(map(int, list(str(int(''.join(list(map(str,digits))))+1))))


digits = [1, 2, 3]
s = Solution()
print(s.plusOne(digits))
