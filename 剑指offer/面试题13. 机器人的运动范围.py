# -*- coding:utf-8 -*-

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution_BFS:
    """
    bfs 解法
    """
    def get_sum(self, i, j):
        """
        计算 行坐标和列坐标的数位之和
        :param i:
        :param j:
        :return:
        """
        ret = 0
        while (i > 0):
            ret += i % 10
            i //= 10
        while (j > 0):
            ret += j % 10
            j //= 10
        return ret

    def movingCount(self, m: int, n: int, k: int) -> int:
        board = [[self.get_sum(i, j) <= k for j in range(n)] for i in range(m)]  # board[i][j] 表示 (i, j) 是否可以访问
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = [[0] * n for _ in range(m)]
        queue = [(0, 0)]
        vis[0][0] = 1  # 记录已经走过的坐标, 已经走过的坐标不再重复走
        res = 1

        while (queue):
            i, j = queue.pop(0)
            for dx, dy in ds:
                x = i + dx
                y = j + dy
                if (0 <= x < m and 0 <= y < n and board[x][y] and not vis[x][y]):
                    vis[x][y] = 1
                    res += 1
                    queue.append((x, y))
        return res


class Solution_DFS:
    """
    深度优先解法
    """

    def get_sum(self, i, j):
        ret = 0
        while (i > 0):
            ret += i % 10
            i //= 10
        while (j > 0):
            ret += j % 10
            j //= 10
        return ret

    def dfs(self, m, n, i, j, k):
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            # 满足条件就 dfs 下去
            if (0 <= x < m and 0 <= y < n and self.get_sum(x, y) <= k and not self.vis[x][y]):
                self.vis[x][y] = 1
                self.res += 1
                self.dfs(m, n, x, y, k)

    def movingCount(self, m: int, n: int, k: int) -> int:

        self.vis = [[0] * n for _ in range(m)]
        self.vis[0][0] = 1
        self.res = 1
        self.dfs(m, n, 0, 0, k)

        return self.res
