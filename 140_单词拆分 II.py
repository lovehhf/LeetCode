# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
在真实的面试中遇到过这道题？

加个139判断就不超时了。
"""


class Solution(object):
    def dfs(self, s, wordDict, path, res):
        """
        超时
        :param s:
        :param wordDict:
        :param path:
        :param res:
        :return:
        """
        if not s:
            res.append(path)
            return
        for word in wordDict:
            k = len(word)
            if s[:k] == word:
                self.dfs(s[k:], wordDict, path + [word], res)

    def wordBreak(self, s, wordDict):
        """
        dfs 超时
        加个139题的判断就不会超时了。。。mdzz
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not self.check(s,wordDict):
            return []
        res = []
        self.dfs(s, wordDict, [], res)
        return [' '.join(x) for x in res]

    def wordBreak2(self, s, wordDict):
        """
        尝试空间换时间
        尝试失败 空间爆炸
        :param s:
        :param wordDict:
        :return:
        """
        if not self.check(s,wordDict):
            return []
        n = len(s)
        dp = [[] for _ in range(n)]
        for word in wordDict:
            k = len(word)
            if s[:k] == word:
                dp[k - 1] += [word]
        for i in range(n):
            if not dp[i]:
                continue
            for word in wordDict:
                k = len(word)
                if i + k < n and s[i+1:i + k+1] == word:
                    # print(i,k,s[i:i+k],word,dp[i])
                    for item in dp[i]:
                        dp[i + k].append(item + ' ' + word)
        return dp[n - 1]

    def check(self, s, wordDict):
        """
        139 判断是否有解
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n+1):
            if not dp[i]:
                continue
            for word in wordDict:
                if i+len(word)<=n and s[i:i+len(word)]==word:
                    dp[i + len(word)] = True
        return dp[-1]



s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

sol = Solution()
res2 = sol.wordBreak2(s, wordDict)
print(res2)
# res1 = sol.wordBreak(s,wordDict)
# print(res1)
# print(sorted(res1)==sorted(res2))
