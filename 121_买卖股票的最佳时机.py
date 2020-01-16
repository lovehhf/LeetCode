# -*- coding:utf-8 -*-

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


解题思路:

正常思维: 画图找出所有的 波峰和波谷, 波峰减掉波谷的最大值就是答案 

dp转移方程分析参考 [一个方法团灭 6 道股票问题](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/)

dp[i][j][k] 表示第 i 天, 最多可操作 j 次, 手里是否持有股票(k = 1 or 0)

状态转移方程:
dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                   不做任何操作         卖掉手里的股票
dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][1] - prices[i])
                   不做任何操作         买入今天的股票
买入时算交易次数 j -= 1, 卖出时由于再买入时算过了交易次数, 不需要再减

初始状态: (股价的下标从1开始算)
dp[0][j][0] = 0: 第 0 天, 还没有开始交易, 盈利为0
dp[i][0][1]: 不存此情况, 手里还有股票, 但是交易次数为0的情况
dp[0][j][1]: 不存在此情况， 还没有开始交易, 手上不可能有股票

本题套用此转移方程:
dp[i][0][1]  # 不存在此情况

dp[i][0][0] = dp[i - 1][0][0]  # dp[i - 1][0][1] 的情况不存在
            = dp[i - 2][0][0]
            = 0

dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
            = max(dp[i - 1][1][1], -prices[i])

dp[i][1][0] = max(dp[i - 1][1][0]，dp[i - 1][1][1] + prices[i])

可以发现 j 只可能是 1, 可以消掉 j, 从三维dp变为二维dp， 得到转移方程

dp[i][1] = max(dp[i - 1][1], -prices[i])
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
-> res = dp[n][0]

观察发现 dp[i][0], dp[i][1] 只和 dp[i - 1][0] 和 dp[i - 1][1] 有关，可以使用两个变量滚动更新这两个值
空间复杂度O(n) -> O(1)：

a, b = max(a, -price), max(b, a + price)
-> res = b
初始状态为
a = dp[1][1] = -prices[1]   # dp[0][1] 不存在
b = dp[1][0] = 0    # dp[0][1] 不存在
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        a, b = -prices[0] if prices else 0, 0
        for price in prices[1:]:
            a, b = max(a, -price), max(b, a + price)
        return b


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))
