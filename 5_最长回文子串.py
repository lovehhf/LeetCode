# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        方法二: 中心扩展
        首先枚举回文串的中心 i，然后分两种情况向两边扩展边界，直到遇到不同字符为止:
        aba型: 回文串长度是奇数，依次判断 s[i−k]==s[i+k],k=0,1,2,3,…
        abba型: 回文串长度是偶数，依次判断 s[i−k]==s[i+k+1],k=0,1,2,3,…
        时间复杂度O(n^2)
        :param s:
        :return:
        """
        n = len(s)
        count = 0  # 记录最大回文串的长度
        res = ''
        for i in range(n):
            # aba型 初始j,k都指向b,然后j往左扩展 k往右扩展
            j, k = i, i
            while (j >= 0 and k < n):
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k + 1]
                    j -= 1
                    k += 1
                else:
                    break
            # abba型 初始j指向第一个b,k指向第二个b, 然后j往左扩展 k往右扩展
            j, k = i, i + 1
            while (j >= 0 and k < n):
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k + 1]
                    j -= 1
                    k += 1
                else:
                    break
        return res

    def is_palindromic_string(self, s):
        return s == s[::-1]

    def longestPalindrome2(self, s: str) -> str:
        """
        方法一: 暴力法
        从最长字符串开始扫,如果不是回文串则扫描的字符串长度递减1
        如果扫描到的是回文串则中断扫描
        :param s:
        :return:
        """
        n = len(s)
        for i in range(n):
            start = 0
            end = n - i
            while end <= n:
                sub_string = s[start:end]
                if self.is_palindromic_string(sub_string):
                    return sub_string
                start += 1
                end += 1


s = "bababababba"
sol = Solution()

print(sol.longestPalindrome2(s))
print(sol.longestPalindrome(s))
