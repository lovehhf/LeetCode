# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

状态转移方程（不对）:n=20 -> 1458=3**6*2!=dp[10]**2
偶数:
dp[i] = dp[i//2]**2 
奇数:
dp[i] = dp[i//2]*dp[i//2+1]

说明: 你可以假设 n 不小于 2 且不大于 58。
"""


class Solution(object):
    def integerBreak(self, n):
        """
        dp
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * 60
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = max(dp[j] * dp[i - j] for j in range(2, i))
        return dp[n]

    def integerBreak2(self, n):
        """
        找规律发现，尽可能多拆一点3值最大
        如果n%3是1，最后的3凑成4
        :param n:
        :return:
        """
        if n==2:
            return 1
        if n==3:
            return 2
        if n%3==0:
            return 3 ** (n // 3)
        if n%3==1:
            return 3 ** (n // 3 - 1) * 4
        return 3 ** (n // 3)*2


s = Solution()
n = 56
print(s.integerBreak(n))
print(s.integerBreak2(n))
