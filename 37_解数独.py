# -*- coding:utf-8 -*-

__author__ = 'huanghf'

import copy

class Solution:
    def solveSudoku(self, board):
        """
        回溯
        :param board:
        :return:
        """

        # def check1(board, i, j, k):
        #     # A = [[] for _ in range(9)]
        #     # B = [[] for _ in range(9)]
        #     # C = [[] for _ in range(9)]
        #     for r in range(9):
        #         for c in range(9):
        #             t = r//3*3 + c//3
        #             if (r == i or j==c or t==(i//3*3 + j//3)) and (r,c)!=(i,j):
        #                 if k==board[r][c]:
        #                     return False
        #     return True

        def check(board, i, j, k):
            for t in range(9):
                if t != j and board[i][t] == k:
                    return False
                if t != i and board[t][j] == k:
                    return False

            tmp_i = i // 3 * 3
            tmp_j = j // 3 * 3
            for s in range(tmp_i, tmp_i + 3):
                for t in range(tmp_j, tmp_j + 3):
                    if s != i and t != j and board[s][t] == k:
                        return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in [str(i) for i in range(1, 10)]:
                            if check(board, i, j, k):
                                board[i][j] = k
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve(board)

    # def solveSudoku2(self, board):
        # """
        # Do not return anything, modify board in-place instead.
        # """
        #
        # def remove_num(r, i, j):
        #     print(r,i,j,r[i][j])
        #     for t in range(9):
        #         if r[t][j]:
        #             r[t][j] -= r[i][j]
        #         if r[i][t]:
        #             r[i][t] -= r[i][j]
        #         tmp_i = i // 3 * 3
        #         tmp_j = j // 3 * 3
        #         for ti in range(tmp_i, tmp_i + 3):
        #             for tj in range(tmp_j, tmp_j + 3):
        #                 r[ti][tj] -= r[i][j]
        #
        # n = 0
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == '.':
        #             n += 1
        #
        # A = [[] for _ in range(9)]
        # B = [[] for _ in range(9)]
        # C = [[] for _ in range(9)]
        # S = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # for i in range(9):
        #     for j in range(9):
        #         k = (i // 3) * 3 + j // 3
        #         if board[i][j] != '.':
        #             # print(i,j,k,board[i][j])
        #             A[i].append(board[i][j])
        #             B[j].append(board[i][j])
        #             C[k].append(board[i][j])
        #
        # A = [S - set(x) for x in A]
        # B = [S - set(x) for x in B]
        # C = [S - set(x) for x in C]
        #
        # # print(A)
        # # print(B)
        # # print(C)
        # d = {}
        # r = [[set() for _ in range(9)] for _ in range(9)]
        #
        # for i in range(9):
        #     for j in range(9):
        #         k = i // 3 * 3 + j // 3
        #         if board[i][j] == '.':
        #             tmp = A[i] & B[j] & C[k]
        #             r[i][j] = tmp
        #
        #             # print(i,j,k,tmp)
        #             # t = []
        #             # if len(tmp) == 1:
        #             #     print(i,j,tmp,1)
        #             #     board[i][j] = str(list(tmp)[0])
        #             #     d[(i, j)] = str(list(tmp)[0])
        #             #     t.append(tmp)
        #             #     A[i] = A[i] - tmp
        #             #     B[j] = B[j] - tmp
        #             #     C[k] = C[k] - tmp
        #             # print(board)
        #     # print("A",A)
        #     # print("B",B)
        #     # print("C",C)
        #     # print("board:",board)
        # print(n)
        # for i in r:
        #     print(i)
        #
        # while n > 0:
        #     for i in range(9):
        #         for j in range(9):
        #             if r[i][j]:
        #                 # k = i // 3 * 3 + j // 3
        #                 if len(r[i][j]) == 1:
        #                     num = str(list(r[i][j])[0])
        #                     n -= 1
        #                     board[i][j] = num
        #                     print(i, j, num)
        #                     remove_num(r, i, j)
        #
        #                     # for t in range(9):
        #                     #     if r[t][j]:
        #                     #         r[t][j] -= r[i][j]
        #                     #     if r[i][t]:
        #                     #         r[i][t] -= r[i][j]
        #                     #     tmp_i = i // 3 * 3
        #                     #     tmp_j = j // 3 * 3
        #                     #     for ti in range(tmp_i,tmp_i+3):
        #                     #         for tj in range(tmp_j,tmp_j+3):
        #                     #             r[ti][tj] -= r[i][j]
        #                 else:
        #                     tmp = copy.deepcopy(r[i][j])
        #
        #                     for t in range(9):
        #                         if t != i:
        #                             tmp -= r[t][j]
        #
        #                     if len(tmp) == 1:
        #                         num = str(list(r[i][j])[0])
        #                         n -= 1
        #                         board[i][j] = num
        #                         r[i][j] = tmp
        #                         remove_num(r, i, j)
        #
        #
        #                     if r[i][j]:
        #                         tmp = copy.deepcopy(r[i][j])
        #
        #                         for t in range(9):
        #                             if t != j:
        #                                 tmp -= r[i][t]
        #                         if len(tmp) == 1:
        #                             num = str(list(r[i][j])[0])
        #                             n -= 1
        #                             board[i][j] = num
        #                             r[i][j] = tmp
        #                             remove_num(r, i, j)
        #
        #                     if r[i][j]:
        #                         tmp = copy.deepcopy(r[i][j])
        #
        #                         tmp_i = i // 3 * 3
        #                         tmp_j = j // 3 * 3
        #                         for ti in range(tmp_i, tmp_i + 3):
        #                             for tj in range(tmp_j, tmp_j + 3):
        #                                 if (i, j) != (ti, tj):
        #                                     tmp -= r[ti][tj]
        #                         if len(tmp) == 1:
        #                             num = str(list(r[i][j])[0])
        #                             n -= 1
        #                             board[i][j] = num
        #                             r[i][j] = tmp
        #                             remove_num(r, i, j)
        #
        #                     for z in r:
        #                         print(z)
        #
        #                     print(i, j, tmp, n)
        #
        #                 # tmp = r[i][j]
        #
        #                 # for t in range(9):
        #
        #                 # for i1 in range(9):
        #                 #     flag = False
        #                 #     for j1 in range(9):
        #                 #         k1 = i1 // 3 * 3 + j1 // 3
        #                 #         if (i1==i or j1==i or k1==k) and (i,j)!=(i1,j1):
        #                 #             tmp -= r[i1][j1]
        #                 #         if len(tmp) == 1:
        #                 #             num = str(list(tmp)[0])
        #                 #             r[i][j] = set()
        #                 #             board[i][j] = num
        #                 #         if not tmp:
        #                 #             flag = True
        #                 #             break
        #                 #     if flag:
        #                 #         break
        # print(board)
        # # print(i,j,str(list(tmp)[0]))
        # # if len(tmp) == 2:
        # #     print(i,j,tmp,2)
        # # for i in r:
        # #     print(i)


board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)
print(board)
