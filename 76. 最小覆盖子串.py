# -*- coding:utf-8 -*-

"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""

from collections import defaultdict


class Solution:
    def check(self, d0: defaultdict, d1: defaultdict) -> bool:
        for key in d0.keys():
            if d1[key] < d0[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        d0 = defaultdict(int)
        for c in t:
            d0[c] += 1
        d1 = defaultdict(int)
        n = len(s)
        res = ""
        l, r = 0, 0
        min_length = len(s) + 10

        while (r < n):
            # print(l, r, d0, d1)
            d1[s[r]] += 1

            while(l <= r and self.check(d0, d1)):
                if (r - l + 1) < min_length:
                    res = s[l:r + 1]
                    min_length = r - l + 1
                d1[s[l]] -= 1
                l += 1

            r += 1
        return res


s = Solution()
S = "a"
T = "a"
print(s.minWindow(S, T))
