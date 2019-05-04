# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
说明:

你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2。
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.dp = self.get_matrix_area()

    def get_matrix_area(self):
        """
        dp[i][j] 表示点到i-1,j-1这个点构成的矩形的面积
        :return:矩形中所有的点与原点构成的矩形的面积
        """
        if not self.matrix:
            return []
        m, n = len(self.matrix), len(self.matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 多出一行防越界
        # dp[0][0] = self.matrix[0][0]
        # for i in range(1, m):
        #     dp[0][i] = dp[0][i - 1] + self.matrix[0][i]
        # for i in range(1, n):
        #     dp[i][0] = dp[i - 1][0] + self.matrix[i][0]
        for i in range(0, m):
            for j in range(0, n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + self.matrix[i][j]
        # print(dp)
        return dp

    def sumRegion(self, row1, col1, row2, col2):
        """

        :param row1:
        :param col1:
        :param row2:
        :param col2:
        :return:
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        res = self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]
        return res

    def sumRegion2(self, row1, col1, row2, col2):
        """
        暴力解法 超时
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]
        return res


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

print(obj.sumRegion(1, 1, 2, 2))
