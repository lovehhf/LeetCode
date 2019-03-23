# -*- coding:utf-8 -*-

__author__ = 'huanghf'

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
"""


class Solution(object):
    '''
    顺时针旋转
    先翻转二维数组,再交叉对换
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    '''
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                # print([i,j],[j,i])
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
            # print("----------")

    def rotate2(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print(list(zip(*A)))
        # t = *A[::-1]
        # print(A[:])
        A[:] = zip(*A[::-1])

    def anti_rotate(self, matrix):
        """
        逆时针旋转
        anticlockwise rotate
        first reverse left to right, then swap the symmetry
        1 2 3     3 2 1     3 6 9
        4 5 6  => 6 5 4  => 2 5 8
        7 8 9     9 8 7     1 4 7
        https://github.com/zzhznx/LeetCode-Python/blob/9dd98d903e492fc509f0096115caccfd4c9fe8e8/48-Rotate%20Image.py
        :param matrix:
        :return:
        """
        for m in matrix:
            m[:] = m[::-1]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
        return matrix

    def anti_rotate_with_zip(self, matrix):
        """逆时针旋转 使用zip"""
        for m in matrix:
            m[:] = m[::-1]
        matrix[:] = zip(*matrix)
        return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


s = Solution()
s.rotate2(matrix)
print(matrix)