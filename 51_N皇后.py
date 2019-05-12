# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

暴力搜索所有方案。
为了优化时间效率，定义 vector<bool>row, col, diag, anti_diag;用来记录每一行、每一列、每条对角线上是否有皇后存在。
搜索时需要记录4个状态：x,y,s,n 分别表示横纵坐标、已摆放的皇后个数、棋盘大小。
对于每步搜索，有两种选择：
1.当前格子不放皇后，则转移到 dfs(x, y + 1, s, n);
2.如果(x,y)所在的行、列、对角线不存在皇后，则当前格子可以摆放皇后，更新row, col, diag, anti_diag后转移到 dfs(x, y + 1, s + 1, n);
回溯时不要忘记恢复row, col, diag, anti_diag等状态。
"""

import copy


class Solution(object):
    def solveNQueens(self, n):
        """
        回溯
        :type n: int
        :rtype: List[List[str]]
        """
        row, col = [0] * n, [0] * n
        diag, anti_diag = [0] * (2 * n), [0] * (2 * n)


        def dfs(x, y, s, n, path, res):
            if y == n:
                x += 1
                y = 0
            if x == n:
                if s == n:
                    res.append(copy.deepcopy(path))
                return
            if not row[x] and not col[y] and not diag[x + y] and not anti_diag[n - 1 - x + y]:
                row[x] = col[y] = diag[x + y] = anti_diag[n - 1 - x + y] = 1
                path[x][y] = 'Q'
                dfs(x, y + 1, s + 1, n, path, res)
                path[x][y] = '.'
                row[x] = col[y] = diag[x + y] = anti_diag[n - 1 - x + y] = 0
            dfs(x, y + 1, s, n, path, res)
        res = []
        path = [['.'] * n for _ in range(n)]
        dfs(0, 0, 0, n, path, res)
        return [[''.join(y) for y in x] for x in res]

    def solveNQueens2(self, n):
        """
        https://leetcode.com/problems/n-queens/discuss/19937/AC-Python-76-ms-iterative-backtracking-solution
        :param n:
        :return:
        """
        ans = []
        queens = [-1] * n
        columns = [True] * n + [False]  # || col with dummy for boundary
        back = [True] * n * 2  # \\ col - row
        forward = [True] * n * 2  # // col + row
        row = col = 0
        while True:
            if columns[col] and back[col - row + n] and forward[col + row]:
                queens[row] = col
                columns[col] = back[col - row + n] = forward[col + row] = False
                row += 1
                col = 0
                if row == n:
                    ans.append(['.' * q + 'Q' + '.' * (n - q - 1) for q in queens])
            else:
                if row == n or col == n:
                    if row == 0:
                        return ans
                    row -= 1
                    col = queens[row]
                    columns[col] = back[col - row + n] = forward[col + row] = True
                col += 1


n = 8
s = Solution()
print(s.solveNQueens2(n))
