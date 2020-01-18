# -*- coding:utf-8 -*-

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

题意: 不限制购买股票的次数, 但是有下一次买需要卖出超过1天

解题思路:

套用 122 的状态转移方程:
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                 继续空仓观望       卖出手上的股票
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])   # dp[i - 1][0] 不能是从 dp[i - 2][1] + prices[i] 转移过来的
                 继续持有股票       买入股票

dp[i][1] 的状态转移问题:
如果从 i - 1 天转移的话, dp[i - 1][0] (第i - 1天, 手上没有股票) 中不可能是从 dp[i - 2][1] + prices[i - 1] (第 i-2 天, 手上有股票)
                      这意味着是在 i - 1 天卖出了股票, 那第 i 天就是冷冻期, 不能买股票, 与 dp[i][1] 矛盾了
dp[i][1] 的 max 的右半边的 dp[i - 1][0] 就只能等于 dp[i - 2][0]

-> dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

初始状态:
dp[0][0] = 0
dp[0][1] 不存在
dp[1][0] = 0
dp[1][1] = -prices[i]

答案: dp[n][0]
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        prices.insert(0, 0)  # 下标1算第一天, 方便处理

        dp[1][1] = -prices[1]
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n][0]


s = Solution()
prices = [1, 2, 3, 0, 2]
print(s.maxProfit(prices))
