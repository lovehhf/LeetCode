# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n):
        """
        超时
        :type n: int
        :rtype: int
        """
        path = [['.'] * n for _ in range(n)]
        col, row = [0] * n, [0] * n
        diag = [0] * (2 * n)
        anti_diag = [0] * (2 * n)

        def dfs(x, y, s, n, res):
            if y == n:
                x, y = x + 1, 0
            if x == n:
                if s == n:
                    self.res += 1
                return
            dfs(x, y + 1, s, n, res)
            if not row[x] and not col[y] and not diag[x + y] and not anti_diag[n - x + y]:
                row[x], col[y], diag[x + y], anti_diag[n - x + y] = 1, 1, 1, 1
                path[x][y] = 'Q'
                dfs(x, y + 1, s + 1, n, path)
                path[x][y] = '.'
                row[x], col[y], diag[x + y], anti_diag[n - x + y] = 0, 0, 0, 0

        dfs(0, 0, 0, n, path)
        return self.res

    def totalNQueens2(self, n):
        def check(x, y, n, board):
            for i in range(x + 1):
                # 判断同一列是否有皇后
                if board[x - i][y] == 'Q':
                    return False
                # 判断对角线
                if y - i >= 0 and board[x - i][y - i] == 'Q':
                    return False
                # 判断逆对角线
                if y + i < n and board[x - i][y + i] == 'Q':
                    return False
            return True

        def dfs(board, n, row, res):
            if row == n:
                res.append(["".join(i) for i in board])
                return
            for i in range(n):
                if not check(row, i, n, board):
                    continue
                board[row][i] = 'Q'
                dfs(board, n, row + 1, res)
                board[row][i] = '.'

        board, res = [['.'] * n for _ in range(n)], []
        dfs(board, n, 0, res)
        # print(res)
        return len(res)


s = Solution()
print(s.totalNQueens2(10))
