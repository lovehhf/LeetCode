# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

dp[i][j] 从word1[:i]到word2[:j]最小需要多少步
1. word1[i]=word2[j]
dp[i+1][j+1]可以直接从i,j转移过来,dp[i+1][j+1] = dp[i][j]
2. word1[i]!=word2[j]:
dp[i+1][j+1]有3种转移方式
dp[i][j]+1,dp[i + 1][j]+1,dp[i][j + 1]+1 选择代价最低的一种
eg:
word1 = "ab", word2 = "ac"
已知dp[1][2]=1(a+c->ac) dp[2][1]=1(ab->a) dp[1][1]=0(a->a)
dp[2][2]有三种转移方式：
1. 从[1][2]转移过来:1+1
2. 从[2][1]转移过来:1+1
3. 从[1][1]转移过来:0+1
显然直接从[1][1]转移代价最低


"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        dp[i][j] 从word1[:i]到word2[:j]最小需要多少步
        状态转移方程:
        word1[i]=word2[j]: dp[i+1][j+1] = dp[i][j]
        word1[i]!=word2[j]: dp[i+1][j+1] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            dp[0][i] = i
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        for i in dp:
            print(i)
        return dp[m][n]


word1 = "horse"
word2 = "ros"
s = Solution()
print(s.minDistance(word1, word2))
