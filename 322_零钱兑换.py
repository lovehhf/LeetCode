# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

bfs:
每一次都加上所有硬币,因为是广度遍历,所得到第一次得到的结果一定是可以用最少硬币达到的
"""

import collections


class Solution(object):
    def coinChange(self, coins, amount):
        """
        bfs AC
        :param coins:
        :param amount:
        :return:
        """
        if amount == 0:
            return 0
        queue = collections.deque(coins)
        d = {x: 1 for x in coins}
        while queue:
            cur = queue.popleft()
            if cur == amount:
                return d[cur]
            for i in coins:
                k = cur + i
                if k <= amount and not k in d:
                    queue.append(k)
                    d[k] = d[cur] + 1
        return -1
    def coinChange3(self, coins, amount):
        """
        完全背包问题
        :param coins:
        :param amount:
        :return:
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        print(dp)
        return dp[-1] if dp[-1]!=float('inf') else -1

    def coinChange2(self, coins, amount):
        """
        dfs, 超时 31/182
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def dfs(coins, target, path, res):
            if target < 0:
                return
            if target == 0:
                res[:] = path
                return True
            for i in coins:
                if dfs(coins, target - i, path + [i], res):
                    return res
            return False

        if amount == 0:
            return 0
        coins = sorted(coins, reverse=True)
        res = []
        dfs(coins, amount, [], res)
        if res:
            return len(res)
        return -1


coins = [1, 2, 5]
amount = 50
s = Solution()
print(s.coinChange(coins, amount))
print(s.coinChange3(coins, amount))
