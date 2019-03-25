# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        d = {}
        for i in range(n):
            # 字典中没有键的记录则将映射加入字典
            if not s[i] in d:
                # 如果t[i]在字典的值中有记录 说明这个值已经被其他的字母映射了
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            # 有记录的话比对t[i]的值和字典中记录的是否相同
            else:
                if d[s[i]] != t[i]:
                    return False
        return True

    def isIsomorphic2(self, s, t):
        # 同构基础
        if len(set(s))!=len(set(t)):
            return False
        n = len(s)
        d = {}
        for i in range(n):
            # 字典中没有键的记录则将映射加入字典
            if not s[i] in d:
                d[s[i]] = t[i]
            # 有记录的话比对t[i]的值和字典中记录的是否相同
            else:
                if d[s[i]] != t[i]:
                    return False
        return True

s = "ab"
t = "aa"
sol = Solution()
print(sol.isIsomorphic(s,t))