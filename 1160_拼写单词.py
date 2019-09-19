# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

 

示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：

输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母
"""


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        recode = [0] * 26
        for i in chars:
            recode[ord(i) - ord('a')] += 1
        recode_bak = recode.copy()
        for word in words:
            flag = True
            for i in word:
                key = ord(i) - ord('a')
                recode_bak[key] -= 1
                if recode_bak[key] < 0:
                    flag = False
                    break
            if flag:
                res += len(word)
            recode_bak = recode.copy()
        return res


s = Solution()
words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(s.countCharacters(words, chars))
