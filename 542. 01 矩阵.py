# -*- coding:utf-8 -*-

"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0

示例 2:
输入:
0 0 0
0 1 0
1 1 1
输出:
0 0 0
0 1 0
1 2 1

注意:
给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

多源最短路问题， 和 1162. 地图分析 类似
"""

import collections
from typing import  List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque([])
        res = [[0] * n for _ in range(m)]
        vis = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == 0):
                    vis[i][j] = 1
                    queue.append((i, j, 0))

        while (queue):
            i, j, s = queue.popleft()
            for dx, dy in ds:
                x = i + dx
                y = j + dy
                if (x < 0 or x >= m or y < 0 or y >= n or vis[x][y] != 0):
                    continue

                if matrix[x][y] == 1:
                    res[x][y] = s + 1
                    vis[x][y] = 1
                    queue.append((x, y, s + 1))
        return res



s = Solution()
matrix = [[0, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
print(s.updateMatrix(matrix))