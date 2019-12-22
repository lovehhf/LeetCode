# -*- coding:utf-8 -*-

"""
给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
 

示例 1：



输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于 4 的正方形的最大边长为 2，如图所示。
示例 2：

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0
示例 3：

输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
输出：3
示例 4：

输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
输出：2
 

提示：

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5

直接暴力枚举边长会超时（时间复杂度O(n^3) = 300*300*300 = 2700w），一秒大概能处理100w...

可以二分搜边长最大值, 时间复杂度(n^2logn) = 300*300*8 = 72w 时间差不多够了
"""


class Solution(object):

    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = 0

        # 前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = mat[i - 1][j - 1] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

        l, r = 0, min(m, n)

        # 二分找最大值
        while (l < r):
            k = (l + r + 1) >> 1  # 除2向上取整，向下取整可能死循环
            flag = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if (i + k <= m and j + k <= n):
                        # 正方形的和
                        t = s[i + k][j + k] - s[i - 1][j + k] - s[i + k][j - 1] + s[i - 1][j - 1]
                        if (t <= threshold):
                            res = max(res, k + 1)
                            flag = 1
                            break
                if flag:
                    break
            # t可以满足，往右边看是否有更大的, 否则右边界往左移
            if flag:
                l = k
            else:
                r = k - 1

        # 暴力做法
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         # 枚举边长(会超时)
        #         for k in range(min(m,n)):
        #             if (i + k <= m and j + k <= n):
        #                 # 正方形所有小方格的值加起来的值
        #                 t = s[i + k][j + k] - s[i - 1][j + k] - s[i + k][j - 1] + s[i - 1][j - 1]
        #                 if(t <= threshold):
        #                     res = max(res, k + 1)
        return res
