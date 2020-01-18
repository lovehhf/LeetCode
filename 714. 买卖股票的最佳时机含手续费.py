# -*- coding:utf-8 -*-

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

解题思路:
122 买卖股票的最佳时机II 的扩展, 交易是算了手续费
手续费可以看做是买入时的价格高了或者是卖出的的价格少了

状态转移方程:
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

初始状态:
dp[0][1] 不存在
-> dp[1][1] = -prices[1]

变量代替 dp[i][0] 和 dp[i][1] 滚动更新:
a, b = max(a, b + prices[i] - fee), max(b, a - prices[i])
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        a, b = 0, -prices[0]
        for price in prices[1:]:
            a, b = max(a, b + price - fee), max(b, a - price)
        return a