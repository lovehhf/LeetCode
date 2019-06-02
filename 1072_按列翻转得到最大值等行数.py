# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的 每个 单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。

返回经过一些翻转后，**行上所有值都相等的最大行数**。

 

示例 1：

输入：[[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。
示例 2：

输入：[[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。
示例 3：

输入：[[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。
 

提示：

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
所有 matrix[i].length 都相等
matrix[i][j] 为 0 或 1
"""

import collections


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        count = collections.Counter(tuple(x ^ r[0] for x in r) for r in matrix)
        print(count)
        return max(count.values())

    # def maxEqualRowsAfterFlips(self, matrix):
    #     """
    #     超时
    #     :type matrix: List[List[int]]
    #     :rtype: int
    #     """
    #     res = 0
    #     m, n = len(matrix), len(matrix[0])
    #     vis = set()
    #     for i in range(m):
    #         if i in vis:
    #             continue
    #         t = 1
    #         for j in range(i + 1, m):
    #             if all(matrix[i][x] != matrix[j][x] for x in range(n)) or all(matrix[i][x]==matrix[j][x] for x in range(n)):
    #                 t += 1
    #                 vis.add(j)
    #         res = max(res, t)
    #     return res
    #
    # def maxEqualRowsAfterFlips2(self, matrix):
    #     """
    #     超时
    #     :type matrix: List[List[int]]
    #     :rtype: int
    #     """
    #     res = 0
    #     m, n = len(matrix), len(matrix[0])
    #     r = [set() for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j]:
    #                 r[i].add(j)
    #     s = {x for x in range(n)}
    #     vis = set()
    #     for i in range(m):
    #         t = 0
    #         if i in vis:
    #             continue
    #         for j in range(i + 1, m):
    #             if (r[i] == r[j] or r[j] == s - r[i]):
    #                 vis.add(j)
    #                 t += 1
    #         res = max(t + 1, res)
    #     # print(res)
    #     return res


s = Solution()
matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(s.maxEqualRowsAfterFlips(matrix))
# print(s.maxEqualRowsAfterFlips2(matrix))
