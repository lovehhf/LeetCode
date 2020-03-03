# -*- coding:utf-8 -*-

"""
给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。

示例 1：
输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""

import collections
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = collections.defaultdict(list)

        for x in range(m):
            for y in range(n):
                d[x - y].append(mat[x][y])

        for v in d.values():
            v.sort()

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            x, y = i, 0
            cur = 0
            while x < m and y < n:
                res[x][y] = d[i][cur]
                x += 1
                y += 1
                cur += 1
        for j in range(1, n):
            x, y = 0, j
            cur = 0
            while x < m and y < n:
                res[x][y] = d[-j][cur]
                x += 1
                y += 1
                cur += 1

        return res
