# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        动态规划。
        dp[i+1]表示字符串s的前i个字符能否拆分成wordDict。
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



s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print(sol.wordBreak(s,wordDict))