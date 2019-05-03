# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""


class Solution(object):

    def numDecodings(self, s):
        """
        约束版的斐波那契数列 f(n) = f(n-1) + f(n-2);
        其中如果是s[n-1]为0，f(n-1) = 0,f(n) = f(n-2)，因为0无法单独解码，
        而f(n-2)的条件则是必须在1与26之间，否则f(n) = f(n-1)
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            dp[i + 1] = dp[i] if s[i] != '0' else 0
            if i > 0 and (10 <= int(s[i - 1:i + 1]) <= 26):
                dp[i + 1] += dp[i - 1]
        print(dp)
        return dp[-1]

        # if not s:
        #     return 0
        # n = len(s)
        # if s[0] == '0':
        #     return 0
        #
        # dp = [0] * len(s)
        # dp[0] = 1
        #
        # for i in range(1, n):
        #     if s[i] == '0':
        #         if s[i - 1] == '1' or s[i - 1] == '2':
        #             dp[i] = dp[i - 1]
        #         else:
        #             return 0
        #     elif int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
        #         dp[i] = dp[i - 1] + 1
        #     else:
        #         dp[i] = dp[i - 1]
        # print(dp)
        # return dp[-1]

    # def fun(self,s):
    #     """
    #     处理没有0的字符串
    #     :param s:
    #     :return:
    #     111111
    #     1235813
    #     """
    #     n = len(s)
    #     res = [1]*s
    #     for i in range(1, n):
    #         if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
    #             res[i] = res[i - 1] + 1
    #         else:
    #             res[i] = res[i - 1]
    #     return res[-1]


s = '10'
sol = Solution()
print(sol.numDecodings(s))
