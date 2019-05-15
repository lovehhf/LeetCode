# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

两次动态规划:
第一次dp：计算出每个子串是否是回文串(647. 回文子串)
状态表示: st[i][j]表示s[i:j+1]是否是回文串
状态转移: s[i~j]是回文串当且仅当s[i]==s[j]并且s[i+1~j-1]是回文串 

第二次dp: 
状态表示: f[i]表示前i个字符划分为回文串最少需要划分几部分
状态转移: 枚举最后一段回文串的起点j，然后利用st[j][i]可知s[j~i]是否是回文串，如果是回文串则f[i]可以从f[j-1]+1转移
eg:abb, f[0] = 0,f[1] = 1,b是回文串,f[2]=f[1]+1, 第二个b，枚举abb,bb,b,发现abb不是回文串,bb是回文串,所以f[3]从f[2]转移=f[2]+1=2
"""


class Solution(object):
    def minCut(self, s):
        """
        两次dp
        :param s:
        :return:
        """
        n = len(s)
        st = [[0] * n for _ in range(n)] # st[i,j]表示s[i:j+1]是否是回文串
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i <= 1 and s[i] == s[j]:
                    st[i][j] = 1
                else:
                    if st[i + 1][j - 1] and s[i] == s[j]:
                        st[i][j] = 1
        dp = [0] * (n + 1)  # dp[i]表示s[:i]最少可以分割几次回文串
        for i in range(1, n + 1):
            dp[i] = min([dp[j] + 1 for j in range(i) if st[j][i - 1]])
        return dp[n] - 1

    def minCut2(self, s):
        """
        dfs 妥妥的超时
        res 存储所有可能的分割的次数
        :type s: str
        :rtype: int
        """

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(len(s)):
                t = s[:i + 1]
                if t == t[::-1]:
                    dfs(s[i + 1:], path + 1, res)

        res = []
        dfs(s, 0, res)
        return min(res) - 1


sol = Solution()
s = 'abcc'
print(sol.minCut(s))
print(sol.minCut2(s))
