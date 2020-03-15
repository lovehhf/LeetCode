# -*- coding:utf-8 -*-

"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def dfs(self, grid, vis, i, j):
        m, n = len(grid), len(grid[0])
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        res = 1
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            if (0 <= x < m and 0 <= y < n and not vis[x][y] and grid[x][y] == 1):
                vis[x][y] = 1
                res += self.dfs(grid, vis, x, y)  # 四个方向上的面积

        return res  # 返回从 (i, j) 开始最多能访问的岛屿面积

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]  # 访问过的岛屿, 不去直接修改原岛屿的数据

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    vis[i][j] = 1
                    res = max(res, self.dfs(grid, vis, i, j))

        return res
