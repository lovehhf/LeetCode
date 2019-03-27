# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # matrix[i] = ['Z']*n # 不能这么直接赋值 如果一行中有多个0 会出错
                    for t in range(n):
                        if matrix[i][t]!=0:
                            matrix[i][t] = 'Z'
                    for t in range(m): # 列
                        if matrix[t][j] != 0:
                            matrix[t][j] = 'Z'
                    continue
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'Z':
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        """
        旋转矩阵的骚方法
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zerolist = [set(), set()]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    zerolist[0].add(i)
                    zerolist[1].add(j)
        for i in zerolist[0]:
            matrix[i][:] = [0 for _ in range(len(matrix[i]))]
        matrix[:] = self.transpose(matrix)
        matrix[:] = self.invert(matrix)
        for i in zerolist[1]:
            matrix[i][:] = [0 for _ in range(len(matrix[i]))]
        matrix[:] = self.invert(matrix)
        matrix[:] = self.transpose(matrix)

    def transpose(self, field):
        """
        矩阵转置
        """
        return [list(row) for row in zip(*field)]

    def invert(self, field):
        """
        矩阵逆转（不是逆矩阵）
        将矩阵沿着纵轴翻转
        """
        return [row[::-1] for row in field]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
s = Solution()
s.setZeroes(matrix)
print(matrix)