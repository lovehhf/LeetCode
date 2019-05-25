# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。
 

示例 1：

输入: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

示例 2：

输入: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

输出: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

 

注意：

输入矩阵的宽和高的范围为 [1,50]。
点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
输入面板不会是游戏结束的状态（即有地雷已被挖出）。
简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。
"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return board

        x, y = click[0], click[1]
        if board[x][y] == "M":  # 一下就挖到地雷，可以直接修改然后返回
            board[x][y] = "X"
            return board

        m, n = len(board), len(board[0])
        visited = [[0 for _ in range(n + 1)] for j in range(m + 1)]

        dx = [1, 1, -1, -1, 0, 0, -1, 1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]

        def dfs(x0, y0):
            if board[x0][y0] == "M" or visited[x0][y0] == 1:  # 如果该点是地雷，或者已经来过了，就直接跑路
                return

            visited[x0][y0] = 1  # 标记一下来过了
            mineCnt = 0  # 统计当前点附近有几个地雷
            for k in range(8):
                x = x0 + dx[k]
                y = y0 + dy[k]

                if 0 <= x < m and 0 <= y < n and board[x][y] == "M":
                    mineCnt += 1

            if mineCnt > 0:
                board[x0][y0] = str(mineCnt)  # 如果有雷，就直接说有几个雷
            else:
                board[x0][y0] = 'B'  # 没有相邻地雷，就还需要递归周围的点

                for k in range(8):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                        dfs(x, y)

        dfs(x, y)
        return board

board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

s = Solution()
print(s.updateBoard(board,[3,0]))