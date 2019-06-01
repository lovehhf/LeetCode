# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
说明: 
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n^2 。

做法一: 合并为一维数组，快速选择。时间复杂度O(n^2logk)
做法二: 堆排序扩展
由于矩阵已经排好序了，所以不需要一次将所有元素放在堆中,可以弹出并push k次，如果堆中不弹出matrix[i][j]就不需要将[i+1][j]放入堆中
eg: 给出矩阵[[1,2,3],[4,5,6][7,8,9]] 
先push 1到堆，
再pop1,push 2和4 堆中元素 2,4
pop2 push 3和5 堆中元素 3,4,5
pop3,push6 堆中元素 4,5,6
pop4,push7 堆中元素5 6 7
...
最坏情况需要push n^2 次,堆中元素最多有n个，时间复杂度O(n^2logn)
"""

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # return list(heapq.merge(*matrix))[k - 1]
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1
        return result


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

k = 15
s = Solution()
print(s.kthSmallest(matrix, k))
