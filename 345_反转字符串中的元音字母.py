# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
"""


def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowel_list = [] # 记录字符串中的元音字母
    index_list = [] # 记录元音字母所在的索引
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            vowel_list.append(s[i])
            index_list.append(i)
    # vowel_list.reverse() # 翻转元音字母列表
    s = list(s)
    for i in index_list:
        s[i] = vowel_list.pop()  # 从后往前取字母
    # print(s)
    return ''.join(s)

print(reverseVowels("leetcode"))
