# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在给定的网格中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：
输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

示例 3：
输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

提示：
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2

链接: https://leetcode-cn.com/problems/rotting-oranges/
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        带状态的 bfs
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 初始队列
        queue = [[i, j, 0] for i in range(m) for j in range(n) if grid[i][j] == 2]
        res = 0

        while queue:
            i, j, res = queue.pop(0)  # i, j 存储已经传染的橘子的坐标, res 表示当前已经经过的时间
            for dx, dy in ds:
                x = i + dx
                y = j + dy
                if (0 <= x < m and 0 <= y < n and grid[x][y] == 1):
                    grid[x][y] = 2
                    queue.append([x, y, res + 1])

        # 还有橘子没有腐烂
        if any(grid[i][j] == 1 for i in range(m) for j in range(n)):
            return -1

        return res


grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]

s = Solution()
print(s.orangesRotting(grid))
