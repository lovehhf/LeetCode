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

f(i,j) s的前i个字符和p的前j个字符是否匹配
为了方便 假设s串和p串下标均从1开始
平凡转移 
f(i,j)=f(i,j) or f(i−1,j−1)，若 i>0 且 s(i) = p(j) or p(j) = '.'
当 p(j) = '*' 时，
此时 f(i,j) 可以从 f(i,j−2)转移，表示丢弃这一次的'*'。此时若 i>0 且 s(i) = p(j - 1)，则表示这个字符可以利用这个 '*'，
则可以从f(i−1,j−2)转移，表示第一次利用'*'（p[j]重复0次）；也可以从 f(i−1,j) 转移，表示第二次或多次利用 '*'。这里的转移即取 or 操作。

设置f(0,0) = true,循环枚举 i 从 0 到 n；jj 从 1 到 m。

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        s = ' ' + s
        p = ' ' + p
        dp[0][0] = 1
        for i in range(0, m + 1):
            for j in range(1, n + 1):
                if i > 0 and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = dp[i - 1][j - 1] | dp[i][j]
                if p[j] == '*':
                    dp[i][j] = dp[i][j] | dp[i][j - 2]
                    if i > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                        print(i,j, dp[i - 1][j - 2])
                        dp[i][j] = dp[i][j] | dp[i - 1][j] | dp[i - 1][j - 2]
        # for i in dp:
        #     print(i)
        return dp[m][n] == 1

    def isMatch2(self, s, p):
        """
        直接使用re
        :param s:
        :param p:
        :return:
        """
        import re
        value = re.match(p, s)
        if value == None or value.group(0) != s:
            return False
        else:
            return True


s = "aaaaa"
p = "aaa*"
sol = Solution()
print(sol.isMatch(s, p))
