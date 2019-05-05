# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        # 方向数组 右下左上
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # 方向指示变量
        cur = 1
        while cur < n ** 2 + 1:
            res[i][j] = cur
            x, y = i + ds[d][0], j + ds[d][1]  # 下一步坐标
            # 需要变向
            if x < 0 or x == n or y < 0 or y == n or res[x][y] != 0:
                d = (d + 1) % 4
                x, y = i + ds[d][0], j + ds[d][1] # 重置下一步坐标
            i, j = x, y
            cur += 1
        return res

    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]

        i, j, di, dj = 0, 0, 0, 1
        for number in range(1, n ** 2 + 1):
            res[i][j] = number
            # 骚操作
            if res[(i + di) % n][(j + dj) % n] != 0:  # 需要转向
                di, dj = dj, - di  # 0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1
            i += di
            j += dj

        return res


n = 3
s = Solution()
print(s.generateMatrix(n))
