# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

84_柱状图中最大的矩形 升级版
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        枚举每个元素能向上延时的最大高度
        根据84. 柱状图中最大的矩形,使用单调栈求出每个元素能够向右延伸的最大宽度
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        M = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and matrix[i][j] == '1':
                    M[i][j] = 1
                if i > 0 and matrix[i][j] == '1':
                    M[i][j] = M[i - 1][j] + 1
        # for i in M:
        #     print(i)
        res = 0
        for line in M:
            stack = []
            for i in range(n + 1):
                while stack and line[stack[-1]] > line[i]:
                    h = line[stack.pop()]
                    l = i - stack[-1] - 1 if stack else i
                    res = max(h * l, res)
                stack.append(i)
        return res


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
print(s.maximalRectangle(matrix))
