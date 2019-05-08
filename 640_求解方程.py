# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。

如果方程没有解，请返回“No solution”。

如果方程有无限解，则返回“Infinite solutions”。

如果方程中只有一个解，要保证返回值 x 是一个整数。

示例 1：

输入: "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: "x=x"
输出: "Infinite solutions"
示例 3:

输入: "2x=x"
输出: "x=0"
示例 4:

输入: "2x+3x-6x=x+2"
输出: "x=-1"
示例 5:

输入: "x=x+2"
输出: "No solution"
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        以=分隔字符串 分别遍历 数字存入totalNum放右边,x系数存在totalX放左边，
        后来发现没必要这么麻烦,可以设置一个遍历equ_flag,表示在左边还是右边,直接一遍遍历
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        m, n = len(left), len(right)
        totalX, totalNum = 0, 0
        sign = 1
        tmp_num = 0
        for i in range(m):
            if ord('0') <= ord(left[i]) <= ord('9'):
                tmp_num = tmp_num * 10 + int(left[i])
                if i == m - 1:
                    totalNum += tmp_num * sign * -1
            elif left[i] == 'x':
                if tmp_num == 0 and (i == 0 or left[i - 1] == '+' or left[i - 1] == '-'):
                    totalX += sign
                else:
                    totalX += tmp_num * sign
                sign = 1
                tmp_num = 0
            elif left[i] == '-':
                totalNum += tmp_num * sign * -1
                sign, tmp_num =                                          -1, 0
            elif left[i] == '+':
                totalNum += tmp_num * sign * -1
                sign, tmp_num = 1, 0
        sign, tmp_num = 1, 0
        for i in range(n):
            if ord('0') <= ord(right[i]) <= ord('9'):
                tmp_num = tmp_num * 10 + int(right[i])
                if i == n - 1:
                    totalNum += tmp_num * sign
            elif right[i] == 'x':
                if tmp_num == 0 and (i == 0 or right[i - 1] == '+' or right[i - 1] == '-'):
                    totalX += sign * -1
                else:
                    totalX += tmp_num * sign * -1
                sign, tmp_num = 1, 0
            elif right[i] == '-':
                totalNum += sign * tmp_num
                sign, tmp_num = -1, 0
            elif right[i] == '+':
                totalNum += sign * tmp_num
                sign, tmp_num = 1, 0
        print(totalX, totalNum)
        if totalNum == 0 and totalX == 0:
            return "Infinite solutions"
        if totalX == 0:
            return "No solution"
        return "x=%s" % str(totalNum // totalX)


equation = "x-10=10-x+x+2x"
s = Solution()
print(s.solveEquation(equation))
