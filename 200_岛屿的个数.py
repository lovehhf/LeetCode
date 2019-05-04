# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        简单的bfs
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        res = 0
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        a, b = queue.pop(0)
                        for dx, dy in d:
                            x = a + dx
                            y = b + dy
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '#'
                                queue.append((x, y))
        # print(grid)
        return res

    # def numIslands2(self, grid):
    #     # 似乎不行 还是bfs靠谱
    #     if not grid or not grid[0]:
    #         return 0
    #     res = 0
    #     m, n = len(grid), len(grid[0])
    #     d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '1':
    #                 for dx, dy in d:
    #                     x = i + dx
    #                     y = j + dy
    #                     if 0 <= x < m and 0 <= y < n and grid[x][y] == '#':
    #                         grid[i][j] = '#'
    #                         break
    #             if grid[i][j] == '1':
    #                 print(i,j)
    #                 res += 1
    #                 grid[i][j] = '#'
    #     print(grid)
    #     return res


grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
s = Solution()
print(s.numIslands(grid))
