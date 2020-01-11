# -*- coding:utf-8 -*-

"""
给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：这些子字符串可以写成某个字符串与其自身的串联。

示例 1：

输入：text = "abcabcabc"
输出：3
解释：3 个子字符串分别为 "abcabc" ， "bcabca" 和 "cabcab" 。
示例 2：

输入：text = "leetcodeleetcode"
输出：2
解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。

提示：

1 <= text.length <= 2000
text 只包含小写英文字母。
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        示例1中答案没有 abcabcabc, 说明只是子串只能是两个串联起来, 不能是三个
        暴力出奇迹了...
        :param text:
        :return:
        """
        n = len(text)
        res = set()
        for i in range(n):
            for j in range(1, n):
                if (i + 2 * j > n):
                    break
                s1 = text[i:i + j]
                s2 = text[i + j:i + 2 * j]
                if s1 == s2:
                    res.add(s1 + s2)
        return len(res)
