# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

 

示例 1：

输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
示例 2：

输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
示例 3：

输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。

https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247567/JavaC%2B%2BPython-DP

Intuition
Seem that most of games, especially stone games, are solved by dp?

Explanation

dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.

Initial status dp[i][i][1] = 0 and dp[i][i][m] = infinity

dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])

The origine python2 solution is a bit too long on the memorization part.
So I rewrote it in python3 with cache helper,
so it will be clear for logic.

Complexity
Time O(N^3/K), Space O(KN^2)
"""


class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """

        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)


        # 方法错了
        # def fun(stones, K):
        #     res = []
        #     n = len(stones)
        #     if n == K:
        #         return [sum(stones)]
        #     t = n - K + 1  # 合并次数
        #     min_sum = sum(stones[:K])  # 最小合并代价
        #     index_flag = 0
        #     for i in range(t):
        #         if sum(stones[i:i + K]) < min_sum:
        #             index_flag = i
        #             min_sum = sum(stones[i:i + K])
        #     res += min_sum
        #     stones = stones[:index_flag] + [min_sum] + stones[index_flag + K:]
        #     res += fun(stones,K)
        #     return res
        #
        # n = len(stones)
        # if n == 1:
        #     return 0
        # while n>K:
        #     n -= K-1
        # if n!=K:
        #     return -1
        # return fun(stones, K)

stones = [6,4,4,6]
K = 2
s = Solution()
print(s.mergeStones(stones,K))
