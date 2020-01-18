# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
     
状态表示:
dp[i][j][k]: 第 i 天, 还可以进行 j 次交易, 是否持有股票 
不限制交易次数, j = +∞ -> j = j - 1, 状态转移就与 j 无关了

状态转移: 
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
-> res = dp[n][0]
初始状态：
dp[0][0] = 0
dp[0][1] -> 不存在

使用变量 a, b 代替 dp[i][0] 和 dp[i][1] —>
a, b = max(a, b + prices[i]),  max(b, a - prices[i])
初始(第一天)： a = 0, b = -prices[0] 
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        a, b = 0, -prices[0]
        for price in prices[1:]:
            a, b = max(a, b + price), max(b, a - price)
        return a


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))