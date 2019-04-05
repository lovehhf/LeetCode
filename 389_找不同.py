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
        ret = 0
        for c in s + t:
            ret ^= ord(c)
        return chr(ret)

    def findTheDifference2(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if t[i]!=s[i]:
                return t[i]
        return t[-1]

    def findTheDifference3(self, s, t):
        return chr(sum([ord(i) for i in t]) - sum([ord(i) for i in s]))

    def findTheDifference4(self, s, t):
        s, t = list(s), list(t)
        for i in s:
            t.remove(i)
        return t[0]

s = "ae"
t = "aea"
sol = Solution()
print(sol.findTheDifference(s,t))