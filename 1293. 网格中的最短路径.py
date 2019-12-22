# -*- coding:utf-8 -*-

"""
给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

 

示例 1：

输入：
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

示例 2：

输入：
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。
 

提示：

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0

与 864 很像
"""

from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        :param grid:
        :param k:
        :return:
        """
        m, n = len(grid), len(grid[0])
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(0, 0, 0, 0)]
        # visited x,y,t保存搜索状态，(x, y)表示位置，t表示经过了t个障碍物的状态
        visited = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        visited[0][0][0] = 1

        while queue:
            i, j, t, s = queue.pop(0)  # 经过了t个障碍物, s: 从(0,0)到(i, j)走了多少步
            for dx, dy in ds:
                x = i + dx
                y = j + dy

                if (0 <= x < m and 0 <= y < n and not visited[x][y][t]):

                    if grid[x][y] == 0:
                        visited[x][y][t] = 1

                        if (x == m - 1 and y == n - 1):
                            return s + 1

                        queue.append((x, y, t, s + 1))

                    if grid[x][y] == 1 :
                        visited[x][y][t] = 1
                        if t < k:
                            queue.append((x, y, t + 1, s + 1))

        return 0 if m == 1 and n == 1 else -1

s = Solution()
grid =[[0,1,1],[1,1,1],[1,0,0]]

k = 1
print(s.shortestPath(grid, k))
