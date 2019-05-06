# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


class Solution(object):
    def solve(self, board):
        """
        记录下边界的O的坐标,放入队列,同时修改为零0,
        bfs搜索能传染到的相邻的O 同样修改为0
        最后遍历board 将所有的O修改为X,0修改为O
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 被空数组搞怕了不管有没有空输入先处理一下
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        queue = []
        # for i in range(m):
        #     for j in range(n):
        #         if (i == 0 or j==0 or i==m-1 or j == n-1) and board[i][j] == 'O':
        #             board[i][j] = '0'
        #             queue.append((i, j))
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = '0'
                    queue.append((i, j))
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    board[i][j] = '0'
                    queue.append((i, j))

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.pop(0)
            for dx, dy in d:
                x = i + dx
                y = j + dy
                if 0 < x < m and 0 < y < n and board[x][y] == 'O':
                    queue.append((x, y))
                    board[x][y] = '0'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '0':
                    board[i][j] = 'O'

    def solve2(self, board):
        """
        dfs 实现
        :param board:
        :return:
        """

        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'Y'
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)
            return

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(board, i, 0)  # 第一列
            dfs(board, i, n - 1)  # 最后一列
        for j in range(n):
            dfs(board, 0, j)  # 第一行
            dfs(board, m - 1, j)  # 最后一行
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'

board = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]

s = Solution()
s.solve2(board)
print(board)
