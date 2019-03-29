# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。
示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window

Intuition
Translation:
Find the longest subarray with at most K zeros.

Explanation
For each A[j], try to find the longest subarray.
If A[i] ~ A[j] has zeros <= K, we continue to increment j.
If A[i] ~ A[j] has zeros > K, we increment i.
"""


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, res = 0, 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            if (K < 0):
                if A[i] == 0:
                    K += 1
                    i += 1
                else:
                    while i<j and A[i] ==1:
                        i+=1
                    K+=1
                    i+=1
            res = max(res,j-i+1)
        return res
            # K -= 1-A[j]
            # if K<0:
            #     K+=1-A[i]
            #     i+=1
        # return j-i+1


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3
s = Solution()
print(s.longestOnes(A, K))
