# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

画图找规律题:
以n=5为例,根节点有1,2,3,4,5枚举这五种根节点,dp[i]表示n=i时的解
1: 左:dp[0],右:dp[4]
2: 左:dp[1],右:dp[3]
3: 左:dp[2],右:dp[2]
4: 左:dp[3],右:dp[1]
5: 左:dp[4]，右dp:[0]
状态转移方程: dp[i] += dp[j] * dp[i - 1 - j] for j in range(i)
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


s = Solution()
n = 10
print(s.numTrees(n))
