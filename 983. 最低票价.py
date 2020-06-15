# -*- coding:utf-8 -*-

"""
983. 最低票价
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets

在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
火车票有三种不同的销售方式：
一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

示例 1：
输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。

示例 2：
输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。
你总共花了 $17，并完成了你计划的每一天旅行。

提示：
1 <= days.length <= 365
1 <= days[i] <= 365
days 按顺序严格递增
costs.length == 3
1 <= costs[i] <= 1000
"""

from typing import List


class DFS_Solution:
    def __init__(self):
        self.d = {}

    def binsearch(self, days, u):
        """
        查找 days >= u 的左边界
        """
        if u > days[-1]:
            return 366

        l, r = 0, len(days) - 1

        while(l < r):
            mid = (l + r) >> 1
            if days[mid] >= u:
                r = mid
            else:
                l = mid + 1

        return l

    def dfs(self, days, costs, u):
        """
        记忆化搜索
        u: 当前搜索到的下标
        """
        if self.d.get(u) != None:
            return self.d[u]

        n = len(days)
        if u >= n:
            return 0

        a = self.dfs(days, costs, u + 1) + costs[0]  # 1天

        i = self.binsearch(days, days[u] + 7)   # 7天后的索引
        j = self.binsearch(days, days[u] + 30)  # 30天后的索引

        b = self.dfs(days, costs, i) + costs[1]
        c = self.dfs(days, costs, j) + costs[2]

        self.d[u] = min(a, b, c)
        return self.d[u]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.dfs(days, costs, 0)


class DP_Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        状态表示:
        dp[i]: 第 i 天的最低花费
        状态转移:
        dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2]) if i in days else dp[i - 1]
        """
        dp = [0] * (days[-1] + 31)

        for i in range(1, len(dp)):
            if i in days:
                # 当天要出门, 从 1 天, 7 天, 30天 前转移状态
                dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2])
            else:
                # 当天不需要出门，不用买票
                dp[i] = dp[i - 1]

        return dp[-1]


s1 = DP_Solution()
s2 = DFS_Solution()
days = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39,
        41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91,
        93, 94, 97, 99]

costs = [9, 38, 134]
a = s1.mincostTickets(days, costs)
b = s2.mincostTickets(days, costs)

print(a, b)
