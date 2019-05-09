# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        dp[i]:以i结尾新增加的回文子串
        时间复杂度n^2,空间复杂度n
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def is_pal_str(x):
            return x == x[::-1]

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(i, -1, -1):
                if is_pal_str(s[j:i + 1]):
                    dp[i] += 1
        return sum(dp)

    def countSubstrings2(self, s):
        """
        方法二
        dp[i][j]表示s[i~j]是否是回文串
        自定向下dp递推表达式:
        dp[i][j] = s[i] == s[j] if i ==j+1;
        dp[i][j] = dp[i+1][j-1] && s[i]==[j]
        :param s:
        :return:
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if j - i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        # print(i,j)
                        dp[i][j] = 1
        res = sum([x.count(1) for x in dp])
        return res

    def countSubstrings3(self, s):
        """
        方法三:
        中心扩展法 和第5题类似
        :param s:
        :return:
        """

        def count_pal_str(s, start, end):
            num = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                num += 1
                start -= 1
                end += 1
            return num

        res = 0
        for i in range(len(s)):
            res += count_pal_str(s, i, i)  # aba型
            res += count_pal_str(s, i, i + 1)  # abba型
        return res


s = "abcba"
sol = Solution()
print(sol.countSubstrings3(s))
