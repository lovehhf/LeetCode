# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""

在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。

返回车能够在一次移动中捕获到的卒的数量。
 
 
board.length == board[i].length == 8
board[i][j] 可以是 'R'，'.'，'B' 或 'p'
只有一个格子上存在 board[i][j] == 'R'
 """


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rook = 0
        i,j = 0,0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = 1
                    break
            if rook:
                break
        w = [board[x][j] for x in range(i-1,-1,-1)]
        s = [board[x][j] for x in range(i+1,8)]
        a = board[i][:j][::-1]
        d = board[i][j+1:]
        res = 0
        for i in w:
            if i=='B':
                break
            if i=='p':
                res += 1
                break
        for i in a:
            if i == 'B':
                break
            if i == 'p':
                res += 1
                break
        for i in s:
            if i == 'B':
                break
            if i == 'p':
                res += 1
                break
        for i in d:
            if i == 'B':
                break
            if i == 'p':
                res += 1
                break
        return res
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
s = Solution()
print(s.numRookCaptures(board))
