# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
 

示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。
示例 2：

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
 

提示：

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
最多 25 个单元格中有黄金。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-maximum-gold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import copy


class Solution(object):
    def __init__(self):
        self.res = 0

    def dfs(self, g, m, n, x, y, cur):
        """
        :param i:
        :param j:
        :param cur:
        :return:
        """
        cur += g[x][y]
        d = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        self.res = max(self.res, cur)
        t = g[x][y]
        g[x][y] = 0
        for dx, dy in d:
            i = x + dx
            j = y + dy
            if 0 <= i < m and 0 <= j < n and g[i][j]:
                self.dfs(g, m, n, i, j, cur)
        g[x][y] = t

    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                g = copy.deepcopy(grid)
                if 0 <= i < m and 0 <= j < n and grid[i][j]:
                    self.dfs(g, m, n, i, j, 0)
                    # print(i,j,self.res)
        return self.res

s = Solution()
grid = [[1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20]]
print(s.getMaximumGold(grid))
