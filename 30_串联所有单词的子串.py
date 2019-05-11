# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        暴力解法 与 28. 实现strStr 类似
        复制一个words列表到tmp,使用cur指针遍历s
        切出和列表里的字符长度相等的字符判断是否存在于tmp列表里面,存在的话就在列表里面删除这个字符串,开始下一轮比较
        如果tmp列表被删光了,说明words中的字符串能组成子串,res列表中添加cur
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not words[0]:
            return []
        m, n = len(words), len(words[0])
        res = []
        cur = 0
        while cur + m * n <= len(s):
            tmp = words.copy()
            for i in range(0, m):
                now_s = s[cur + n * i:cur + n * (i+1)]
                if now_s in tmp:
                    tmp.remove(now_s)
                else:
                    break
            if not tmp:
                res.append(cur)
            cur += 1
        return res


s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
sol = Solution()
print(sol.findSubstring(s, words))
