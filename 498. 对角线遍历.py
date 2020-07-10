# -*- coding:utf-8 -*-

"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]
解释:
说明:
给定矩阵中的元素总数不会超过 100000 。

分类 + 找规律
横坐标和宗纵坐标相同的放一起
i + j 为奇数的，尾插
i + j 为偶数的，头插
"""

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        nums = [[] for _ in range(m + n - 1)]

        for i in range(m):
            for j in range(n):
                if (i + j) & 1:
                    nums[i + j].append(matrix[i][j])
                else:
                    nums[i + j].insert(0, matrix[i][j])
        res = []
        for i in range(m + n - 1):
            res += nums[i]

        return res
