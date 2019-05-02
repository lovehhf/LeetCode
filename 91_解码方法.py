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
    def fun(self,s):
        """
        处理没有0的字符串
        :param s:
        :return:
        111111
        1235813
        """
        n = len(s)
        res = [1]*s
        for i in range(1, n):
            if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i - 1]
        return res[-1]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        if s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 1]
                else:
                    return 0
            elif int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]


s = '1111101111'
sol = Solution()
print(sol.numDecodings(s))
