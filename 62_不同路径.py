# -*- coding:utf-8 -*-

__author__ = 'huanghf'

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[i][j]表示从第i行第j列到m,n能选择的路径数量
        由于只能向下或者向右走, 最后一行和最后一列一定是1
        dp从倒数第二行开始从后往前填，dp[i][j] = dp[i+1][j] + dp[i][j+1]
        :param m:
        :param n:
        :return:
        """
        dp = [[1 for _ in range(n)] for _ in range(m)] # m行n列
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走就行了
        即C（（m+n-2），（m-1））。
        :param m:
        :param n:
        :return:
        """
        from math import factorial
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))

m = 100
n = 100
s = Solution()
print(s.uniquePaths2(m,n))
