# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        使用字典记录每个字符出现的次数
        如果字符>=2 说明这个字符可以构建字符串
        :param s:
        :return:
        """
        d = {}
        res = 0
        # 遍历s 将字符出现的次数写到字典中
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in d.values():
            res += i//2*2
        # 如果res小于s的长度 那么s还可以拿出一个字符作为回文串的中间字符
        if res<len(s):
            res += 1
        return res

    def longestPalindrome2(self, s: str) -> int:
        return len(s) - max(0, sum([s.count(i) % 2 for i in set(s)]) - 1)


s = "abccccdd"
sol = Solution()
print(sol.longestPalindrome(s))