# -*- coding:utf-8 -*


"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        f[i][j] 表示 s1[:i] 和 s2[:j] 能否组成 s3[:k], k = i + j
        可以按 s1[i] 和 s2[j] 是否等于 s3[k] 将所有的状态分为以下情况
        1. s1[i] != s3[k] && s2[i] != s3[k] -> 无法转移
        2. s1[i] == s3[k] -> 从 f[i - 1][j] 转移
        3. s2[j] == s3[k] -> 从 f[i][j - 1] 转移
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        f = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化
        f[0][0] = 1
        for i in range(m):
            if s1[i] != s3[i]:
                break
            f[i + 1][0] = 1
        for i in range(n):
            if s2[i] != s3[i]:
                break
            f[0][i + 1] = 1

        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j
                if s3[k] == s1[i]:
                    f[i][j] |= f[i - 1][j]
                if s3[k] == s2[j]:
                    f[i][j] |= f[i][j - 1]

        return f[m][n] == 1
