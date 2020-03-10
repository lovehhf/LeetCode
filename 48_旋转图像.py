# -*- coding:utf-8 -*-

"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

参考了: https://github.com/zzhznx/LeetCode-Python/blob/9dd98d903e492fc509f0096115caccfd4c9fe8e8/48-Rotate%20Image.py
"""


class Solution(object):

    def rotate(self, matrix):
        """
        '''
        顺时针旋转
        先翻转每一列,再交叉对换
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        '''
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 先翻转每一列
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        # 再交叉互换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class AntiRotateSolution(object):

    def anti_rotate(self, matrix):
        """
        逆时针旋转
        先翻转每一行, 再翻转每一列
        1 2 3     3 2 1     3 6 9
        4 5 6  => 6 5 4  => 2 5 8
        7 8 9     9 8 7     1 4 7
        :param matrix:
        :return:
        """
        n = len(matrix)

        # 翻转每一行
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

        # 交叉互换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    s = Solution()
    s.rotate(matrix)
    print(matrix)

    s2 = AntiRotateSolution()
    s2.anti_rotate(matrix)

    print(matrix)
