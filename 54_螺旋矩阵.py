# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


def spiralOrder(matrix):
    """
    :param matrix: 二维列表
    :return: 顺时针输出的一维数组
    """
    res = []

    while matrix:
        """
        删除第一行 然后二维数组逆时针旋转90度 继续再删除第一行 一直这样直到没有可以输出的了
        
        [
          [5, 6, 7, 8],   ===>   [[8,12],[7,11],[6,10],[5,9]]
          [9,10,11,12]
        ]
        0,3->3,0 0,2->2,0
        行数: 变列数  下标递增 range(0,m)x
        列数: 变行数  下标递减 range(n,-1,-1)
        """
        res += matrix.pop(0)
        if matrix:
            m, n = len(matrix), len(matrix[0])  # 行,列 3,4
            matrix = [[row[x] for row in matrix] for x in range(n-1, -1, -1)] # 逆时针旋转二位数组
    return res

    #
    # ret = []
    # if matrix == []:
    #     return ret
    # ret.extend(matrix[0])  # 上侧
    # new = [reversed(i) for i in matrix[1:]]
    # if new == []:
    #     return ret
    # r = self.spiralOrder([i for i in zip(*new)])
    # ret.extend(r)
    # return ret

print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))