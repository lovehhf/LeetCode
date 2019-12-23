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

from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        字典 + 双指针实现滑动窗口
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        l, r = 0, 0
        n = len(s)
        res = 0

        while (r < n):
            d[s[r]] += 1
            while (d[s[r]] > 1):
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

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
