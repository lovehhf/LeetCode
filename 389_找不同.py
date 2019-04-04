# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if t[i]!=s[i]:
                return t[i]
        return t[-1]




s = "ae"
t = "aea"
sol = Solution()
print(sol.findTheDifference(s,t))