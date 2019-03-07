# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
https://leetcode-cn.com/problems/pascals-triangle/
"""

def generate(numRows):
    triangle = []
    for i in range(0, numRows):
        row = [1 for _ in range(i + 1)]

        # 填充第2~i-1行
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i-1][j]

        triangle.append(row)
        # print(row)
    return triangle

print(generate(10))