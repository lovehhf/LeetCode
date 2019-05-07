# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        自上向下dp
        空间复杂度0(n^2)
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])

    def minimumTotal2(self, triangle):
        """
        自顶乡下dp 空间复杂度O(n^2)
        代码复杂度优化 加一行不用初始化dp
        :param triangle:
        :return:
        """
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    def minimumTotal3(self, triangle):
        """
        空间优化
        空间复杂度0(n)
        骚方法 学不来
        :param triangle:
        :return:
        """
        if not triangle:
            return 0
        n = len(triangle)
        dp = [0] * (n + 1)  # dp不但记录了每层最小值 还记录了自顶到第i层第j个元素的最小路径和
        for i in range(n - 1, -1, -1):
            # print(i, triangle[i])
            for j in range(i + 1):
                # 这里的dp[j] 使用的时候默认是上一层的，赋值之后变成当前层
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
                print('dp:', j, dp)
        print(dp)
        return dp[0]


s = Solution()
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 3, 8, 1],
    [6, 1, 8, 9, 2]
]

print(s.minimumTotal3(triangle))
