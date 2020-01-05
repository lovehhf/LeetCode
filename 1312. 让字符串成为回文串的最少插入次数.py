# -*- coding:utf-8 -*-

"""
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 s 成为回文串的 最少操作次数 。

「回文串」是正读和反读都相同的字符串。

 

示例 1：

输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
示例 2：

输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
示例 3：

输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
示例 4：
输入：s = "g"
输出：0
示例 5：
输入：s = "no"
输出：1

提示：
1 <= s.length <= 500
s 中所有字符都是小写字母。

题目等价于让字符串成为回文串的最少删除次数
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        """
        区间dp
        f[i][j] 表示把 i~j 区间的字符串变成回文串所需要的最少操作步数
        初始: 长度为1的字符串操作次数是0

        状态转移方程:
        1. s[i]!=s[j]: 把 i+1~j 或 i~j-1 变成回文串的操作次数 + 1 (插入与s[i]或s[j]相同的字符来抵消它)
           f[i][j] = min(f[i + 1][j], f[i][j - 1]) + 1
        2. s[i]==s[j], 头和尾刚好抵消: f[i][j] = f[i + 1][j - 1]

        :param s:
        :return:
        """
        n = len(s)
        f = [[0] * n for _ in range(n)]
        # 从长度为2的字符串开始枚举
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if s[i] != s[j]:
                    f[i][j] = min(f[i][j - 1], f[i + 1][j]) + 1
                else:
                    # 这里长度为2时 i + 1 > j - 1， f[i + 1][j - 1]=0，所以可以省略 if l!=1 else 0 的判断条件
                    f[i][j] = f[i + 1][j - 1]
        return f[0][n - 1]


sol = Solution()
s = "leetcode"
print(sol.minInsertions(s))