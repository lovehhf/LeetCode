# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

注意:

给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。
示例 1:

输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4

解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
示例 2:

输入: Array = {"10", "0", "1"}, m = 1, n = 1
输出: 2

解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。

给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。

dp(i,j): 使用i个0和j个1的解
Array = ['0', '1', '10', '0001', '111001'], m = 5, n = 3
状态转移方程: 
dp[1,0] = 1
dp[0,1] = 1
dp[1,1] = max(1,dp[0][1]+dp[1][0])=2
dp[3][2] = max(dp[0][1]+dp[2][1],dp[0][2]+dp[1][1]...
dp[5][3] = ...

["111","1000","1000","1000"]
9
3

"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        strs = [(x.count('0'), x.count('1')) for x in strs]
        for a, b in strs:
            if a > m or b > n:
                continue
            for i in range(m, a - 1, -1):
                for j in range(n, b - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - a][j - b] + 1)

        return dp[m][n]

        # res = 0
        # for it in strs:
        #     a, b = it
        #     if a <= m and b <= n:
        #         m -= a
        #         n -= b
        #         res += 1
        # return res


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
s = Solution()
print(s.findMaxForm(strs, m, n))
