# -*- coding:utf-8 -*-

"""
5129. 下降路径最小和 II 显示英文描述
用户通过次数146
用户尝试次数190
通过次数146
提交次数284
题目难度Hard
给你一个整数方阵 arr ，定义「非零偏移下降路径」为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。

请你返回非零偏移下降路径数字和的最小值。



示例 1：

输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
输出：13
解释：
所有非零偏移下降路径包括：
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。


提示：

1 <= arr.length == arr[i].length <= 200
-99 <= arr[i][j] <= 99
"""

from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        """
        dp[i][j]: 从第一行走到i,j的最短距离
        dp[i][j] 可以从出i-1行除dp[i-1][j]外的所有点转移过来
        状态转移方程 dp[i][j] = arr[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
        :param arr:
        :return:
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = arr[0][i]

        for i in range(1, n):
            for j in range(n):
                t = min(dp[i - 1][:j] + dp[i - 1][j + 1:])
                dp[i][j] = arr[i][j] + t

        return min(dp[n - 1])


s = Solution()
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.minFallingPathSum(arr))
