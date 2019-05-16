# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1" 1,1,+
输出: 2
示例 2:

输入: " 2-1 + 2 " -> 2,1,-,2,+
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)" ->1,4,5,+,2,+,+,3,-,6,8,+,+
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

开两个栈，一个记录数字，一个记录操作符。
然后从前往后扫描整个表达式：
如果遇到 (、+、-，直接入栈；
如果遇到数字，则判断操作符栈的栈顶元素，如果不是 (，则弹出操作符的栈顶元素，并用相应操作更新数字栈的栈顶元素。
从而保证操作符栈的栈顶最多有一个连续的+或-；
如果遇到 )，此时操作符栈顶一定是 (，将其弹出。然后根据新栈顶的操作符，对数字栈顶的两个元素进行相应操作；
"""


class Solution(object):
    def calc(self, nums, ops):
        op = ops.pop()
        a = nums.pop()
        b = nums.pop()
        if op == '+':
            nums.append(b + a)
        else:
            nums.append(b - a)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        n = len(s)
        ops = []
        nums = []
        i = 0
        while i < n:
            if '0' <= s[i] <= '9':
                j = i + 1
                while j < n and '0' <= s[j] <= '9':
                    j += 1
                nums.append(int(s[i:j]))
                i = j
                if ops and ops[-1] != '(':
                    self.calc(nums, ops)
            elif s[i] == '(' or s[i] == '+' or s[i] == '-':
                ops.append(s[i])
                i += 1
            elif s[i] == ')':
                ops.pop()
                if ops and ops[-1] != '(':
                    self.calc(nums, ops)
                i += 1
        return nums[-1]


s = Solution()
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
