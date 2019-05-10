# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        dp[i][j] i,j为正方形右下角能构成的最大正方形边长
        状态转移方程: dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return max(max(x) for x in dp) ** 2

    def maximalSquare2(self, matrix):
        """
        逻辑写复杂了。
        dp[i][j]:i,j能构成的最大正方形边长
        遍历矩阵 当[i][j]是1的时候,看[i-k,j-k]是不是正方形,如果是的话 检查(i,j-k)和(i-k,j)到i,j是不是都是1 是的话 更新dp[i][j]
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j]:
                    k = 1
                    while i - k >= 0 and j - k >= 0 and dp[i - k][j - k]:
                        if all(dp[i][j - x] for x in range(1, k + 1)) and all(dp[i - x][j] for x in range(1, k + 1)):
                            dp[i][j] = min(k + 1, dp[i - 1][j - 1] + 1)
                        k += 1
        res = max(max(x) for x in dp) ** 2
        return res


matrix = [["0", "1", "1", "0", "1"],
          ["1", "1", "0", "1", "0"],
          ["0", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "1"],
          ["0", "0", "0", "0", "0"]]
s = Solution()
print(s.maximalSquare(matrix))
