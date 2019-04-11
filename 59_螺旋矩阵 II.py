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

        i, j, di, dj = 0, 0, 0, 1
        for number in range(1, n ** 2 + 1):
            res[i][j] = number
            if res[(i + di) % n][(j + dj) % n] != 0:  # 需要转向
                di, dj = dj, - di  # 0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1
            i += di
            j += dj

        return res

n = 3
s = Solution()
print(s.generateMatrix(n))
