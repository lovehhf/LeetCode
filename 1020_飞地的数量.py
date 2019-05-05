# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：

输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释： 
有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

示例 2：

输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：
所有 1 都在边界上或可以到达边界。
"""


class Solution(object):
    def numEnclaves(self, A):
        """
        dfs
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and A[i][j]:
                A[i][j] = 0
                dfs(i - 1, j), dfs(i + 1, j), dfs(i, j - 1), dfs(i, j + 1)
        for i in range(m):
            dfs(i, 0), dfs(i, n - 1)
        for j in range(n):
            dfs(0, j), dfs(m - 1, j)
        return sum(A[i][j] for i in range(m) for j in range(n))

A = [[0,0,0,0],
     [1,0,1,0],
     [0,1,1,0],
     [0,0,0,0]]
s = Solution()
print(s.numEnclaves(A))