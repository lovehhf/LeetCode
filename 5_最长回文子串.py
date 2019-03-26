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
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s: str) -> str:
        """
        方法二: 中心扩展算法
        事实上，只需使用恒定的空间，我们就可以在 O(n^2) 的时间内解决这个问题。
        我们观察到回文中心的两侧互为镜像。因此，回文可以从它的中心展开，并且只有 2n - 12n−1 个这样的中心。
        你可能会问，为什么会是 2n - 1个，而不是 n个中心？
        原因在于所含字母数为偶数的回文的中心可以处于两字母之间（例如 abba 的中心在两个b之间）。
        :param s:
        :return:
        """
        if not s:
            return ''
        start, end = 0, 0
        n = len(s)
        for i in range(n):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len_max = max(len1, len2)
            if len_max > end - start:
                start = i - (len_max - 1) // 2
                end = i + len_max // 2
        return s[start:end + 1]

    def is_palindromic_string(self, s):
        return s == s[::-1]

    def longestPalindrome2(self, s: str) -> str:
        """
        方法一: 暴力法
        :param s:
        :return:
        """
        n = len(s)
        # max_alindromic_string = ''
        for i in range(n):
            start = 0
            end = n - i
            # find_flag = 0  # 发现最长回文串的标志，如果发现则中断则标志变为1,中断内外循环
            """
            从最长字符串开始扫,如果不是回文串则扫描的字符串长度递减1
            如果扫描到的是回文串则中断扫描
            """
            while end <= n:
                sub_string = s[start:end]
                if self.is_palindromic_string(sub_string):
                    return sub_string
                    # max_alindromic_string = sub_string
                    # find_flag = 1
                    # break
                start += 1
                end += 1
        #     if find_flag:
        #         break
        # return max_alindromic_string


s = "bababababba"
sol = Solution()

print(sol.longestPalindrome2(s))
print(sol.longestPalindrome(s))
