# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def computer(nums, ops):
            x = nums.pop()
            y = nums.pop()
            op = ops.pop()
            if op == '*':
                nums.append(x * y)
            elif op == '/':
                nums.append(y // x)
            elif op == '+':
                nums.append(x + y)
            else:
                nums.append(y - x)
        if not s:
            return 0
        nums = []
        ops = []
        i = 0
        n = len(s)
        while i < n:
            if '0' <= s[i] <= '9':
                j = i + 1
                while j < n and '0' <= s[j] <= '9':
                    j += 1
                nums.append(int(s[i:j]))
                if ops and (ops[-1] == '*' or ops[-1] == '/'):
                    computer(nums, ops)
                i = j - 1
            if s[i] in '+-*/':
                ops.append(s[i])
            i += 1
        # print(nums, ops)
        # while ops:
        #     computer(nums, ops)
        res = nums[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                res += nums[i + 1]
            else:
                res -= nums[i + 1]
        return res


s = " 1 -3 *5* 3 + 1 "
sol = Solution()
print(sol.calculate(s))
