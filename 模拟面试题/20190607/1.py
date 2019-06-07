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


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = [0]*26
        for i in t:
            d[ord(i)-ord('a')] += 1
        for i in s:
            d[ord(i) - ord('a')] -= 1
        for i in range(26):
            if d[i]>0:
                return chr(ord('a')+i)



s,t = "abcd","abcde"
sol = Solution()
print(sol.findTheDifference(s,t))