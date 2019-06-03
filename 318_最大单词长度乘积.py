# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。
你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
"""


class Solution(object):
    def maxProduct(self, words):
        """
        用一个26bit的数来存储每一个单词，如果两个数做与运算=0,就表示没有相同的字母，在找出相遇为零的这个字母就可以了
        时间复杂度O(n^2) 不需要转成word,数字与运算比set快
        :param words:
        :return:
        """
        n = len(words)
        mask = [0] * n
        res = 0
        for i in range(n):
            for c in words[i]:
                mask[i] |= 1 << (ord(c) - ord('a'))
        for i in range(n):
            for j in range(i+1,n):
                if mask[i] and mask[j] and mask[i] & mask[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        # print([bin(mask[i])[2:] for i in range(n)])
        return res

    def maxProduct2(self, words):
        """
        时间复杂度>O(n^2)
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        res = 0
        sets = [set(i) for i in words]  # 不预处理的话会超时
        for i in range(n):
            for j in range(i + 1, n):
                if not sets[i] & sets[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res


words = ["abcw","baz","foo","bar","xtfn","abcdef"]

s = Solution()
print(s.maxProduct(words))
print(s.maxProduct2(words))
