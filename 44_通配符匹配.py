# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

动态规划: 
f(i,j)表示s串的前i个字符与p串的前j个字符是否匹配
为了方便算法书写,不妨假设s串和p串下标均从1开始
初始化f(0,0)=true，且f(0,i)=true当且仅当p的前i个字符均为*
状态转移方程: 假设s串的第i个字符为变量x，p串的第j个字符为变量y
f(i,j) = f(i,j)|f(i-1,j-1)当且仅当x==y 或y=='?' 或y=='*'
f(i,j) = f(i,j)|f(i-1,j)|f(i,j-1)当且仅当y="*"
解释：
(1)的含义是s串的第i个字符与p串的第j个字符匹配对应，所以f(i,j)的值可以由f(i−1,j−1))的值来转移。
(2)的含义是，特别地，如果p串的第j个字符为*，则可以让s串的第i个字符同之前的字符一起与这个*对应，或者是s串的第i个字符与p串的第j−1个字符对应（即视作该*匹配空串）。
最终f(m,n)的值表示字符串是否匹配。
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
        dp[0][0] = 1
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = 1
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x, y = s[i - 1], p[j - 1]
                if x == y or y == '?' or y == '*':
                    dp[i][j] = dp[i][j] | dp[i - 1][j - 1]
                if y == '*':
                    dp[i][j] = dp[i][j] | dp[i - 1][j] | dp[i][j - 1]
        # for i in dp:
        #     print(i)
        return dp[m][n] == 1


s = "adceb"
p = "*a*b"
sol = Solution()
print(sol.isMatch(s, p))
