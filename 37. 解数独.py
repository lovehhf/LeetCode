# -*- coding:utf-8 -*-

"""
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""

from typing import List

class Solution:
    def __init__(self):
        self.n = 9
        self.row = [[0] * self.n for _ in range(self.n)]  # 行
        self.col = [[0] * self.n for _ in range(self.n)]  # 列
        self.seq = [[0] * self.n for _ in range(self.n)]  # 小方块, 可以用三维表示 seq[3][3][9], 也可以将第一维的3个元素都*3分组

    def dfs(self, board, x, y):
        if (y == self.n):
            x, y = x + 1, 0

        if (x == self.n):
            return True

        if board[x][y] != '.':
            return self.dfs(board, x, y + 1)

        for i in range(self.n):   # 对 . 枚举所有可能的数字
            k = x // 3 * 3 + y // 3
            if (self.row[x][i] or self.col[y][i] or self.seq[k][i]):
                continue

            self.row[x][i] = self.col[y][i] = self.seq[k][i] = 1  # 记录访问过的点
            board[x][y] = str(i + 1)

            if self.dfs(board, x, y + 1):
                return True

            board[x][y] = '.'   # 回溯恢复现场
            self.row[x][i] = self.col[y][i] = self.seq[k][i] = 0

        return False




    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(self.n):
            for j in range(self.n):
                if (board[i][j] != '.'):
                    idx = int(board[i][j]) - 1
                    self.row[i][idx] = self.col[j][idx] = self.seq[i // 3 * 3 + j // 3][idx] = 1

        self.dfs(board, 0, 0)



board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

s = Solution()
s.solveSudoku(board)
print(board)
