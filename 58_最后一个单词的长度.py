# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。
"""
def lengthOfLastWord(s):
    s = s.strip()
    s_list = s.split(' ')
    return len(s_list[-1])

print(lengthOfLastWord('a '))