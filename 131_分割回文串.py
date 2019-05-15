# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

和全排列类似,dfs
"""


class Solution(object):
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(len(s)):
            tmp = s[:i + 1]
            if tmp==tmp[::-1]:
                self.dfs(s[i + 1:], path + [tmp], res)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res


s = 'aabb'
sol = Solution()
print(sol.partition(s))
