# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

动态规划:
dp[i] 表示通过平方数组成 i 所需要的最少数量。
则 dp[i] = min(dp[i-j*j]+1)  其中1<=j<=i**0.5
dp[n]即为最终答案
dp[12] = min(dp[12-1]+1,dp[12-4]+1,dp[12-9]+1) = min(dp[11],dp[8],d[3])+1 = min(3,2,3)+1=3



1. 根据 拉格朗日四平方和定理，可以得知答案必定为 1, 2, 3, 4 中的一个。
2. 其次根据 勒让德三平方和定理，可以得知当 n=(8b+7)*4^a时，n 不能写成 3 个数的平方和。
3. 然后可以根据以上定理和枚举，判断出答案是否为 1, 2, 3，若都不是则答案为 4。
"""


class Solution(object):
    def numSquares(self, n):
        """
        动态规划:
        dp[i] 表示通过平方数组成 i 所需要的最少数量。
        则 dp[i] = min(dp[i-j*j]+1) 其中1<=j<=√i
        dp[n]即为最终答案
        时间复杂度O(n√n)
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = 1 if int(i ** 0.5) == i ** 0.5 else min(dp[i - j ** 2] for j in range(1, int(i ** 0.5) + 1)) + 1
        return dp[n]

    def numSquares2(self, n):
        if int(n ** 0.5) == n ** 0.5:
            return 1
        for i in range(1, int(n ** 0.5) + 1):
            if int((n - i ** 2) ** 0.5) ** 2 == n - i ** 2:
                return 2
        # 先根据公式来缩小n
        while n % 4 == 0:
            n %= 4
        # 如果满足公式 则返回4
        if n % 8 == 7:
            return 4
        # while (t & 3) == 0:
        #     t >>= 2
        # if (t - 7) & 7 == 0:
        #     return 4
        return 3


n = 10
s = Solution()
print(s.numSquares(n))
