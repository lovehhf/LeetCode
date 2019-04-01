# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False
        m,n = len(matrix),len(matrix[0])
        # 第一行第一列的值大于目标值 直接返回False
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False

        l = 0
        r = m
        while l<=r:
            mid = (l + r) // 2
            if matrix[mid][-1] == target:
                return True
            # 中间的值比目标值大
            elif matrix[mid][-1] > target:
                r = mid - 1
            else:
                l = mid + 1

        # 改为二分查找 找到在哪一行
        # i = 0
        # for i in range(m):
        #     if matrix[i][-1]>target:
        #         break

        targets = matrix[l]
        # 二分搜素
        L,R = 0,n-1

        while L<=R:
            mid = (L + R) // 2
            if targets[mid] == target:
                return True
            # 中间值大于目标值, 说明目标值在左区间
            elif targets[mid]>target:
                R = mid - 1
            else:
                L = mid + 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 16
s = Solution()
print(s.searchMatrix(matrix,target))