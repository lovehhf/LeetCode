# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
     
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        遍历一遍s
        使用一个列表存储到遍历到当前字符的无重复字符串
        如果当前字符没有在列表中出现,则添加当前字符 
        否则在列表里面删除重复字符索引前面的所有字符 再在最后加上当前字符
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        res = 0
        for i in range(n):
            if s[i] not in stack:
                stack.append(s[i])
                res = max(len(stack), res)
            else:
                idx = stack.index(s[i])
                stack = stack[idx + 1:] + [s[i]]
        return res

    def lengthOfLongestSubstring2(self, s):
        """
        滑动窗口
        :param s:
        :return:
        """
        n = len(s)
        st = set()
        L, R = 0, 0
        res = 0
        while R < n:
            strlen = len(st)
            st.add(s[R])
            if not strlen == len(st):
                R += 1
                res = max(res, R - L)
            else:
                st.remove(s[L])
                L += 1
        return res

s = Solution()
print(s.lengthOfLongestSubstring2("dvdf"))
