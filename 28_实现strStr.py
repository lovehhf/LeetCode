# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not n:
            return 0
        if m >= n:
            i = 0
            while i <= m - n:
                if haystack[i] == needle[0]:
                    k = 0
                    for k in range(n):
                        if haystack[i + k] != needle[k]:
                            i += 1
                            break
                        if k == n - 1:
                            return i
                else:
                    i += 1
        return -1

    def strStr2(self, haystack, needle):
        n_length = len(needle)
        h_length = len(haystack)
        if n_length > h_length:
            return -1
        if n_length == 0:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                t = True
                for j in range(1, n_length):
                    if i + j >= h_length:
                        return -1
                    if haystack[i + j] != needle[j]:
                        t = False
                        break
                if t == True:
                    return i

        return -1


s = Solution()
print(s.strStr("mississippi", "issip"))
