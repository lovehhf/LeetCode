# -*- coding:utf-8 -*-

"""
给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。
请你返回结果字符串。如果无法做到，则返回一个空串。

示例 1：
输入：palindrome = "abccba"
输出："aaccba"

示例 2：
输入：palindrome = "a"
输出：""

提示：
1 <= palindrome.length <= 1000
palindrome 只包含小写英文字母
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        if n & 1 == 0 and all(x == 'a' for x in palindrome):
            return palindrome[:-1] + 'b'
        if n & 1 != 0 and all(x == 'a' for x in palindrome[:n // 2] + palindrome[n // 2 + 1:]):
            if palindrome[n // 2] == 'b':
                return palindrome[:-1] + 'b'
            else:
                return palindrome[:n // 2] + 'b' + palindrome[n // 2 + 1:]
        for i in range(n):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
