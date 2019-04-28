# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        n = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    n+=1

        A = [[] for _ in range(9)]
        B = [[] for _ in range(9)]
        C = [[] for _ in range(9)]
        S = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i in range(9):
            for j in range(9):
                k = (i//3)*3 + j//3
                if board[i][j]!='.':
                    # print(i,j,k,board[i][j])
                    A[i].append(board[i][j])
                    B[j].append(board[i][j])
                    C[k].append(board[i][j])

        A = [S - set(x) for x in A]
        B = [S - set(x) for x in B]
        C = [S - set(x) for x in C]

        # print(A)
        # print(B)
        # print(C)
        d = {}
        # r = [[0 for _ in range(9)] for _ in range(9)]
        while n>0:
            for i in range(9):
                for j in range(9):
                    k = i//3*3 + j//3
                    if board[i][j] == '.':
                        # print(i,j,A[i],B[j],C[k])
                        tmp = A[i]&B[j]&C[k]
                        t = []
                        if len(tmp) == 1:
                            print(i,j,tmp,1)
                            board[i][j] = str(list(tmp)[0])
                            d[(i, j)] = str(list(tmp)[0])
                            t.append(tmp)
                            n -= 1
                            A[i] -= tmp
                            B[j] -= tmp
                            C[k] -= tmp
        # print(board)
                        # print(i,j,str(list(tmp)[0]))
                    # if len(tmp) == 2:
                    #     print(i,j,tmp,2)
        # for i in r:
        #     print(i)



board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

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