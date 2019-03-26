# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        方法一 字符串排序后比较
        :param s:
        :param t:
        :return:
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        方法二 借助字典
        :param s:
        :param t:
        :return:
        """
        if len(s)!=len(t):
            return False
        d = {}
        n = len(s)
        for i in range(n):
            d[s[i]] = d.get(s[i],0) + 1
            d[t[i]] = d.get(t[i],0) - 1
        for v in d.values():
            print(v)
            if v != 0:
                return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        """
        方法二 借助列表
        :param s:
        :param t:
        :return:
        """
        if len(s)!=len(t):
            return False
        # 列表存放a-z 26字母的计数
        l = [0]*26
        n = len(s)
        for i in range(n):
            l[ord(s[i]) - ord('a')] += 1
            l[ord(t[i]) - ord('a')] -= 1
        return l == [0]*26

s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram3(s,t))
