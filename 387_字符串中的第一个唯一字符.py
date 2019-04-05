# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp_list = [0]*26
        n = len(s)
        for i in s:
            tmp_list[ord(i)-ord('a')] += 1
        for i in range(n):
            if tmp_list[ord(s[i])-ord('a')]==1:
                return i
        return -1

s = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(s))