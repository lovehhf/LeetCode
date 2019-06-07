# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
 

示例 1：

输出："IDID"
输出：[0,4,1,3,2]
示例 2：

输出："III"
输出：[0,1,2,3]
示例 3：

输出："DDI"
输出：[3,2,0,1]
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        res = [0] * (n+1)
        t = 0
        for i in range(n):
            if S[i]=='I':
                res[i] = t
                t +=1
        res[-1] = t
        t += 1
        for i in range(n-1,-1,-1):
            if S[i]=='D':
                res[i] = t
                t += 1
        return res

S = "DDI"
sol = Solution()
print(sol.diStringMatch(S))