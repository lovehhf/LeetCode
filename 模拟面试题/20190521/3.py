# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

dp[i][j] s前i个字符与p的前j个字符是否匹配
状态转移:
dp[i][j] = 
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = ' ' + s
        p = ' ' + p
        m, n = len(s), len(p)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(1, n):
                if i > 0 and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                if p[j] == '*':
                    dp[i][j] = dp[i][j - 2] | dp[i][j]
                    if i > 0 and (p[j - 1] == '.' or p[j - 1] == s[i]):
                        dp[i][j] = dp[i][j] | dp[i - 1][j] | dp[i - 1][j - 2]
        # print(dp)
        # for i in dp:
        #     print(i)
        return dp[-1][-1] == 1


sol = Solution()
s = "aab"
p = "c*a*b"
print(sol.isMatch(s, p))
