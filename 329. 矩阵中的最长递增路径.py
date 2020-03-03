# -*- coding:utf-8 -*-

"""
给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:
输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。

示例 2:
输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

解题思路:
1. 暴力 dfs  -> 超时

2. 记忆化搜索
   给 dfs 加缓存, 已经搜索过的不再重复搜索

3. 拓扑排序

"""

from typing import List


class Solution:

    def dfs(self, i, j):
        if self.cache[i][j] != 0:
            return self.cache[i][j]

        count = 1

        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            x = i + dx
            y = j + dy

            if 0 <= x < m and 0 <= y < n and self.matrix[x][y] > self.matrix[i][j]:
                count = max(count, self.dfs(x, y) + 1)  # 取所有可行路径的最大值

        self.cache[i][j] = count
        return count

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        global m, n

        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix

        res = 0
        self.cache = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j))

        return res


s = Solution()
nums = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

print(s.longestIncreasingPath(nums))
