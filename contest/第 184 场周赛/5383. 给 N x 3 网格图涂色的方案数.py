# -*- coding:utf-8 -*-

"""
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
给你网格图的行数 n 。
请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。

示例 1：
输入：n = 1
输出：12
解释：总共有 12 种可行的方法：

示例 2：
输入：n = 2
输出：54

示例 3：
输入：n = 3
输出：246

示例 4：
输入：n = 7
输出：106494

示例 5：
输入：n = 5000
输出：30228214

提示：
n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""

from collections import defaultdict


class Solution:
    def numOfWays(self, n: int) -> int:
        """
        暴力法，
        枚举每行所有的方案, 记录每次迭代所有状态出现的次数
        暴力统计所有和上一行颜色都不同的方案数量
        :param n:
        :return:
        """
        status = ["010", "012", "020", "021", "101", "102", "120", "121", "201", "202", "210", "212"]

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for statu in status:
            d1[statu] = 1

        for k in range(1, n):
            for i in range(12):
                for j in range(12):
                    if (all(status[i][k] != status[j][k] for k in range(3))):
                        d2[status[j]] += d1[status[i]] % (10 ** 9 + 7)

            d1 = d2
            d2 = defaultdict(int)

        res = sum(d1.values()) % (10 ** 9 + 7)
        return res


n = 5000
sol = Solution()
print(sol.numOfWays(n))