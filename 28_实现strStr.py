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


def strStr(haystack,needle):
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

print(strStr("hello","ll"))